{
    'name': 'Multiuser ToDo',
    'description': 'Extend the ToDo app to multi-user',
    'author': 'Juan Arillo',
    'depends': [
        'todo-tasks',
        'mail'
    ],
    'data': ['views/todo_task.xml',
             'security/todo_access_rules.xml'
    ],
}