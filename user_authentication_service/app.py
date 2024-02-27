#!/usr/bin/env python3
'''
flask module
'''

from flask import Flask, jsonify, request, abort, redirect, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    '''GET /
    Return:
      - welcome message
    '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    '''POST /users
    JSON body:
      - email
      - password
    Return:
      - user
    '''
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        abort(400, description="email and password are required")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        abort(400, description="email already exists")


@ app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Sessions Login User """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(401)

    if (AUTH.valid_login(email, pwd)):
        session_id = AUTH.create_session(email)
        if session_id is not None:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response

    abort(401)


@ app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    '''
    logout session
    '''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        Auth.destroy_session(user.id)
        return redirect('GET /')

    if session_id is None or not AUTH.get_user_from_session_id(session_id):
        abort(403)


@ app.route('/profile', methods=['POST'])
def profile() -> str:
    '''
    profile
    '''
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    message = {"email": user.email}
    return jsonify(message), 200


@ app.route('/reset_password', methods=['GET'], strict_slashes=True)
def get_reset_password_token() -> str:
    '''
    reset password
    '''
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    message = {"email": email, "reset_token": token}
    return jsonify(message), 200


@ app.route('/reset_password', methods={'PUT'})
def update_password() -> str:
    '''
    update password
    '''
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_password = request.form['new_password']
    except KeyError:
        abort(403)

    AUTH.update_password(reset_token, new_password)
    return jsonify({"email": f"{email}",
                    "message": "Password updated"}), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
