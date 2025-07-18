from flask import Flask, request, jsonify
from Scraper.reddit import RedditScraper
from flask_cors import CORS
from Logic.sentiment import calculate_polarity
from Logic.analysis import count_sentiment

app = Flask(__name__)
CORS(app)


@app.route('/api/scrape', methods=['POST'])
def handle_scrape():
    data = request.get_json()
    topic = data.get('topic')
    print("This is the topic which we want to see. Also CKBH: ", topic)

    if not topic:
        return jsonify({'error': 'No topic provided'}), 400
    
    scraper = RedditScraper(topic, limit=10)

    post = scraper.scrape_top_posts()
    comments = scraper.scrape_comments(post["reddit_url"])
    score = calculate_polarity(comments)
    pol_count = count_sentiment(score)
    pos, neu, neg, = pol_count

    return jsonify({
        "topic": topic,
        "post": post,
        "score": score,
        "pol_count": {
            "positive": pos,
            "neutral": neu,
            "negative": neg
        }
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

