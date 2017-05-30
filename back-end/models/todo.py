from datetime import datetime
from . import db
from .abc import BaseModel

class Todo(db.Model, BaseModel):

    __tablename__ = 'todo'

    todo_name = db.Column(db.String(300), primary_key=True)
    is_complete = db.Column(db.Boolean(), default=True, unique=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow())

    def __init__(self, todo_name):
        self.todo_name = todo_name
