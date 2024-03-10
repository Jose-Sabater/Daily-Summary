from bs4 import BeautifulSoup
import requests


class BaseScraper:
    def get_article_list(self) -> list[dict[str, str]]:
        pass


class NYT(BaseScraper):
    def __init__(self):
        self.url = "https://www.nytimes.com/"
        self.soup = BeautifulSoup(requests.get(self.url).text, "html.parser")
        self.stories = self.soup.find_all("section", class_="story-wrapper")

    def get_article_list(self, n_articles: int = 30) -> list[dict[str, str]]:
        """Retrieves the first n articles from nytimes"""
        news_articles = []
        for element in self.stories:
            article_dict = {}
            try:
                title = element.find_all("p", class_="indicate-hover")[0].text
            except Exception as e:
                title = ""
                continue

            try:
                summary = element.find_all("p", class_="summary-class")[0].text
            except Exception as e:
                summary = ""
                continue
            try:
                link = element.find("a").attrs["href"]
            except Exception as e:
                link = ""
            article_dict["title"] = title
            article_dict["summary"] = summary
            article_dict["link"] = link
            news_articles.append(article_dict)

        return news_articles[:n_articles]
