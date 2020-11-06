from chalice import Chalice
from chalice import BadRequestError, NotFoundError
from chalicelib import database

app = Chalice(app_name='todo_back')


@app.route('/todos', methods=['GET'])
def get_all_todos():
    return database.get_all_todos()

@app.route('/todos/{todo_id}', methods=['GET'])
def get_todo(todo_id):
    todo = database.get_todo(todo_id)
    if todo:
        return todo
    else:
        raise NotFoundError('Todo not found.') #404

@app.route('/todos', methods=['POST'])
def create_todo():
    # リクエストメッセージjson_bodyを修得
    todo = app.current_request.json_body

    # 必須項目をチェック
    for key in ['title', 'memo', 'priority']:
        if key not in todo:
            raise BadRequestError(f"{key} is required.")

    # データを登録
    return database.create_todo(todo)
    

@app.route('/todos/{todo_id}', methods=['PUT'])
def update_todo(todo_id):
    changes = app.current_request.json_body

    # データを更新
    return database.update_todo(todo_id, changes)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
