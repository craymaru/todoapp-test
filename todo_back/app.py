from chalice import Chalice, NotFoundError
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
