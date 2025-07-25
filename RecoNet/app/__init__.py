from flask import Flask
from .models import db
from .auth.routes import auth_bp
from .admin.routes import admin_bp
from .user.routes import user_bp
from .main.routes import main_bp
from .services.whois.routes import whois_bp
from .services.geopy.routes import geopy_bp
from .services.dnsres.routes import dns_bp
from .services.ipwhois.routes import ipwhois_bp 

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(whois_bp)
    app.register_blueprint(geopy_bp)
    app.register_blueprint(dns_bp)
    app.register_blueprint(ipwhois_bp)
    
    return app