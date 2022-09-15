from flask import Blueprint, render_template

pokemon_router = Blueprint("pokemon", __name__, url_prefix= "/pokemon")
@pokemon_router.route("/")
def index():
    return "<h1>Testing Pokemon</h1>"


