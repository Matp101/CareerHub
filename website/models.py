'''
models.py
Creates the database models in SQLAlchemy
'''
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin): # Every successful registered user is saved as a User in the User table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))

class JobCategory(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(128))

class JobListing(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    company = db.Column(db.String(128))
    salary = db.Column(db.Integer)
    location = db.Column(db.String(128))
    type = db.Column(db.String(128))
    description = db.Column(db.String(32768))
    email = db.Column(db.String(128))
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())

    # Foreign key reference to JobCategory model's primary key
    category_id = db.Column(db.Integer, db.ForeignKey('job_category.category_id'), nullable=False)

    # Define the relationship with JobCategory model
    category = db.relationship('JobCategory', backref=db.backref('job_listings', lazy=True))
