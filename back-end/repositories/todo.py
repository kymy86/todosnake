from models import Todo
from sqlalchemy.exc import IntegrityError

class TodoRepo:

    @staticmethod
    def get(todo_name):
        return Todo.query.filter_by(
            todo_name=todo_name
        ).one_or_none()

    def update(self, todo_name, is_complete):
        todo = self.get(todo_name)
        if todo is None:
            return None
        todo.is_complete = bool(is_complete)
        return todo.save()

    @staticmethod
    def create(todo_name):
        try:
            todo = Todo(todo_name=todo_name)
            todo_obj = todo.save()
        except IntegrityError:
            return None
        return todo_obj