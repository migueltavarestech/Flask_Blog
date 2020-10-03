from flaskblog import db
from datetime import datetime

# Create SQLAlchemy User models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # One user can have multiple posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # How our object is printed out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Create SQLAlchemy Posts models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    #One post can only have one user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable='False')

    # How our object is printed out
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"