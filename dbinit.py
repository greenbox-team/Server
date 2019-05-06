from app import db, create_app
#from sqlalchemy_utils import create_database, database_exists
import os

#url = 'mysql+pymysql://root:password@localhost/GBA'
#if not database_exists(url):
#    create_database(url)
db.create_all(app=create_app(os.getenv('FLASK_CONFIG') or 'default'))
