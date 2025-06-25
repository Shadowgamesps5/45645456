
from flask import Flask, render_template
import random
import threading
import time

app = Flask(__name__)

top_users = [
    {"name": "User1", "likes": 100},
    {"name": "User2", "likes": 90},
    {"name": "User3", "likes": 80},
    {"name": "User4", "likes": 70},
    {"name": "User5", "likes": 60}
]

def simulate_likes():
    while True:
        user = random.choice(top_users)
        user["likes"] += random.randint(1, 3)
        top_users.sort(key=lambda x: x["likes"], reverse=True)
        time.sleep(2)

@app.route("/")
def overlay():
    return render_template("template.html", users=top_users)

if __name__ == "__main__":
    threading.Thread(target=simulate_likes, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
