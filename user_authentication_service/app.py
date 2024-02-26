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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    '''
    POST /sessions
    JSON body:
            - email
            - password
    Return:
            redirect main or 403 error
    '''

    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
