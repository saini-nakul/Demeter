import praw

class RedditScraper:
    def __init__(self, topic, limit):
        print("Reddit Scraper Initialised")
        self.topic = topic
        self.limit = 10
        self.reddit = praw.Reddit(
                        client_id="-80YrjTmuTWDLIBUVo66nw",
                        client_secret="XOEsI5qByY4OhBT4YWk8Hz5lH1DCfA",
                        user_agent="saininakull"
                        )

    def scrape_top_posts(self):
        try:
            subreddit = self.reddit.subreddit(self.topic)

            for post in subreddit.top(limit=10):
                reddit_url = "https://www.reddit.com" + post.permalink
                print(f"Title: {post.title}")
                print(f"Score: {post.score}")
                print(f"Reddit Link: {reddit_url}")
                print(f"External Link: {post.url}")
                print("-" * 40)

        except Exception as e:
            print(f"Can't Scrape {self.topic} - {e}")



    def scrape_comments(self, post_url):

        comments = []

        try:
            submission = self.reddit.submission(url=post_url)
            submission.comments.replace_more(limit=1) 
            for comment in submission.comments.list():
                # print(comment)
                comments.append(comment.body)
            return comments

        except Exception as e:
            print(f"Can't Scrape comments due to - {e}")