"""
Configuration class
"""

class Config():
    # TODO
    APP_NAME = 'Replace with application name'

    # Enable debug mode
    DEBUG = True
    
    # TODO
    # Setup database URL and credentials
    APP_DB = {
        'host': 'localhost',
        'db': 'bottle_collector_final',
        'user': 'root',
        'password': '',
        'port': 3306
    }


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'.format(
        APP_DB['user'], APP_DB['password'], APP_DB['host'], APP_DB['db'])

    # Setup CORS
    ALLOWED_HEADERS = ['Access-Token', 'Content-Type', 'referrer', 'Authorization', 'Cache-Control', 'X-Requested-With']
    ALLOWED_ORIGINS = '*'
    ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']

    # TODO
    # This is where frontend should go, create a route for all UI files
    # Setup template folder for webpages
    TEMPLATE_FOLDER = '/replace/template/folder/here/'
