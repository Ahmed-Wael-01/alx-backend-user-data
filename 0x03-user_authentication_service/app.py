#!/usr/bin/env python3
""" the flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def openning():
    """ beginning route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """ users end point
    """
    try:
        AUTH.register_user(request.form['email'], request.form['password'])
        return jsonify({"email": request.form['email'],
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    """ login route
    """
    if not AUTH.valid_login(request.form['email'], request.form['password']):
        abort(401)
    session_id = AUTH.create_session(request.form['email'])
    res = jsonify({"email": request.form['email'], "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
