from flask import Flask,render_template,request

app=Flask(__name__)

# Basic Route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup_form")
def signup_form():
    return render_template('signup.html')

@app.route("/thanks")
def thankyou():
    first=request.args.get('first')
    last=request.args.get('last')
    age=request.args.get('age')
    return render_template("thankyou.html",first=first)

if __name__=='__main__':
    app.run(debug=True)
