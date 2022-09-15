
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .config import Config
from flask import Flask 
from .routes.pokemon import pokemon_router
from .routes.items import items_router
import os


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(pokemon_router)
app.register_blueprint(items_router)




# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
