from flask import Flask
from flask_cors import CORS
from .database import db
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    CORS(app)  

    app.register_blueprint(main_bp)
    
    return app
