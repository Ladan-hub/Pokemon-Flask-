from flask import Blueprint, render_template

items_router = Blueprint("items", __name__, url_prefix= "/items")

@items_router.route("/")
def items():
    return "<h1>Testing Items</h1>"
