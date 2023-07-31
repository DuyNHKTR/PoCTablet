import os
import json
import sys


from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Function to load user data from users.json
def load_users():
    with open('static/users.json', 'r', encoding='utf-8') as file:
        users_data = json.load(file)
    return users_data

# Function for facial recognition (dummy implementation)
def recognize_face(image_data):
    # In a real implementation, you would use a facial recognition model
    # to check if the provided image_data matches any user in the database.
    # For this example, we'll use a dummy implementation that always returns True.
    return True

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    users_data = load_users()
    user = next((user for user in users_data if user["username"] == username and user["password"] == password), None)

    if user:
        session["isLoggedIn"] = True
        session["user"] = user  # Store the user data in the session
        return redirect("/dashboard")
    else:
        return redirect("/?error=invalid_credentials")

@app.route("/dashboard")
def dashboard():
    if not session.get("isLoggedIn"):
        return redirect("/")

    user = session.get("user")
    if not user:
        return redirect("/?error=user_not_found")

    return render_template("dashboard.html", user=user)

@app.route("/faceid")
def faceid():
    # Facial recognition logic here...
    # Store the recognized user data in "user" variable

    session["isLoggedIn"] = True
    session["user"] = user  # Store the recognized user data in the session
    return redirect("/dashboard")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    
    app.run(host="0.0.0.0", threaded=True, debug=True)
