from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = "itsjustasecretkeylol"

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongodb:27017/vulndb")
client = MongoClient(MONGO_URI)
db = client.get_default_database()
users = db.users

@app.route("/", methods=["GET"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    user = users.find_one({"username": session["username"]})
    if not user:
        session.clear()
        return redirect(url_for("login"))

    return render_template("index.html", user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    data = request.get_json(force=True)
    query = {"username": data.get("username"), "password": data.get("password")}

    user = users.find_one(query)
    
    if user and isinstance(data.get("username"), str) and isinstance(data.get("password"), str):
        session["username"] = user["username"]
        return jsonify({"redirect": "/"})

    elif user and user["username"] == "mongo":
        return jsonify({"message": f"Найден пользователь: {user['username']}, но авторизация не выполнена"}), 200

    return jsonify({"message": "Неверные данные"}), 401

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)