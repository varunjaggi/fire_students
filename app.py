from flask import Flask,render_template,request

app=Flask(__name__)

# Basic Route
@app.route("/")
def index():
    return render_template('base.html')

if __name__=='__main__':
    app.run(debug=True)