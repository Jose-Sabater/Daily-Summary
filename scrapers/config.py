nyt_config = {
    "url": "https://www.nytimes.com/",
    "story_wrapper_class": "story-wrapper",
    "title_class": "indicate-hover",
    "summary_class": "summary-class",
    "rate_limit": 2,  # seconds between requests
}

tg_config = {
    "url": "https://www.theguardian.com/world",
    "headline_tag": "aria-label",
    "region_container": "container-",
    "regions": {
        "africa": 2,
        "americas": 2,
        "europe": 4,
        "middle-east": 2,
        "south-and-central-asia": 2,
        "uk": 2,
        "us": 3,
    },
    "rate_limit": 2,  # seconds between requests
}
