from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# User Model 
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
