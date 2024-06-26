from flask import Flask, jsonify
import commons

app = Flask(__name__)


@app.route("/")
@commons.api_logger
def home():
    return "This is a fake api."


@app.route("/api/login/", methods=["POST"])
@commons.api_logger
def login():
    return jsonify({"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"})


@app.route("/api/tarifas/deposito/", methods=["POST", "PUT"])
@commons.api_logger
def tarifas():
    return "OK", 201


@app.route(
    "/api/tarifas/deposito/<id>/unidad_captura/", methods=["POST", "PUT"]
)
@commons.api_logger
def unidad_captura(id: str):
    return "OK", 201
