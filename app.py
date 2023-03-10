from flask import Flask, request, jsonify
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

#método post hasta acá
#método get desde acá

@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@app.route("/pokemon/list", methods=["GET"])
def get_pokemon():
    pokemons = Pokemon.query.all()
    result = []
    for pokemon in pokemons:
        result.append(pokemon.serialize())
    return jsonify(result)

@app.route("/ability/list", methods=["GET"])
def get_ability():
    abilitys = Ability.query.all()
    result = []
    for ability in abilitys:
        result.append(ability.serialize())
    return jsonify(result)

@app.route("/type/list", methods=["GET"])
def get_type():
    types = Type.query.all()
    result = []
    for type in types:
        result.append(type.serialize())
    return jsonify(result)

@app.route("/feature/list", methods=["GET"])
def get_feature():
    features = Feature.query.all()
    result = []
    for feature in features:
        result.append(feature.serialize())
    return jsonify(result)

@app.route("/stat/list", methods=["GET"])
def get_stat():
    stats = Stat.query.all()
    result = []
    for stat in stats:
        result.append(stat.serialize())
    return jsonify(result)

#método get hasta acá
#método put, delete desde acá

@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            user.name = request.json.get("name")
            user.last_name = request.json.get("last_name")
            user.password = request.json.get("password")
            user.email = request.json.get("email")
        
            db.session.commit()
        
            return jsonify("Usuario actualizado"), 200
    
    return jsonify("Usuario no encontrado"), 404

@app.route("/pokemon/<int:id>", methods=["PUT", "DELETE"])
def update_pokemon(id):
    pokemon = Pokemon.query.get(id)
    if pokemon is not None:
        if request.method == "DELETE":
            db.session.delete(pokemon)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            pokemon.name = request.json.get("name")
       
            db.session.commit()
        
            return jsonify("Pokemon actualizado"), 200
    
    return jsonify("Pokemon no encontrado"), 404

@app.route("/ability/<int:id>", methods=["PUT", "DELETE"])
def update_ability(id):
    ability = Ability.query.get(id)
    if ability is not None:
        if request.method == "DELETE":
            db.session.delete(ability)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            ability.ability = request.json.get("ability")
       
            db.session.commit()
        
            return jsonify("Ability actualizado"), 200
    
    return jsonify("Ability no encontrado"), 404

@app.route("/type/<int:id>", methods=["PUT", "DELETE"])
def update_type(id):
    type = Type.query.get(id)
    if type is not None:
        if request.method == "DELETE":
            db.session.delete(type)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            type.type = request.json.get("type")
       
            db.session.commit()
        
            return jsonify("Type actualizado"), 200
    
    return jsonify("Type no encontrado"), 404

@app.route("/feature/<int:id>", methods=["PUT", "DELETE"])
def update_feature(id):
    feature = Feature.query.get(id)
    if feature is not None:
        if request.method == "DELETE":
            db.session.delete(feature)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            feature.height = request.json.get("height")
            feature.weight = request.json.get("weight")
       
            db.session.commit()
        
            return jsonify("Feature actualizado"), 200
    
    return jsonify("Feature no encontrado"), 404

@app.route("/stat/<int:id>", methods=["PUT", "DELETE"])
def update_stat(id):
    stat = Stat.query.get(id)
    if stat is not None:
        if request.method == "DELETE":
            db.session.delete(stat)
            db.session.commit()
            
            return jsonify("Eliminado"), 204
        else:
            stat.hp = request.json.get("hp")
            stat.attack = request.json.get("attack")
            stat.defense = request.json.get("defense")
            stat.special_attack = request.json.get("special_attack")
            stat.special_defense = request.json.get("special_defense")
            stat.speed = request.json.get("speed")
       
            db.session.commit()
        
            return jsonify("Stat actualizado"), 200
    
    return jsonify("Stat no encontrado"), 404

#método put, delete hasta acá



with app.app_context():
    db.create_all()



app.run(host="localhost", port="8080")