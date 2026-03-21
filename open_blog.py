from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
	{
		"author":"Aditya Sharma",
		"title":"The First Dot",
		"date_posted":"March 21, 2026",
		"content":"This marks the beginning of this project."
	},
	{
		"author":"Mimansha Agarwal",
		"title":"The Second Dot",
		"date_posted":"March 21, 2026",
		"content":"This is a dummy content for testing purposes."
	}
]

@app.route("/")
def home():
	return render_template("home.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title="About")

if __name__ == '__main__':
	app.run(debug=True)
