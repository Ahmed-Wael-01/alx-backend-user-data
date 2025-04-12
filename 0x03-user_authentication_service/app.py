#!/usr/bin/env python3
""" the flask app
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=['DELETE'])
def logout():
    """ logout route
    """
    user = AUTH.get_user_from_session_id(request.cookies.get('session_id'))
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    abort(403)


@app.route("/profile", methods=['GET'])
def profile():
    """ profile route
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """ gets a reset token
    """
    try:
        token = AUTH.get_reset_password_token(request.form['email'])
    except Exception:
        abort(403)
    return jsonify({"email": request.form['email'], "reset_token": token})


@app.route("/reset_password", methods=['PUT'])
def update_password():
    """ updates password
    """
    try:
        AUTH.update_password(request.form['reset_token'],
                             request.form['new_password'])
    except Exception:
        abort(403)
    return jsonify({"email": request.form['email'],
                    "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
