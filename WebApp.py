import streamlit as st
from streamlit import checkbox

import function13

todos = function13.get_todos()


def add_todo():
    tod = st.session_state["new_todo"] + "\n"
    todos.append(tod)
    function13.store_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function13.store_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")


