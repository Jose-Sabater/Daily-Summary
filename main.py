from scrapers.tg_scraper import TheGuardianScraper
from scrapers.nyt_scraper import NYTScraper
from scrapers import config
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    # nyt_scraper = NYTScraper(config=config.nyt_config)
    # articles_nyt = nyt_scraper.get_article_list(30)
    # print("NYT articles:")
    # print(articles_nyt)
    tg_scraper = TheGuardianScraper(config=config.tg_config)
    articles_tg = tg_scraper.get_article_list(30)
    print("The Guardian articles:")
    print(articles_tg)
