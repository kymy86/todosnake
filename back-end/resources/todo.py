from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify
from flask import request

from repositories import TodoRepo
#from util import parse_params

class TodoResource(Resource):

    @staticmethod
    def get(todo_name):

        todo = TodoRepo.get(todo_name=todo_name)
        return jsonify({'todo':{} if todo is None else todo.json})

    @staticmethod
    def post():
        req_data = request.get_json()

        todo = TodoRepo.create(
            todo_name=req_data['todo_name']
        )
        if todo is None:
            response = jsonify({'error':"todo already exists"})
            response.status_code = 400
            return response
        else:
            response = jsonify({'todo':todo.json})
            response.status_code = 201
            return response

    @staticmethod
    def put():
        req_data = request.get_json()
        repository = TodoRepo()
        todo = repository.update(
            todo_name=req_data['todo_name'],
            is_complete=req_data['is_complete']
        )
        if todo is None:
            response = jsonify({'error':"todo doesn't exist"})
            response.status_code = 400
            return response
        else:
            response = jsonify({'todo':todo.json})
            response.status_code = 200
            return response
