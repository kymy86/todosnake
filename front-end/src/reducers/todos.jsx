
const todo = (state, action) => {
  switch (action.type) {
    case 'ADD_TODO':
      return {
        id: action.id,
        text: action.text,
        completed: false
      }
    case 'TOGGLE_TODO':
      if (state.id !== action.id) {
        return state
      }

      return {
        state,
        completed: !state.completed,
        text: state.text,
        id: state.id
      }
    default:
      return state
  }
}

const INITIAL_STATE = {
  items: [],
  isFetching: false,
  error: undefined
};

const todos = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case 'FETCH_TODO_REQUEST':
      return Object.assign({}, state, {
          isFetching: true
        });
    case 'FETCH_TODOS_SUCCESS':
      console.log(action)
      return Object.assign({}, state, {
        isFetching: false,
        todos: action.todos
      });
    case 'FETCH_TODOS_FAILURE':
      return Object.assign({}, state, {
        isFetching: false,
        error: action.error
      });
    case 'ADD_TODO':
      return [
        ...state,
        {
          id: action.id,
          text: action.text,
          completed: false
        }
      ]
    case 'TOGGLE_TODO':
       return state.map(t =>
        todo(t, action)
      )
    default:
      return state
  }
}

export default todos