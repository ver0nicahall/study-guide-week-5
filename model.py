"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    brand_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String)
    discontinued = db.Column(db.Integer)

    models = db.relationship('Model', back_populates='brand')

    def __repr__(self):
        return f"<Brand id={self.brand_id} name={self.name}>"


class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    brand_id = db.Column(db.String, db.ForeignKey('brands.brand_id'))

    brand = db.relationship('Brand', back_populates='models')

    def __repr__(self):
        return f"<Model model_id={self.model_id} name={self.name}>"


# End Part 1
##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cars'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    init_app()
