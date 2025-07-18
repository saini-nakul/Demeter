from Scraper.reddit import RedditScraper
from Logic.sentiment import calculate_polarity
from Logic.analysis import count_sentiment

topic = "government"
scraper = RedditScraper(topic, limit=10)
scraper.scrape_top_posts()
comments_list = scraper.scrape_comments("https://www.reddit.com/r/Minecraft/comments/hi22zu/hope_this_makes_your_day_better/")
score_dict = calculate_polarity(comments_list)

pos, neu, neg = count_sentiment(score_dict)
print(pos, neu, neg)

