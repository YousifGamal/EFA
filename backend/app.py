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

@app.route('/getStadiums',methods=['GET'])
def getStadiums():
    queryResult = query_factory.getStadiums()
    stadiums = []
    for stadium in queryResult:
        dec = {}
        dec["value"] =  stadium[0]
        dec["text"] = stadium[1]
        stadiums.append(dec)
    #print(stadiums)
    return jsonify(stadiums)

@app.route('/getTeams',methods=['GET'])
def getTeams():
    queryResult = query_factory.getTeams()
    teams = []
    for team in queryResult:
        dec = {}
        dec["value"] =  team[0]
        dec["text"] = team[1]
        teams.append(dec)
    #print(teams)
    return jsonify(teams)

@app.route('/getReferees',methods=['GET'])
def getReferees():
    queryResult = query_factory.getReferees()
    referees = []
    for referee in queryResult:
        dec = {}
        dec["value"] =  referee[0]
        dec["text"] = referee[1]
        referees.append(dec)
    #print(referees)
    return jsonify(referees)

@app.route('/getLinemen',methods=['GET'])
def getLinemen():
    queryResult = query_factory.getLinemen()
    Linemen = []
    for lineman in queryResult:
        dec = {}
        dec["value"] =  lineman[0]
        dec["text"] = lineman[1]
        Linemen.append(dec)
    #print(Linemen)
    return jsonify(Linemen)


