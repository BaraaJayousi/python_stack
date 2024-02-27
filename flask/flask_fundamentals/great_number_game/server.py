from flask import Flask, render_template,request, session, redirect
import random

app = Flask(__name__)

app.secret_key = '123456789'
# random_number = random.randint(1,100)

@app.route('/')
def start_game():
    # session['random_num'] = random_number
    if "random_num" not in session:
        return redirect('/reset/')
    # if "answer" in session:
    #     print(session['answer'])
    return render_template("index.html")

@app.route("/check_guess/", methods=["POST"])
def check_guess():
    guess= int(request.form['guess'])
    if 'guess_count' not in session:
        session['guess_count'] = 1
    else:
        session['guess_count'] += 1

    if guess > session['random_num']:
        session['answer'] = 'high'
    elif guess < session['random_num']:
        session['answer'] = 'low'
    else:
        session['answer'] = 'correct'
    return redirect('/')

@app.route("/reset/", methods=["GET"])
def reset_game():
    session.clear()
    random_number = random.randint(1,100)
    session['random_num'] = random_number
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)