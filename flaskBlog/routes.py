from flask import render_template, url_for, flash, redirect
from flaskBlog.forms import RegistrationForm, LoginForm
from flaskBlog.models import User, Post
from flaskBlog import app

posts = [
    {
        'author': 'Ranjith Reddy Gaddam',
        'title': 'First Post',
        'content': 'First Post content',
        'date': '05 Feb, 2024'
    },
    {
        'author': 'John Cena',
        'title': 'Second Post',
        'content': 'Second Post content',
        'date': '05 Feb, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "title")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = "register", form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'grreddy2726@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful login. Please check your password', 'danger')
    return render_template('login.html', title = "login", form = form)
