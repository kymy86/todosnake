import { connect } from 'react-redux'
import { toggleTodo, fetchTodos } from '../actions/actions'
import TodoList from '../components/TodoList'

const getVisibleTodos = (todos, filter) => {
  switch (filter) {
    case 'SHOW_ALL':
      return todos
    case 'SHOW_COMPLETED':
      return todos.filter(t => t.is_complete)
    case 'SHOW_ACTIVE':
      return todos.filter(t => !t.is_complete)
    default:
      throw new Error('Unknown filter: ' + filter)
  }
}

const mapStateToProps = (state) => {
  return {
    todos: getVisibleTodos(state.todos, state.visibilityFilter)
  }
}

const mapDispatchToProps = (dispatch) => {
  /*return {
      onTodoClick: toggleTodo,
      fetchTodos: dispatch(fetchTodos())
  }*/
  return {
    // This function will be available in component as `this.props.fetchTodos`
    fetchTodos: function() {
      dispatch(fetchTodos());
    },
    onTodoClick: function() {
      toggleTodo
    }
  };
}

const VisibleTodoList = connect(
  mapStateToProps,
  mapDispatchToProps
)(TodoList)


export default VisibleTodoList