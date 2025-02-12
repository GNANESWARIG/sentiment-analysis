import sys
import json
from textblob import TextBlob

# Read input from PHP (Command-line argument)
if len(sys.argv) > 1:
    input_text = sys.argv[1]
    
    # Perform sentiment analysis
    analysis = TextBlob(input_text)
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"

    # Return JSON response
    print(json.dumps({"sentiment": sentiment}))
else:
    print(json.dumps({"error": "No input provided"}))
