from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# Dummy Post Data
posts = [
    {
        'author': 'Miguel Tavares',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '2nd October 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '1st October 2020'
    }
]

# Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


# About Page
@app.route("/about")
def about():
    return render_template('about.html', title='About')


# Register Page w/ GET and POST possibilities
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(("Account created {name}!".format(name={form.username.data})), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


# Login Page w/ GET and POST possibilities
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)