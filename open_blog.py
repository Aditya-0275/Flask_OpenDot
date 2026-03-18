from flask import Flask

app = Flask(__name__)

print("Hello, World!")

@app.route("/")
def home():
	return "<h1>Home Page</h1>", 200

if __name__ == '__main__':
	app.run(debug=true)