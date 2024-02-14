from flask import Flask,render_template, request

app= Flask(__name__)

@app.route("/")
def render_form():
    return render_template("index.html")


@app.route('/result/', methods=["POST"])
def render_results():
    print("Got post info")
    print(request.form)
    print(request.form.getlist('email_agreement'))
    return render_template("result.html",result=request.form)

if __name__ == "__main__":
    app.run(debug=True)