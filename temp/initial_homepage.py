from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index() :
	return "<h1>Hello Flask</h1>"

@app.route("/test")
def test() :
	return "<h1>Hello Test Page</h1>"


app.run()