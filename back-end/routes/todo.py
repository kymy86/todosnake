from flask import Blueprint
from flask_restful import Api

from resources import TodoResource

TODO_BLUEPRINT = Blueprint('todo', __name__)
Api(TODO_BLUEPRINT).add_resource(
    TodoResource,
    '/todo/<string:todo_name>',
    '/todo/'
)