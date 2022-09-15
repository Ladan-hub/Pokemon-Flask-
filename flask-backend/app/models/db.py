from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from sqlalchemy.sql import func
# from datetime import datetime




types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]



db = SQLAlchemy()


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Columns(db.Integer, primary_key=True, nullable=False)
    number = db.Columns(db.Integer, nullable=False, unique=True)
    attack = db.Columns(db.Integer,nullable=False )
    defense = db.Columns(db.Integer, nullable=False)
    image_url = db.Columns(db.String(255), nullable=False)
    name = db.Columns(db.String(255), nullable=False, unique=True)
    type = db.Columns(db.Enum(types), nullable=False )
    moves = db.Columns(db.String(255), nullable=False)
    encounter_rate = db.Columns(db.Float(3, 2), nullable=False, default=1.00)
    catch_rate = db.Columns(db.Float(3, 2), nullable=False, default=1.00)
    captured = db.Columns(db.Boolean, nullable=False, default=False)
    # createdAt = db.Columns(DateTime(timezone=True), server_default=func.now())
    # updatedAt = db.Columns(DateTime(timezone=True), onupdate=func.now())
    created_at = db.Columns(db.DateTime, nullable=False)
    updated_at = db.Columns(db.DateTime, nullable=False)
    #Relationshipd
    pokemon_items = db.relationship("Item", back_populates = "pokemon_owner" cascade="all,delete")
    
    # def to_dict(self):
    #     return {
    #         "id": self.id
    #         "number": self.number
    #         "attack": self.attack
    #         "defense": self.defense
    #         "image_url": self.image_url
    #         "name":self.name
    #         "type": self.type
    #         "moves": self.moves
    #         "encounter_rate": self.encounter_rate
    #         "catch_rate": self.catch_rate
    #         "captured": self.captured
    #         "created_at": self.created_at
    #         "updated_at": self.updated_at
    #         "pokemonItems": [item.to_dict_no_pokemon() for item in self.pokemon_items]
    #     }

    # def to_dict_no_pokemonItems(self):
    #     return {
    #         "id": self.id
    #         "number": self.number
    #         "attack": self.attack
    #         "defense": self.defense
    #         "image_url": self.image_url
    #         "name":self.name
    #         "type": self.type
    #         "moves": self.moves
    #         "encounter_rate": self.encounter_rate
    #         "catch_rate": self.catch_rate
    #         "captured": self.captured
    #         "created_at": self.created_at
    #         "updated_at": self.updated_at
    #     }


class Item(db.Model):
    __tablename__ = "items"
    id = db.Columns(db.Integer, primary_key=True, nullable=False)
    happiness = db.Columns(db.Integer, nullable=False)
    image_url = db.Columns(db.String(255), nullable=False)
    name = db.Columns(db.String(255), nullable=False)
    price = db.Columns(db.Integer, nullable=False)
    pokemon_id = db.Columns(db.Integer, db.ForeignKey("pokemon.id"))
    created_at = db.Columns(db.DateTime, nullable=False)
    updated_at = db.Columns(db.DateTime, nullable=False)

    pokemon_owner = db.relationship("Pokemon", back_populates="pokemon_items", cascade="all,delete")

    # def to_dict(self):
    #     return {
    #         "id"= self.id,
    #         "happiness": self.happiness
    #         "image_url": self.image_url
    #         "name": self.name
    #         "price": self.price
    #         "pokemon_id": self.pokemon_id,
    #         "created_at": self.created_at,
    #         "updated_at": self.updated_at
    #         "pokemon_owner": [pokemon.to_dict_no_pokemonItems() for pokemon in self.pokemon_owner]
    #     }


    # def to_dict_no_pokemon(self):
    #     return {
    #        "id"= self.id,
    #         "happiness": self.happiness
    #         "image_url": self.image_url
    #         "name": self.name
    #         "price": self.price
    #         "pokemon_id": self.pokemon_id,
    #         "created_at": self.created_at,
    #         "updated_at": self.updated_at
    #     }




    



