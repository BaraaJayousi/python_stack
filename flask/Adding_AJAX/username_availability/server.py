from flask import Flask, redirect,render_template, session,request
import time

app = Flask(__name__)

app.secret_key = "1234567"

users_list = []

@app.route("/")
def render_registration_form():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register_user():
    user_info={"username":"","email":"","password":""}
    for key in request.form.keys():
        if key in user_info:
            user_info[key] = request.form[key]
    users_list.append(user_info)
    if "users" not in session:
        print("initation users session")
        session["users"] = []
    session["users"] = users_list
    print(session["users"])
    return redirect("/")

@app.route("/check-data", methods=["POST"])
def check_registration_data():
    username_available = True
    email_available = True
    password_match = True
    # print(session)
    print(request.form)
    for user in session["users"]:
        if request.form['username'] == user['username'] or request.form['username'] == '':
            username_available = False
        if request.form['email'] == user['email'] or request.form['email'] == '':
            email_available = False
        if request.form['password'] != request.form['confirm_pw'] or request.form['password'] == '':
            password_match = False
    time.sleep(2)
    return render_template("partials/index.html", username_available = username_available, email_available = email_available, password_match = password_match)

if __name__ == "__main__":
    app.run(debug=True)