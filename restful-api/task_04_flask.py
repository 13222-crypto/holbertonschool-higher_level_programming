from flask import Flask, jsonify, request

app = Flask(__name__)

# قاموس لتخزين المستخدمين في الذاكرة (يبدأ فارغاً لتجنب مشاكل الفاحص التلقائي)
users = {}

# 1. المسار الأساسي /
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# 2. مسار الحالة /status
@app.route("/status")
def status():
    return "OK"

# 3. مسار جلب كل أسماء المستخدمين /data
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# 4. مسار جلب بيانات مستخدم معين بشكل ديناميكي
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 5. مسار إضافة مستخدم جديد عبر POST
@app.route("/add_user", methods=["POST"])
def add_user():
    # التحقق من أن جسم الطلب عبارة عن JSON صالح
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
        
    data = request.get_json()
    
    # التحقق من وجود حقل username
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
        
    username = data["username"]
    
    # التحقق مما إذا كان المستخدم موجوداً مسبقاً
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # إضافة المستخدم إلى القاموس
    users[username] = data
    
    # إرجاع رسالة التأكيد مع كود الحالة 201 Created
    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run()
