from re import I
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

comments = [
    {
        "post_id" : 1,
        "comment" : [
            {
            "id" : 1,
            "content" : "Nice pic!"
            }
        ]
    }
]

#as

@app.route("/posts/<id>/comments",methods=['GET'])
def get_comments(id):
    return jsonify(comments), 200

@app.route("/posts/<id>/comments",methods=['POST'])
def post_comments(id):
    id = int(id)
    commentId = random.randint(1,4)
    content = request.form.get('content')    
    index = None

    i = 0;
    for comment in comments:
        if comment["post_id"] == id:
            index = i 
            break 
        i += 1

    print("index: ", index)

    if index is not None:
        comments[index]["comment"].append({"id" : commentId, "content" : content})
    else:
        comments.append({
            "post_id" : id,
            "comment" : [{"id" : commentId, "content" : content}]
        })

    return jsonify(status='created'), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)