import sys
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Performs sentiment analysis using VADER."""
    sentiment_score = analyzer.polarity_scores(text)
    compound = sentiment_score['compound']
    sentiment = "positive" if compound > 0.05 else "negative" if compound < -0.05 else "neutral"
    return {"sentiment": sentiment, "score": sentiment_score}

# If script is executed from command line
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        result = analyze_sentiment(input_text)
        print(json.dumps(result))
    else:
        print(json.dumps({"error": "No input provided"}))
