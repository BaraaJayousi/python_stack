from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkboard_constant():
    return render_template("index.html", x=8, y=8,col1 ="red",col2="black")

@app.route("/<int:x>/")
def checkboard_x_variable(x):
    return render_template("index.html",x = int(x), y = 8, col1="red", col2="black")

@app.route("/<int:x>/<int:y>/")
def checkboard_x_y_variable(x,y):
    return render_template("index.html", x =int(x), y=int(y), col1="red", col2="black")

@app.route("/<int:x>/<int:y>/<col1>/<col2>/")
def checkboard_x_y_color_variable(x,y,col1,col2):
    return render_template("index.html",x =int(x), y=int(y), col1=col1, col2=col2)

if __name__ == "__main__":
    app.run(debug=True)