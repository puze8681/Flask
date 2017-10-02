from flask import Flask
app = Flask(__name__)

@app.route("/")

@app.route("/")
def hello():
	return "<h1>Hello World!</h>"
if __name__ == "__main__":
	app.run()

