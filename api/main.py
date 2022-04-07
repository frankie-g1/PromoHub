
# To run the app run
# $env:FLASK_APP = "main"
# python3 -m flask run
# in ^ powershell terminal

from pydoc import render_doc
import youtubeAPI
import subprocess
from flask import Flask, render_template
from flask_restful import Api
import flask_mysqldb as mysql
from promoHubController import PromoHubController

# defines app with Flask & allows for requests
app = Flask(__name__)
api = Api(app)



@app.route('/')
def home():
    return render_template('draft.html')



api.add_resource(PromoHubController, '/getData')


if __name__ == '__main__':
    # starts youtube api data collection
    app.run(port=5000, debug=True)
    subprocess.call('.\youtubeAPI.py', shell=True)
