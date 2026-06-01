from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_sentiment(text):

    score = analyzer.polarity_scores(text)

    compound = score["compound"]

    if compound >= 0.3:
        return "calm"

    elif compound <= -0.3:
        return "frustrated"

    else:
        return "neutral"