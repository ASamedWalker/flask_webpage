from flask_webpage import app, db
from flask import render_template, redirect, url_for, flash, session, request
from flask_webpage.forms import RegistrationForm, LoginForm
from flask_webpage.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/account")
def account():
    return render_template("account.html", title="Account")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data))
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data} was successfully created!", category='success')
        return redirect(url_for("login"))
    return render_template("register.html", title="Sign Up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "samed@grassrootsdev.com" and form.password.data == '123456':
            flash(f"Login successful for {form.email.data}", category='success')
            return redirect(url_for("account"))
        else:
            flash(f"Login unsuccessful for {form.email.data}", category='danger')
    return render_template("login.html", title="Login", form=form)
