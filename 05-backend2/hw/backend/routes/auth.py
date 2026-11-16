from datetime import datetime, timedelta, timezone
from functools import wraps

import jwt
from flask import Blueprint, g, jsonify, request

auth_bp = Blueprint("auth", __name__)

SECRET_KEY = "swef-dev-secret-key-for-homework-five"

# Hardcoded for now since we haven't learned databases yet
USERS = {"thaddius": "swef2026"}


def create_access_token(username):
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "Missing token"}), 401
        token = header.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid or expired token"}), 401
        g.username = payload["sub"]
        return f(*args, **kwargs)
    return wrapper


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password or USERS.get(username) != password:
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"access_token": create_access_token(username), "token_type": "bearer"})


@auth_bp.get("/me")
@require_auth
def me():
    return jsonify({"message": f"Welcome, {g.username}!"})
