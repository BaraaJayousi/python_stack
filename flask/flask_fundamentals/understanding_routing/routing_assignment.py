from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def error_page(e):
    print(e)
    return "Sorry! No Response. Try again."

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def say_dojo():
    return "Dojo"

@app.route("/say/<word>")
def say_word(word):
    return f"Hi, {word}!"

@app.route("/repeat/<int:count>/<word>")
def repeate_word(count, word):
    return word * int(count)

if __name__ == "__main__":
    app.run(debug=True)