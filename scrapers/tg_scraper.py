import sys
import os
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time
import logging
from scrapers.base_scraper import BaseScraper

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import from utils
from utils.summarization import Summarizer

summarizer = Summarizer()


class TheGuardianScraper(BaseScraper):
    def __init__(self, config: dict):
        super().__init__(config)
        logging.info("Initiating TheGuardian Scraper")
        self.fetch_page()
        if self.soup:
            logging.info("Page fetched")
        else:
            logging.warning("Failed to fetch page")

    def get_article_list(self, n_articles: int = 30) -> List[Dict[str, str]]:
        articles = {}
        for region, nr_articles in self.config["regions"].items():
            container = self.soup.find(
                "div", id=f"{self.config['region_container']}{region}"
            )
            # print(f"{self.config['region_container']}{region}")
            # print("####################")
            # print(container)
            if container:
                stories = []
                for tag in container.find_all("a")[:nr_articles]:
                    story = {
                        "headline": tag.get(
                            self.config["headline_tag"], "No headline available"
                        ),
                        "link": "https://www.theguardian.com" + tag.get("href", ""),
                    }
                    try:
                        response = requests.get(story["link"])
                        content_soup = BeautifulSoup(response.content, "html.parser")
                        content = content_soup.find(
                            class_=lambda x: x and x.startswith("article-body")
                        ).text
                        story["content"] = content
                        stories.append(story)
                        story["summary"] = summarizer.summarize(content)
                        time.sleep(self.config["rate_limit"])  # Throttle requests
                    except Exception as e:
                        logging.error(
                            f"Failed to fetch content for {story['headline']}: {e}"
                        )
                articles[region] = stories if stories else None
            else:
                articles[region] = None
        return articles
