import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a new task
def add_task(task):
    if task and task not in [t["task"] for t in st.session_state.tasks]:
        st.session_state.tasks.append({"task": task, "completed": False})
    elif task:
        st.warning(f"Task '{task}' already exists.")
    else:
        st.warning("Task field cannot be empty.")

# Function to remove a task
def remove_task(task):
    st.session_state.tasks.remove(task)

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Add Task", "Completed Tasks", "Incompleted Tasks"])

if page == "Add Task":
    st.header("Add Tasks")
    new_task = st.text_input("Enter a new task")
    if st.button("Add Task"):
        add_task(new_task)

    # Display all tasks at the bottom
    st.subheader("All Tasks")
    if not st.session_state.tasks:
        st.info("No tasks available.")
    for task in st.session_state.tasks:
        col1, col2 = st.columns([5, 1])
        with col1:
            task["completed"] = st.checkbox(task["task"], task["completed"], key=task["task"])
        with col2:
            if st.button("Delete", key=f"delete_{task['task']}"):
                remove_task(task)
                st.rerun()

elif page == "Completed Tasks":
    st.header("Completed Tasks")
    completed_tasks = [task for task in st.session_state.tasks if task["completed"]]
    if not completed_tasks:
        st.info("No completed tasks available.")
    for task in completed_tasks:
        col1, col2 = st.columns([5, 1])
        with col1:
            if st.checkbox(task["task"], task["completed"], key=task["task"]):
                task["completed"] = True
            else:
                task["completed"] = False
                st.rerun()
        with col2:
            if st.button("Delete", key=f"delete_{task['task']}"):
                remove_task(task)
                st.rerun()

elif page == "Incompleted Tasks":
    st.header("Incompleted Tasks")
    incompleted_tasks = [task for task in st.session_state.tasks if not task["completed"]]
    if not incompleted_tasks:
        st.info("No incompleted tasks available.")
    for task in incompleted_tasks:
        col1, col2 = st.columns([5, 1])
        with col1:
            if st.checkbox(task["task"], task["completed"], key=task["task"]):
                task["completed"] = True
                st.rerun()
        with col2:
            if st.button("Delete", key=f"delete_{task['task']}"):
                remove_task(task)
                st.rerun()
