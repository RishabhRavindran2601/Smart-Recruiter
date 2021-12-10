from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

from chat import get_response

app = Flask(_name_)
CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer" : response}
    return jsonify(message)


if _name_ == "_main_":
    app.run(debug=True)