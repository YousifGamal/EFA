from flask import Flask, request, jsonify,make_response
from flask_cors import CORS, cross_origin
#from models import User, Course, Student, StaffMember, Semester, Requirement
from query_factory import QueryFactory
from datetime import datetime
from pusher import Pusher


# imports for PyJWT authentication 
import jwt
import hashlib 
from datetime import datetime, timedelta 
from functools import wraps 

app = Flask(__name__)
CORS(app, support_credentials=True)
query_factory = QueryFactory()
query_factory.initialize_connection(db_name="efa", db_user="postgres", db_password="jimmy")

app.config['SECRET_KEY'] = 'el secret key aho'

# decorator for verifying the JWT 
def token_required(f): 
    @wraps(f) 
    def decorated(*args, **kwargs): 
        print(request.headers)
        token = None
        # jwt is passed in the request header 
        if 'x-access-token' in request.headers: 
            token = request.headers['x-access-token'] 
        # return 401 if token is not passed 
        if not token: 
            return jsonify({'message' : 'Token is missing !!'}), 401
   
        try: 
            # decoding the payload to fetch the stored details 
            data = jwt.decode(token, app.config['SECRET_KEY']) 
            # current_user = User.query\ 
            #     .filter_by(public_id = data['public_id'])\ 
            #     .first() 
        except: 
            return jsonify({ 
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes 
        return  f(*args, **kwargs) 
   
    return decorated 


    # configure pusher object
pusher = Pusher(
      app_id='1149611',
      key='53327a58e47a84312542',
      secret='aa52a12e8d34e1d87b04',
      cluster='eu',
      ssl=True
    )

@app.route('/AddStadium',methods=['POST'])
@token_required
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
@token_required
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
@token_required
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
@token_required
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
@token_required
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
@token_required
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
@token_required
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
        matches.append(dec)
    print(matches)
    
    return jsonify(matches)

    
@app.route('/getStadiumsSeats',methods=['GET'])
def getStadiumsSeats():
    match_id = request.args.get("match_id")
    response = query_factory.getStadiumsSeats(match_id)
    return jsonify(response)

@app.route('/addSeats',methods=['POST'])
@token_required
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

'''
    show/delete users functions
'''

@app.route("/showallusers/")
@token_required
def showAllUsers():
    response = query_factory.getAllUsers()
    print(response)
    return jsonify(response)

@app.route("/searchforuser/<string:userName>")
@token_required
def searchUser(userName):
    response = query_factory.searchUser(userName)
    print(response)
    return jsonify(response)

@app.route("/deleteuser/<int:id>")
@token_required
def deleteUser(id):
    response = query_factory.deleteUser(id)
    return response


'''
    show/delete/approve pending users functions
'''

@app.route("/showpendingusers/")
@token_required
def showAllPendingUsers():
    response = query_factory.getAllPendingUsers()
    print(response)
    return jsonify(response)

@app.route("/searchforpending/<string:userName>")
@token_required
def searchPendingUser(userName):
    response = query_factory.searchPendingUser(userName)
    print(response)
    return jsonify(response)

@app.route("/approvepending/<int:id>")
@token_required
def approvePending(id):
    response = query_factory.approvePendingUser(id)
    return response

'''
    show/delete tickets functions
'''
@app.route("/showusertickets/<int:id>")
@token_required
def showUserTickets(id):
    response = query_factory.showTickets(id)
    tickets = []
    print(response)
    for ticket in response:
        dec = {}
        dec[0] = ticket[0]
        dec[1] = ticket[1]
        dec[2] = ticket[2]
        dec[3] = str(ticket[3])
        dec[4] = str(ticket[4])
        dec[5] = ticket[5]
        dec[6] = ticket[6]
        tickets.append(dec)
    print(tickets)
    return jsonify(tickets)

@app.route("/deleteticket/<int:ticketId>")
@token_required
def deleteUserTicket(ticketId):
    print(ticketId)
    response = query_factory.deleteTicket(ticketId)
    data="yaraaab"
    pusher.trigger('seats', 'seat-reserved', data)
    return response

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
        token = jwt.encode({ 
            'username': response[0],
            'role': response[1], 
            'exp' : datetime.utcnow() + timedelta(minutes = 30) 
        }, app.config['SECRET_KEY']) 
   
        return make_response(jsonify({'token' : token.decode('UTF-8'),'role':response[0],'status':response[1] , 'id':response[2]}), 201) 
        # return jsonify({'user': response}), 200
    else:
        return make_response( 
            'Could not verify', 
            403, 
            {'WWW-Authenticate' : 'Basic realm ="User credentials is not right !!"'} 
        ) 
        # return jsonify({'error': 'user credentials is not right'}), 400


@app.route('/profile',methods=['GET'])
@token_required
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
@token_required
def updateProfile():
    data = request.get_json()
    print(data ," incoming payload")
    response = query_factory.updateUser(data)

    return jsonify({'update': "successed"}), 200

@app.route('/passUpdate',methods=['PUT'])
@token_required
def updatePass():
    data = request.get_json()
    # check if the password is correct 
    userPass = query_factory.getPass(data['username'])
    oldPass  = hashlib.sha256(data['password'].encode()).hexdigest()

    if userPass == oldPass:
        response = query_factory.updatePass(data)
        return jsonify({'update': "successed"}), 200
    else:
        return jsonify({'update': "failed"}), 200




