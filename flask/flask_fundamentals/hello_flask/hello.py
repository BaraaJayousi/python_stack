from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return f"the page is not found, call me to give you hints"

@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"

@app.route('/hello/<name>')
def hello(name):
    return f"hello, {name}"

if __name__  == '__main__':
    app.run(debug=True)