from flask import Flask, jsonify, request
import random

app = Flask(__name__)

posts_obj = [{"id" : 1, "name" : "saifu"}, {"id" : 2, "name" : "khan"}]

@app.route("/posts",methods=['GET'])
def get_post() -> str:
    return jsonify(posts_obj), 200

@app.route("/posts",methods=['POST'])
def create_post() -> str:
    id = random.randint(99,999)
    name = request.form.get("name")
    post_obj = {
        "id" : id,
        "name" : name
    }
    posts_obj.append(post_obj)
    return jsonify({"message" : "success"}), 201

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)