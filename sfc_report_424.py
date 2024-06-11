from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route("/")
def home():
    return "This is a fake api."


@app.route("/api/login/", methods=["POST"])
def login():
    return jsonify({"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"})


@app.route("/api/tarifas/deposito/", methods=["POST", "PUT"])
def tarifas():
    print(request.data)
    print(request.json)
    return "OK", 201


@app.route("/api/tarifas/deposito/<id>/unidad_captura/", methods=["POST", "PUT"])
def unidad_captura(id):
    print(id)
    print(request.data)
    print(request.json)
    return "OK", 201
