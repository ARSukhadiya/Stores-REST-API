import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)                       # make a flask object
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
#                                                       DATABASE_URL - postgres_db_env_variable's_URL from Heroku

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)                              # assign a flask-object to restful parameter Api to perform on Resource
app.secret_key = 'jose'

# @app.before_first_request
# def create_tables():
#     db.create_all()

# initialize a JWT object-'jwt'
jwt = JWT(app, authenticate, identity)      # /auth - create a new end-point


# add resource to api to connect the logic  
api.add_resource(Store, '/store/<string:name>')      
api.add_resource(Item, '/item/<string:name>')   # item
api.add_resource(ItemList, '/items')            # items
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')     # signup


if __name__ == "__main__":                      # It's to prevent run method without app.py execution, i.e. by any import of any from app.py 
    
    from db import db                           # import here, because of "circular_import"
    db.init_app(app)

    app.run(port=5000, debug=True)              # debug is for better ERROR_MESSAGE from web page