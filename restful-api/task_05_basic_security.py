from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# إعداد مفتاح السري لـ JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# قاعدة بيانات المستخدمين في الذاكرة طبقاً للمواصفات
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- إعدادات Basic Authentication ---
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def basic_auth_error(status):
    return jsonify({"error": "Unauthorized access"}), 401


# --- معالجة أخطاء JWT المخصصة لترد دائماً بـ 401 طبقاً للتعليمات ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# --- المسارات (Endpoints) ---

# 1. مسار محمي بـ Basic Auth
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# 2. مسار تسجيل الدخول للحصول على توكين JWT
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
        
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
        
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # إضافة الدور (role) داخل الـ payload الخاص بالتوكين
        additional_claims = {"role": user["role"]}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify({"access_token": access_token}), 200
        
    return jsonify({"error": "Invalid credentials"}), 401

# 3. مسار محمي بـ JWT لجميع المستخدمين
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# 4. مسار محمي بـ JWT ومخصص للمسؤولين فقط (Admin Role)
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
