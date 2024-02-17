from flask import Flask,render_template, request, redirect, session
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


app.secret_key = os.getenv("SESSION_SECRET")

@app.route("/")
def show_visits_count():
    if "username" not in session:
        print("hi")
        return render_template("register.html")
    

    if "visit_count" in session:
        session['visit_count'] += session['increment_value']
    else:
        session['visit_count'] = 0
    return render_template("index.html")

@app.route("/register/", methods=['POST'])
def register_user():
    session['username'] = request.form['username']
    session['increment_value'] = int(request.form['increment'])
    return redirect('/')

@app.route('/destroy_session/')
def destroy_session():
    session.clear()
    return redirect("/")

@app.route("/double-visit/")
def double_visit():
    session['visit_count'] += 2 - session['increment_value']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)