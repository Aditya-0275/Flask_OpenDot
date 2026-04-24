from flask import render_template, url_for, flash, redirect
from open_blog.forms import RegistrationForm, LoginForm
from open_blog.models import User, Post
from open_blog import app

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

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account created successfully, Welcome {form.username.data}!", "success")
		return redirect(url_for('home'))
	return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template("login.html", title="Login", form=form)