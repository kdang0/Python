from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return f"Hi, {name}"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    try:
        int(num)
    except ValueError:
        return "<h1>NOT A VALID INT<h1>"
    return int(num)*("<h1>" + word + "</h1>")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Sorry! No response. Try again.</h1>"
app.run(debug=True)