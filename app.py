from flask import Flask
from models.models import db, User
from flask_login import LoginManager
from routes.web import web_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.secret_key = "vlan-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vlan.db"
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(web_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)