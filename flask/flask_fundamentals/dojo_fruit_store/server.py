from flask import Flask, render_template, request, redirect
from time import localtime, strftime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    current_time = strftime("%d %b %Y %I:%M:%S %p", localtime())
    order_qunatity = int(request.form['raspberry']) + int(request.form['strawberry']) + int(request.form['apple'])
    print(order_qunatity)
    print(request.form)
    print(current_time)
    return render_template("checkout.html",order=request.form, time=current_time, order_qty= order_qunatity)

@app.route('/fruits')         
def fruits():
    store_furits = [{'name':'Apple', 'price':'3', 'unit':'Kg'},
                    {'name':'Blackberry', 'price':'6', 'unit':'Kg'},
                    {'name':'Raspberry', 'price':'8', 'unit':'Kg'},
                    {'name':'Strawberry', 'price':'10', 'unit':'Kg'}
                    ]
    return render_template("fruits.html", fruits=store_furits)

if __name__=="__main__":   
    app.run(debug=True)    