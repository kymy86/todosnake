import unittest
import json
import config

from app import app
from models.abc import db
from models import Todo
from repositories import TodoRepo

class TestTodo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLLITE
        cls.client = app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """
        Test get request
        """
        TodoRepo.create("test todo")
        response = self.client.get('/todo/test todo')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json['todo']['todo_name'], 'test todo')

    def test_create(self):
        """
        Test post request
        """
        response = self.client.post(
            '/todo/',
            content_type='application/json',
            data=json.dumps({
                'todo_name':'test todo 2'
            }))
        self.assertEqual(response.status_code, 201)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json['todo']['todo_name'], 'test todo 2')
        self.assertEqual(Todo.query.count(), 1)

    def test_create_exists(self):
        """
        Test create if todo already exists
        """
        #create
        TodoRepo.create(todo_name='todo 1')
        #test
        response = self.client.post(
            '/todo/',
            content_type='application/json',
            data=json.dumps({
                'todo_name':'todo 1'
            }))
        self.assertEqual(response.status_code, 400)

    def test_update(self):
        """
        Test put request
        """
        TodoRepo.create(todo_name='todo 1')
        response = self.client.put(
            '/todo/',
            content_type='application/json',
            data=json.dumps({
                'todo_name':'todo 1',
                'is_complete': True
            })
        )
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json['todo']['is_complete'], True)

    def test_update_not_exists(self):
        """
        Test put request if todo not
        exists
        """
        TodoRepo.create(todo_name='todo 1')
        response = self.client.put(
            '/todo/',
            content_type='application/json',
            data=json.dumps({
                'todo_name':'todo 2',
                'is_complete': True
            })
        )
        self.assertEqual(response.status_code, 400)
    