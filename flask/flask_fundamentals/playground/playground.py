from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play/")
def playground_1():
    return render_template("index.html.jinja", loops = 3, color="blue", title="Playground 1")

@app.route("/play/<int:count>/")
def playground_2(count):
    return render_template("index.html.jinja", loops = int(count), color="blue", title="Playground 2")

@app.route("/play/<int:count>/<color>/")
def playground_3(count,color):
    return render_template("index.html.jinja", loops = int(count), color=color, title="Playground 3")

if __name__ == "__main__":
    app.run(debug=True)

