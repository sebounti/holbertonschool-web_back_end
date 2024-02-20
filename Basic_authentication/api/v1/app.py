import os
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.auth.auth import Auth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

auth_type = os.getenv("AUTH_TYPE")  # Utilisation de os.getenv directement

if auth_type:
    if auth_type == "custom_auth":
        from api.v1.auth.auth import Auth
        auth = Auth()

@app.errorhandler(404)
def not_found(error):
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def Unauthorized(error):
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def Forbidden(error):
    """ Forbidden Handler """
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def handle_before_request():
    """ Request validation """
    if auth is None:
        return
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
