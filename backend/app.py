from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
#from models import User, Course, Student, StaffMember, Semester, Requirement
from query_factory import QueryFactory
from datetime import datetime
from crypto import *

app = Flask(__name__)
CORS(app, support_credentials=True)
query_factory = QueryFactory()
query_factory.initialize_connection(db_name="efa", db_user="postgres", db_password="pass123")



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
    return jsonify(reserved_seats)

@app.route('/numberOfReservedSeats',methods=['GET'])
def numberOfReserSeats():
    mId = request.args.get("mid")
    response = query_factory.numberOfRecvSeasts(mId)
    return jsonify(response[0][0])


@app.route('/createUser',methods=['POST'])
def createUser():
    data = request.get_json()
    print(data)
    response = query_factory.checkUsername(data["username"])
    if response:
        return jsonify({'errors': 'username already exists'}), 400
    else:
        response = query_factory.addUser(data)
        print(response)
        return jsonify({'msg': 'user created successfully'}), 200



@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    response = query_factory.authenticate(data)
    if response:
        return jsonify({'user': response}), 200
    else:
        return jsonify({'error': 'user credentials is not right'}), 400


@app.route('/profile',methods=['GET'])
def getProfile():
    username = request.args.get("username")
    # print(username)
    data = query_factory.getUser(username)
    # print(data)
    response = {"username":data[1],
          "email": data[9],
          "first_name": data[3],
          "last_name":data[4],
          "gender":data[6],
          "role":data[10],
          "password":"",
          "city":data[7],
          "address":data[8],
          "birth_date":data[5].strftime('%Y-%m-%d')}

    return jsonify({'user': response}), 200

    
@app.route('/profileUpdate',methods=['PUT'])
def updateProfile():
    data = request.get_json()
    print(data)
    response = query_factory.updateUser(data)

    return jsonify({'update': "successed"}), 200



# @app.route('/test',methods=['get'])
# def test():

#     username = "onetwo"
#     newpass = "123"

#     # stringhashed = encrypt_message(newpass)
#     # stringhashed = stringhashed.decode('utf-8')
#     # print(stringhashed,type(stringhashed))
#     # query_factory.updatePass(stringhashed,username)

#     text = query_factory.getPass(username)
#     print(text,type(text))
#     my_str_as_bytes =  text.encode('utf-8')
#     print(my_str_as_bytes,type(my_str_as_bytes))
    
#     print(decrypt_message(my_str_as_bytes))

#     return jsonify({'update': "successed"}), 200

