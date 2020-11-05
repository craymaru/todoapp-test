BLUE_ THREE = [
    { 'id': 'L5',
      'title':'夢の舞台へ駆け上がる',
      'memo': 'TONOSAKI',
      'priority': 3,
      'completed': False,
    },
    { 'id': 'L6',
      'title':'今ここで魅せる',
      'memo': 'GENDA',
      'priority': 2,
      'completed': False,
    },
    { 'id': 'L8',
      'title':'その瞬間を掴む',
      'memo': 'KANEKO',
      'priority': 1,
      'completed': False,
    } 
]

# すべてのレコードを修得
def get_all_todos():
    return BLUE_THREE


# IDからレコードを修得
def get_todo(todo_id):
  for todo in BLUE_THREE:
    if todo['id'] == todo_id:
      return todo
    return None