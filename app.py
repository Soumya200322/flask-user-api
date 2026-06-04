from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data
users = [
    {"id": 1, "name": "Soumya"},
    {"id": 2, "name": "Rahul"}
]

# Home Route
@app.route('/')
def home():
    return "Flask User API is Running!"

# GET ALL USERS
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET USER BY ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404

# ADD USER
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    if not data or "name" not in data:
        return jsonify({"message": "Name is required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(new_user)

    return jsonify(new_user), 201

# UPDATE USER
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404

# DELETE USER
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
    