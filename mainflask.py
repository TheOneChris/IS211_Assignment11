from flask import Flask, render_template, request, redirect
app = Flask(__name__)

todo_list = []

@app.route('/')
def hello_world():
    global todo_list
    name = "Chris"
    day = "Friday"

    return render_template('todo_list.html', name=name, day=day, list=todo_list)

@app.route('/submit', methods = ['POST'])
def submit():
    global todo_list
    email = request.form['email']

    task = request.form['task']
    priority = request.form["Priority"]
    to_do_item = {"email": email, "task": task, "level": priority}

    if "@" not in email:
        print("email is invalid")
        return redirect('/')

    if priority != "High" and priority != "Medium" and priority != "Low":
        print("priority is invalid")
        return redirect('/')

    todo_list.append(to_do_item)


    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    global todo_list
    todo_list = []

    return redirect('/')


if __name__ == "__main__":
    app.run()
