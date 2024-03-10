from typing import List, Dict
from base_scraper import BaseScraper


class NYTScraper(BaseScraper):
    def __init__(self, config: dict):
        super().__init__(config)
        self.fetch_page()
        if self.soup:
            self.stories = self.soup.find_all(
                "section", class_=self.config["story_wrapper_class"]
            )
        else:
            self.stories = []

    def get_article_list(self, n_articles: int = 30) -> List[Dict[str, str]]:
        if not self.soup:  # Check if soup is None (request failed)
            return []
        news_articles = []
        for element in self.stories[:n_articles]:
            try:
                title = element.find("p", class_=self.config["title_class"]).text
                summary = element.find("p", class_=self.config["summary_class"]).text
                link = element.find("a").get("href")
                news_articles.append({"title": title, "summary": summary, "link": link})
                # self.sleep()  # Enforce rate limit after processing each article
            except AttributeError:  # Catching if any attributes are not found
                continue  # Skip this element and continue with the next
        return news_articles


# Usage example
if __name__ == "__main__":
    from config import nyt_config

    nyt_scraper = NYTScraper(nyt_config)
    articles = nyt_scraper.get_article_list(30)
    print(articles)
