"""
Configuration class
"""
class Config():
    # TODO
    APP_NAME = 'plastic bottle collector'

    # Enable debug mode
    DEBUG = True
    
    # TODO
    # Setup database URL and credentials
    APP_DB = {
        'host': 'localhost',
        'db': 'bottle_collector',
        'user': 'root',
        'password': 'jabelojabelo101',
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
    from flask import Blueprint
    from flask import render_template
    

    mod_frontend = Blueprint('frontend', __name__)


    @mod_frontend.route('/page1', methods=['GET'])
    def scan_page():
        return render_template('pages/page1.html')

    @mod_frontend.route('/page2', methods=['GET'])
    def profile_page():
        return render_template('pages/page2.html')

    @mod_frontend.route('/page4', methods=['GET'])
    def camera_page():
        return render_template('pages/page4.html')

    @mod_frontend.route('/page5', methods=['GET'])
    def thankyou_page():
        return render_template('pages/page5.html')


    # Setup template folder for webpages
    TEMPLATE_FOLDER = "C:/Users/cecilia/Documents/programming_practice_l/templates"
