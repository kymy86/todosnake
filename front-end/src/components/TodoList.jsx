import React, {Component} from 'react'
import Todo from './Todo'


class TodoList extends Component {

  componentDidMount(){
    this.props.fetchTodos();
  }

  render() {
    console.log(this.props)
      return  <ul>
        {this.props.todos.map(todo =>
          <Todo
            key={todo.todo_name}
            {...todo}
            onClick={() => this.propos.onTodoClick(todo.todo_name)}
          />
        )}
      </ul>
  }
}

export default TodoList