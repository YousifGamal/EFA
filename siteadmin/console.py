import psycopg2
from psycopg2 import Error
from flask import Flask, render_template,jsonify
from flask_cors import CORS
import tempfile
try:
    connection = psycopg2.connect(
        user="postgres",
        password="newpassword",
        host="127.0.0.1",
        port="5432",
        database="efa")
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT * from efa.user;")
    # Fetch result
    record = cursor.fetchall()
    print("You are connected to - ", record, "\n")
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)


app = Flask(__name__)

'''
@app.route("/")
def index():
    return render_template("index.html")
'''
#try to make a dynamic URL with variables
#here we assign the value name dynamically so it should create our route
cors = CORS(app, resources={r"/showallusers/*": {"origins": "*"},r"/deleteuser/*": {"origins": "*"}})
@app.route("/showallusers/")
def showallusers():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="newpassword",
            host="127.0.0.1",
            port="5432",
            database="efa")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT user_id,first_name,last_name from efa.user;")
        # Fetch result
        records = cursor.fetchall()
        print("You are connected to - ", records, "\n")
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return jsonify(records)

@app.route("/deleteuser/<int:id>")
def deleteuser(id):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="newpassword",
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
    return "done"

if __name__ == "__main__":
    app.run(port=7777,debug=True)

'''
insert into efa."user" values(1,'25','69','s','s','2019-03-06','s','madirdi','sdf','sdfds','sdf',0);
'''