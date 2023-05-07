import bottle
from bottle import auth_basic, route, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from model import Base
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

engine = engine = create_engine(
    '{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
        **settings.COCKROACH
    ),
    echo=settings.SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)

def setup_routes():
     bottle.route('/dog/<dog_id>', ['GET', 'DELETE'], crud)
     bottle.route('/dog/<dog_breed>/<dog_color>', ['PUT'], insert_entry)
     bottle.route('/dog/<dog_id>/<dog_breed>/<dog_color>', ['POST'], update_entry)

def is_authenticated_user(user, password):
    # You write this function. It must return
    # True if user/password is authenticated, or False to deny access.
	if user == 'user' and password == 'pass':
		return True
	return False

def get_strategy(db):
     return Raw(db)

@route('/')
def hello(db):
	return {"hello": "world"}

@route('/dog')
@auth_basic(is_authenticated_user)
def get_all(db):
    strategy = get_strategy(db)
    return strategy.all()

@route('/dog/<dog_id>')
@auth_basic(is_authenticated_user)
def crud(db, dog_id):
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(dog_id)
    
    return strategy.delete_by(dog_id)

@route('/dog/<dog_breed>/<dog_color>')
@auth_basic(is_authenticated_user)
def insert_entry(db, dog_breed, dog_color):
    strategy = get_strategy(db)
    return strategy.insert_entry(dog_breed, dog_color)

@route('/dog/<dog_id>/<dog_breed>/<dog_color>')
@auth_basic(is_authenticated_user)
def update_entry(db, dog_id, dog_breed, dog_color):
    strategy = get_strategy(db)
    return strategy.update_entry(dog_id, dog_breed, dog_color)

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))

setup_routes()

run(host='0.0.0.0', port=8000,debug=True)