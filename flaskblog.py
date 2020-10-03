from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd8bc59a7ef0c8ae183ef4fd0bec66836'

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


# Use python script to open in localhost instead of opening through flask
if __name__ == '__main__':
    app.run(debug=True)