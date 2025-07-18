from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def calculate_polarity(comments):
    
    polarity_score_dict = {}

    sentiment_analyser = SentimentIntensityAnalyzer()

    for comment in comments:
        polarity_score_dict[comment] = sentiment_analyser.polarity_scores(comment)

    return polarity_score_dict




