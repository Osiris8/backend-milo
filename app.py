from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from extensions import db
from datetime import timedelta
load_dotenv()

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=int(os.getenv('JWT_EXPIRES_HOURS', 2)))

db.init_app(app)
jwt = JWTManager(app)


from routes.auth import auth_bp
from routes.mistralai import prompt_bp
from routes.groqai import prompt_groqai_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(prompt_bp, url_prefix='/api/mistral')
app.register_blueprint(prompt_groqai_bp, url_prefix='/api/groqai')

with app.app_context():
    db.create_all()


if __name__ == '__main__':
        app.run(debug=True)