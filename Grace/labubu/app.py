from flask import Flask, render_template
import random

app = Flask(__name__)

QUOTES = [
    "Stay pawsitive and keep going!",
    "You’ve got this — one whisker at a time!",
    "Focus like a cat stalking success.",
    "Small steps, big purr-ogress!",
    "Take a deep breath. Stretch. FocusFlow."
]

@app.route("/")
def home():
    quote = random.choice(QUOTES)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
