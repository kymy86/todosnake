let nextTodoId = 0


export function fetchTodos(){
  return (dispatch) => {
    dispatch({
      type: 'FETCH_TODOS_REQUEST'
    });
    return fetch('http://localhost:8000/todo/')
      .then(response => response.json().then(body => ({ response, body })))
      .then(({ response, body }) => {
        if (!response.ok) {
          dispatch({
            type: 'FETCH_TODOS_FAILURE',
            error: body.error
          });
        } else {
          dispatch({
            type: 'FETCH_TODOS_SUCCESS',
            todos: body.todos
          });
        }
      });
  }
}

export const addTodo = (text) => ({
  type: 'ADD_TODO',
  id: nextTodoId++,
  text
})

export const setVisibilityFilter = (filter) => ({
  type: 'SET_VISIBILITY_FILTER',
  filter
})

export const toggleTodo = (id) => ({
  type: 'TOGGLE_TODO',
  id
})