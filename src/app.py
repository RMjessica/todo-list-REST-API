from flask import Flask, jsonify
from flask import request
import json


app = Flask(__name__)

todos = [
    {"label": "Meal-prep for the week", "done": False},
    {"label": "Finish todo-list-API", "done": True}
]


@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():

    if request.method == 'GET':
        json_text = jsonify(todos)

        return json_text

    elif request.method == 'POST':
        request_body = json.loads(request.data)
        todos.append(request_body)
        json_todos = jsonify(todos)

        return json_todos

    return ({'msg': f'Bad request. ${request.method} is not avaliable'}, 400)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)

    return json_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
