import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-do App")
st.subheader("")
st.write("")

todos = functions.read_todos()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()   # OR .experimental_rerun()

st.text("")
st.text_input(label="", placeholder="Enter a to-do",
              on_change=add_todo, key="new_todo")