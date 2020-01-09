from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_conn = create_engine("mysql+pymysql://username:pwd@serverlocation/database_name")
print(db_conn.table_names())
app = Flask(__name__)
api = Api(app)
class Users(Resource):
    def get(self):
        conn = db_conn.connect()
        query = conn.execute("select id, username, email, phone from usertable")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(Users, '/users')

if __name__ == "__main__":
    app.run(port="5002")
