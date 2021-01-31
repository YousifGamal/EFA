from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
#from models import User, Course, Student, StaffMember, Semester, Requirement
from query_factory import QueryFactory
from datetime import datetime

app = Flask(__name__)
CORS(app, support_credentials=True)
query_factory = QueryFactory()
query_factory.initialize_connection(db_name="efa", db_user="postgres", db_password="jimmy")



@app.route('/AddStadium',methods=['POST'])
def addStadium():
    stadium = request.get_json()
    print(stadium)
    name = stadium.get('stadiumName')
    rows = stadium.get('rows')
    seatPerRow = stadium.get('seatsPerRow')
    res = query_factory.addStadium(name,rows,seatPerRow)
    if(res):
        print("stadium was not added an error occured")
    else:
        print("Stadium added sucessfully")
    response = {'res':res}
    return jsonify(response)