from flask import Flask,render_template, request, session, redirect
import random
from time import gmtime, strftime

app= Flask(__name__)

app.secret_key = "123456789"



@app.route("/")
def render_main_page():
    if "gold" not in session:
        session['gold']= 0
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
## Best practices: Do Not return html tags ##
## returning html tag with a parameter rather than a session would result in a better performance
def process_money():
    locations = {"farm": random.randint(10,20),"house":random.randint(2,5), "cave":random.randint(5,10), "casino":random.randint(-50,50)}
    activity = {}
    session['gold'] += locations[request.form['location']]
    if locations[request.form['location']] > 0:
        activity["class"] = "text-success"
        activity["content"] = f"Earned {locations[request.form['location']]} golds from  the {request.form['location']}: {strftime('%d %b %Y %H:%M:%S', gmtime())}"
        # f"<h6 class='text-success'>Earned {locations[request.form['location']]} golds from  the {request.form['location']}: {strftime('%d %b %Y %H:%M:%S', gmtime())} </h6>"
    else:
        activity["class"] = "text-danger"
        activity["content"] = f"Entered a Casino and lost {locations[request.form['location']]} golds....Ouch.: : {strftime('%d %b %Y %H:%M:%S', gmtime())}"
        # f"<h6 class='text-danger'>Entered a Casino and lost {locations[request.form['location']]} golds....Ouch.: : {strftime('%d %b %Y %H:%M:%S', gmtime())} </h6>"
    if "activities" not in session:
        session["activities"] = []
        session["activities"].append(activity)
    else:
        session["activities"].append(activity)

    print(session["activities"])
    return redirect("/")

@app.route("/reset_game")
def reset_game():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)