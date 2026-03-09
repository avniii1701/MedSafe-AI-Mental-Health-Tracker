from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive 😊", "Keep doing things that make you happy!"
    elif polarity < 0:
        return "Negative 😔", "Take a break, talk to someone, or relax."
    else:
        return "Neutral 😐", "Your mood seems balanced today."

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    suggestion = None

    if request.method == "POST":
        text = request.form["text"]
        sentiment, suggestion = analyze_sentiment(text)

    return render_template("index.html", sentiment=sentiment, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
