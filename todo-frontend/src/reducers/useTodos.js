import { globalReducer } from "react-hook-utils";
import { guid } from "../utils";
import {addTodos, deleteTodos, updateTodos} from "../apis/api_calls";


// can be chaged to interact with django backend
export const newTodo = label => ({
  done: false,
  id: guid(),
  label: (label || "").trim()
});

export const reducer = {
  // Delete a todo by id
  deleteTodo: (state, id) => {
      deleteTodos(id);
      return state.filter(i => i.id !== id)
  },

  // Create a new item
  addTodo: (state, label) => {
      let label_obj = newTodo(label);
      addTodos(label_obj);
      return [label_obj, ...state]
  },

  // Set the done state of an item
  setDone: (state, id, done) =>
  {
      return state.map(i =>
          {
              if (i.id === id) {
                  updateTodos(id, { ...i, done });
                  return { ...i, done };
              } else {
                  return i
              }
          }
      )
  },

  // Set the label of an item
  setLabel: (state, id, label) =>
    state.map(i =>
      i.id === id
        ? {
            ...i,
            label
          }
        : i
    ),

  // Toggle an item done
  toggleDone: (state, id) =>
    state.map(i =>
    {
        if (i.id === id) {
            let new_data = {
            ...i,
            done: !i.done
            };
            updateTodos(id, new_data);
            return new_data;
        } else {
            return i
        }
    }
    )
};

export default globalReducer(
  // Load todos from local storage
  JSON.parse(localStorage.getItem("todos") || "[]"),
  reducer,
  // On state change, persist to local storage
  todos => localStorage.setItem("todos", JSON.stringify(todos))
);
