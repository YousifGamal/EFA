import psycopg2
from psycopg2 import Error
from flask import Flask, render_template,jsonify
from flask_cors import CORS
import tempfile

app = Flask(__name__)

'''
@app.route("/")
def index():
    return render_template("index.html")
'''
#try to make a dynamic URL with variables
#here we assign the value name dynamically so it should create our route
cors = CORS(app, resources={r"/showallusers/*": {"origins": "*"},r"/showpendingusers/*": {"origins": "*"},
r"/searchforuser/*": {"origins": "*"},r"/searchforpending/*": {"origins": "*"},r"/approvepending/*": {"origins" :"*"},
r"/deleteuser/*": {"origins": "*"},r"/showusertickets/*":{"origins":"*"},r"/deleteticket/*":{"origins":"*"}})
@app.route("/showallusers/")
def showallusers():
    connection = None
    cursor = None
    records = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT user_id,user_name from efa.user where status = 0;")
        # Fetch result
        records = cursor.fetchall()
        print("You are connected to - ", records, "\n")
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    if records is not None:
        return jsonify(records)
    return ""

@app.route("/searchforuser/<string:userName>")
def searchUser(userName):
    connection = None
    cursor = None
    records = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("prepare dummy as SELECT user_id,user_name from efa.user where status = 0 and lower(user_name) Like lower($1);")
        cursor.execute("execute dummy (%s)",("%"+str(userName)+"%",))
        # Fetch result
        records = cursor.fetchall()
        print("You are connected to - ", records, "\n")
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    if records is not None:
        return jsonify(records)
    return ""

@app.route("/showpendingusers/")
def showPendingUsers():
    connection = None
    cursor = None
    records = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT user_id,user_name from efa.user where status = 1;")
        # Fetch result
        records = cursor.fetchall()
        print(records)
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    if records is not None:
        return jsonify(records)
    return ""


@app.route("/searchforpending/<string:userName>")
def searchPending(userName):
    connection = None
    cursor = None
    records = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("prepare dummy as SELECT user_id,user_name from efa.user where status = 1 and lower(user_name) Like lower($1);")
        cursor.execute("execute dummy (%s)",("%"+str(userName)+"%",))# Fetch result
        records = cursor.fetchall()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    if records is not None:
        return jsonify(records)
    return ""

@app.route("/approvepending/<int:id>")
def approvePending(id):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("update efa.user set status = 0 where user_id = %s;",(int(id),))
        # Fetch result
        connection.commit()
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return "done"

@app.route("/deleteuser/<int:id>")
def deleteuser(id):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("DELETE FROM efa.user where user_id = %s",(int(id),))
        # Fetch result
        connection.commit()
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return "done"


@app.route("/showusertickets/<int:id>")
def showUserTickets(id):
    connection = None
    cursor = None
    records = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("select reservation.ticket_number,match.home_team,match.away_team,match.mdate from efa.reservation \
         inner join efa.match on match.match_id = reservation.match_id where reservation.user_id= %s",(int(id),))
        # Fetch result
        records = cursor.fetchall()
        print(records)
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    if records is not None:
        return jsonify(records)
    return ""

@app.route("/deleteticket/<int:id>")
def deleteTicket(id):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="jimmy",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("DELETE FROM efa.reservation where reservation.ticket_number = %s",(int(id),))
        # Fetch result
        connection.commit()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
    return "done"

if __name__ == "__main__":
    app.run(port=7777,debug=True)

'''
insert into efa."user" values(1,'25','69','s','s','2019-03-06','s','madirdi','sdf','sdfds','sdf',0);
'''