from flask import Flask, jsonify
from flask import request
import json


app = Flask(__name__)

todos = [
    {"label": "Meal-prep for the week", "done": False},
    {"label": "Finish todo-list-API", "done": True}
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():

    request_body = json.loads(request.data)
    todos.append(request_body)
    json_todos = jsonify(todos)

    return json_todos


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
