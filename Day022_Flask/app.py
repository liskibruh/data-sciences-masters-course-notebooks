from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Company Name: ABC Corporation</p><p>Location: India</p><p>Contact Detail: 999-999-9999</p>"

@app.route('/welcome')
def welcome():
    return "Welcome to ABC Corporation"

with app.test_request_context():
    print(url_for('welcome'))

if __name__=="__main__":
    app.run(host="0.0.0.0")