from flask import Flask
import os

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))
MESSAGE = os.getenv("PONG_MESSAGE", "Pong")

@app.route("/ping")
def ping():
    return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)