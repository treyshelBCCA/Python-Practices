from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for the to-do list
todo_list = []

@app.route('/')
def home():
    # Render the index.html template and pass the todo_list to it
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add_todo():
    # Get the task from the form and add it to the todo_list
    task = request.form.get('task')
    # Add the task to the todo_list
    # TODO: Implement this function
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_todo(task_id):
    # Delete the task from the todo_list based on its index
    # TODO: Implement this function
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
