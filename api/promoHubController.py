import MySQLdb as mysql
import pandas as pd
from flask_restful import Resource, request
from flask import jsonify

class PromoHubController(Resource):

    def get(self):
        
        db = mysql.connect(host="localhost", user="root", passwd="woodenHand12_(", db="promohub_schema")
        cur  = db.cursor()
        cur.execute("SELECT * FROM promohub")
        v = cur.fetchall()
        print('v type')
        print(type(v))
        jsaa = jsonify(v)
        print('here')
        print(jsonify(v))
        return jsaa