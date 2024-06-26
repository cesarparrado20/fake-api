from flask import Flask, jsonify
import commons

app = Flask(__name__)


@app.route("/")
@commons.api_logger
def home():
    return "This is a fake api."


@app.route("/notifications", methods=["POST"])
@commons.api_logger
def notifications():
    error = None
    success = False
    if not success:
        error = "SMS send rate limit exceeded"
    return jsonify(
        {"payload": {"success": success, "channel": "SMS", "error": error}}
    )
