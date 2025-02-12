from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Enable CORS for frontend communication

@app.route("/")
def home():
    return render_template("index.html")  # Ensure 'index.html' is inside 'templates/'

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.json
    if not data or "text" not in data or not data["text"].strip():
        return jsonify({"error": "Text input is empty"}), 400

    text = data["text"]
    analysis = TextBlob(text)
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Runs on localhost:5000
