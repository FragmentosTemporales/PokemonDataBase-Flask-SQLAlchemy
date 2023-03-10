from flask import Flask, request
from models import db, User, Pokemon, Ability, Type, Feature, Stat

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "Hello World"

#método POST desde aquí

@app.route("/users", methods=["POST"])
def create_user() :
    user = User()
    user.name = request.json.get("name")
    user.last_name = request.json.get("last_name")
    user.password = request.json.get("password")
    user.email = request.json.get("email")
    
    db.session.add(user)
    db.session.commit()
    
    return "User guardado"

@app.route("/pokemon", methods=["POST"])
def create_pokemon() :
    pokemon = Pokemon()
    pokemon.id = request.json.get("id")
    pokemon.name = request.json.get("name")
    
    db.session.add(pokemon)
    db.session.commit()
    
    return "Pokemon guardado"

@app.route("/ability", methods=["POST"])
def create_ability() :
    ability = Ability()
    ability.ability = request.json.get("ability")
    ability.pokemon_id = request.json.get("pokemon_id")
    
    db.session.add(ability)
    db.session.commit()
    
    return "Ability guardado"

@app.route("/type", methods=["POST"])
def create_type() :
    type = Type()
    type.type = request.json.get("type")
    type.pokemon_id = request.json.get("pokemon_id")
    
    db.session.add(type)
    db.session.commit()
    
    return "Ability guardado"

@app.route("/feature", methods=["POST"])
def create_feature() :
    feature = Feature()
    feature.height = request.json.get("height")
    feature.weight = request.json.get("weight")
    feature.pokemon_id = request.json.get("pokemon_id")
    
    db.session.add(feature)
    db.session.commit()
    
    return "Feature guardado"

@app.route("/stat", methods=["POST"])
def create_stat() :
    stat = Stat()
    stat.hp = request.json.get("hp")
    stat.attack = request.json.get("attack")
    stat.defense = request.json.get("defense")
    stat.special_attack = request.json.get("special_attack")
    stat.special_defense = request.json.get("special_defense")
    stat.speed = request.json.get("speed")
    stat.pokemon_id = request.json.get("pokemon_id")
    
    db.session.add(stat)
    db.session.commit()
    
    return "Stat guardado"

with app.app_context():
    db.create_all()

#método post hasta acá

app.run(host="localhost", port="8080")