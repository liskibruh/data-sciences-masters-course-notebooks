from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    a  = 5+2
    return f'this is my function to run app {a}'

@app.route("/test2")
def test2():
    data=request.args.get('x')
    return f'this is the data input from my url {data}'

if __name__=="__main__":
    app.run(host="0.0.0.0")
