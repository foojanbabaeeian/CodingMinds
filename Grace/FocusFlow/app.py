from flask import Flask, render_template, jsonify
import random, json, os
from datetime import date

app = Flask(__name__)

DATA_FILE = "user_data.json"

QUOTES_FOCUS = [
    "Small steps make big dreams bloom.",
    "Focus like the gentle flow of a stream.",
    "You’re doing amazing — one moment at a time.",
    "Every minute of focus is a gift to your future self."
]

QUOTES_BREAK = [
    "Time to rest your mind — you’ve earned it.",
    "Breathe in peace, breathe out worry.",
    "Stretch a little. Your bunny’s proud of you!",
    "Rest isn’t wasting time — it’s recharging your light."
]

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"completed_sessions": 0, "last_date": "", "streak": 0}, f, indent=4)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# home route
@app.route("/")
def home():
    quote_focus = random.choice(QUOTES_FOCUS)
    quote_break = random.choice(QUOTES_BREAK)
    user_data = load_data()
    return render_template("index.html", 
                           quote_focus=quote_focus,
                           quote_break=quote_break,
                           sessions=user_data["completed_sessions"],
                           streak=user_data["streak"])

@app.route("/complete", methods=["POST"])
def complete_session():
    data = load_data()
    today = str(date.today())

    # Update completed sessions
    data["completed_sessions"] += 1

    # Update streak logic
    if data["last_date"] == "":
        data["streak"] = 1
    elif data["last_date"] == today:
        pass  # same day, do not add
    else:
        data["streak"] += 1
    data["last_date"] = today

    save_data(data)
    return jsonify(data)

# navigate to the pomo page
@app.route("/pomo")
def pomo():
    quote_focus = random.choice(QUOTES_FOCUS)
    quote_break = random.choice(QUOTES_BREAK)
    user_data = load_data()
    return render_template("pomo.html",
                           quote_focus=quote_focus,
                           quote_break=quote_break,
                           sessions=user_data["completed_sessions"],
                           streak=user_data["streak"])


if __name__ == "__main__":
    app.run(port=5001, debug=True)
