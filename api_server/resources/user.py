from flask_restful import Resource
from flask import jsonify
import pymysql


class Users(Resource):
    def db_init(self):
        db = pymysql.connect('localhost', 'root', 'password', 'api')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self):
        db, cursor = self.db_init()
        sql = 'Select * From api.users'
        cursor.execute(sql)
        db.commit()
        users = cursor.fetchall()
        db.close()

        return jsonify({'data':users})
