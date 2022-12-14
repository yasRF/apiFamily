from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
           
        }

class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    years = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'<Family {self.name}>'

    def serialize(self):
        return {
    "id": self.id,
    "name": self.name,
    "lastname": self.lastname,
    "years": self.years
}
        
        
        