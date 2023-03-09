from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    favorite = db.relationship('favorite')
    
class Favorite(db.Model):
    __tablename__='favorite'
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon'))
    name = db.Column(db.String(50), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Pokemon(db.Model):
    __tablename__='pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ability = db.relationship('ability')
    type = db.relationship('type')
    
class Feature(db.Model):
    __tablename__='feature'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pokemon = db.relationship('pokemon')

class Ability(db.Model):
    __tablename__='ability'
    id = db.Column(db.Integer, primary_key=True)
    ability = db.Column(db.String(50), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    
class stat(db.Model):
    __tablename__='stat'
    id = db.Column(db.Integer, primary_key=True)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pokemon = db.relationship('pokemon')
    
class Type(db.Model):
    __tablename__='type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))