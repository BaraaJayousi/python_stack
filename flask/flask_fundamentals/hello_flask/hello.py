from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return f"the page is not found, call me to give you hints"

@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"

@app.route('/hello/<name>/')
def hello(name):
    return f"hello, {name}"


@app.route('/lists/')
def render_lists():
    #hard coded data, instead of retriving from a database
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 22},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27},
    ]

    return render_template("lists.html", random_numbers=[3,1,5], students = student_info)


if __name__  == '__main__':
    app.run(debug=True)