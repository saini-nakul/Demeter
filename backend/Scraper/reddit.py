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
            posts_data = []

            for post in subreddit.top(limit=10):
                reddit_url = "https://www.reddit.com" + post.permalink
                post_info = {
                    "title": post.title,
                    "score": post.score,
                    "reddit_url": reddit_url,
                    "external_url": post.url
                }
                posts_data.append(post_info)

            # Sort by score (descending)
            posts_data.sort(key=lambda x: x["score"], reverse=True)

            # Return the top post only
            return posts_data[0] if posts_data else None

        except Exception as e:
            print(f"Can't Scrape {self.topic} - {e}")
            return None

        



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