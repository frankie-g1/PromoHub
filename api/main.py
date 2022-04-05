import youtubeAPI
import subprocess
from flask import Flask
from flask_restful import Api
import flask_mysqldb as mysql
from promoHubController import PromoHubController

# defines app with Flask & allows for requests
app = Flask(__name__)
api = Api(app)


api.add_resource(PromoHubController, '/')




if __name__ == '__main__':
    # starts youtube api data collection
    app.run(port=5000, debug=True)
    subprocess.call('.\youtubeAPI.py', shell=True)
