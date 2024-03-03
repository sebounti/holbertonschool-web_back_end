#!/usr/bin/env python3
'''
flask module
'''

from flask import Flask, jsonify, request, abort, redirect, make_response
from sqlalchemy.orm.exc import NoResultFound
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
    '''
        Register a user
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
    Logout route. This function handles the DELETE request to /sessions.

    Returns:
        str: A message indicating success or failure.
    '''
    session_id = request.cookies.get('session_id')

    try:
        user = AUTH.get_user_from_session_id(session_id)
        Auth.destroy_session(user.id)
        return redirect("http://localhost:5000/", 302)

    except Exception:
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


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    '''
    Reset password route.function handles the POST request to /reset_password.

    Returns:
        str:JSON response containing the email and reset token, or a 403 error.
    '''
    # Extract email from form data
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": "{}".format(email),
                        "reset_token": "{}".format(reset_token)})
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ This function handles the PUT request to /reset_password."""

    # Extract email, reset token, and new password from form data
    email = request.form.get('email')
    token = request.form.get('reset_token')
    password = request.form.get('new_password')

    try:
        # Attempt to update the password using the provided reset token
        AUTH.update_password(token, password)

        # If successful, return JSON response indicating success
        return jsonify({"email": "{}".format(email),
                        "message": "Password updated"}), 200

    except Exception:
        # If an error occurs, abort with 403 error
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
