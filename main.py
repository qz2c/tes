from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return jsonify({"msg":"hello from glitch."})

if __name__ == "__main__":
	app.run()