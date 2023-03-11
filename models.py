from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    favorite = db.relationship("Favorite")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }


class Pokemon(db.Model):
    __tablename__='pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ability = db.relationship("Ability")
    type = db.relationship("Type")
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Ability(db.Model):
    __tablename__='ability'
    id = db.Column(db.Integer, primary_key=True)
    ability = db.Column(db.String(50), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "ability": self.ability,
            "pokemon_id": self.pokemon_id
        }

class Type(db.Model):
    __tablename__='type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "pokemon_id": self.pokemon_id
        }
    
class Feature(db.Model):
    __tablename__='feature'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "weight": self.weight,
            "pokemon_id": self.pokemon_id
        }

class Stat(db.Model):
    __tablename__='stat'
    id = db.Column(db.Integer, primary_key=True)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "special_attack": self.special_attack,
            "special_defense": self.special_defense,
            "speed": self.speed,
            "pokemon_id": self.pokemon_id
        }

class Favorite(db.Model):
    __tablename__='favorite'
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    name = db.Column(db.String(50), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "pokemon_id": self.pokemon_id,
            "name": self.name,
            "id_user": self.id_user            
        }
    