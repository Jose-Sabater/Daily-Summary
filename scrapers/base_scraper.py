import time
import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from requests.exceptions import RequestException


class BaseScraper(ABC):
    def __init__(self, config):
        self.config = config
        self.soup = None

    def fetch_page(self):
        try:
            response = requests.get(self.config["url"], timeout=5)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            self.soup = BeautifulSoup(response.text, "html.parser")
        except RequestException as e:
            print(f"Request failed: {e}")
            self.soup = None  # Ensuring soup is None if request fails

    @abstractmethod
    def get_article_list(self, n_articles: int = 30) -> list[dict[str, str]]:
        pass

    def sleep(self):
        time.sleep(
            self.config.get("rate_limit", 1)
        )  # Default to 1 second if not specified
