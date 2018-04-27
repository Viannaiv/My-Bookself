from flask import Flask, flash, redirect
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookshelf.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)



from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app) #Here was .init_app

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Log in to use this function")
    return redirect('/auth/login')

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from application import views, testValues

from application.works import models
from application.works import views

from application.auth import models
from application.auth import views

from application.editions import models
from application.editions import views

from application.formats import models
from application.formats import views




from application.auth.models import User
from application.works.models import Work

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
    works = Work.query.all()
    if not works:
        testValues.create_test_data()     
except:
    pass
