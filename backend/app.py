from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
#from models import User, Course, Student, StaffMember, Semester, Requirement
from query_factory import QueryFactory
from datetime import datetime
from pusher import Pusher

app = Flask(__name__)
CORS(app, support_credentials=True)
query_factory = QueryFactory()
query_factory.initialize_connection(db_name="efa", db_user="postgres", db_password="jimmy")

    # configure pusher object
pusher = Pusher(
      app_id='1149611',
      key='53327a58e47a84312542',
      secret='aa52a12e8d34e1d87b04',
      cluster='eu',
      ssl=True
    )

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
        data = ""
        pusher.trigger('matches', 'stadium-added', data)
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

@app.route('/createMatch',methods=['POST'])
def addMatch():
    match = request.get_json()
    print(match)
    stadium = match.get('stadium')
    homeTeam = match.get('homeTeam')
    awayTeam = match.get('awayTeam')
    referee = match.get('referee')
    lineman1 = match.get('lineman1')
    lineman2 = match.get('lineman2')
    mdate = match.get('mdate')
    mtime = match.get('mtime')
    response = query_factory.addMatch(stadium,homeTeam,awayTeam,referee,lineman1,lineman2,mdate,mtime)
    if(response):
        print("Match was not added an error occured")
    else:
        data = ""
        pusher.trigger('matches', 'match-added', data)
        print("Match added sucessfully")
    return jsonify(response)

@app.route('/editMatch',methods=['POST'])
def editMatch():
    match = request.get_json()
    print(match)
    mId = match.get("id")
    stadium = match.get('stadium')
    homeTeam = match.get('homeTeam')
    awayTeam = match.get('awayTeam')
    referee = match.get('referee')
    lineman1 = match.get('lineman1')
    lineman2 = match.get('lineman2')
    mdate = match.get('mdate')
    mtime = match.get('mtime')
    response = query_factory.EditMatch(mId,stadium,homeTeam,awayTeam,referee,lineman1,lineman2,mdate,mtime)
    if(response):
        print("Match was not edited an error occured")
    else:
        data = ""
        pusher.trigger('matches', 'match-edited', data)
        print("Match edited sucessfully")
    return jsonify(response)
    
@app.route('/getMatches',methods=['GET'])
def getMatches():
    queryResult = query_factory.getMatches()
    matches = []
    #print(queryResult)
    for match in queryResult:
        dec = {}
        dec["id"] =  match[0]
        dec["stadium"] = match[1]
        dec["homeTeam"] = match[2]
        dec["awayTeam"] = match[3]
        dec["referee"] = match[4]
        dec["lineman1"] = match[5]
        dec["lineman2"] = match[6]
        dec["date"] =str(match[7])
        dec["time"] = str(match[8])
        dec["homeName"] = match[9]
        dec["awayName"] = match[10]
        dec["stadiumName"] = match[11]
        dec["refName"] = match[12]
        dec["lName1"] = match[13]
        dec["lName2"] = match[14]
        #dec["show"] = False
        matches.append(dec)
    #print(matches)
    
    return jsonify(matches)

    
@app.route('/getStadiumsSeats',methods=['GET'])
def getStadiumsSeats():
    match_id = request.args.get("match_id")
    response = query_factory.getStadiumsSeats(match_id)
    return jsonify(response)

@app.route('/addSeats',methods=['POST'])
def addSeats():
    reservation = request.get_json()
    matchId = reservation.get('matchId')
    userId = reservation.get('userId')
    seats = reservation.get('seats')
    reserved_seats = query_factory.reserveStadiumsSeats(matchId,userId,seats)
    data=""
    pusher.trigger('seats', 'seat-reserved', data)
    return jsonify(reserved_seats)

@app.route('/numberOfReservedSeats',methods=['GET'])
def numberOfReserSeats():
    mId = request.args.get("mid")
    response = query_factory.numberOfRecvSeasts(mId)
    return jsonify(response[0][0])