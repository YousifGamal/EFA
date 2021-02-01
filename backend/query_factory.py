from database_manager import DatabaseManager
#from models import User, Course, Student, StaffMember, Semester, Requirement
from typing import Optional
from psycopg2 import IntegrityError
class QueryFactory:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def initialize_connection(self, db_name: str, db_user: str, db_password) -> bool:
        connection_str: str = f"dbname='{db_name}' host=localhost user='{db_user}' password='{db_password}'"
        response = self.db_manager.initialize_connection(connection_str)
        if response is None:
            return True  # Successful connection
        else:
            
            print(response)
            return False  # Unsuccessful connection

    def insertLineman(self):
        name = "Ahmed Yasser"
        query : str = f"INSERT INTO efa.linesman(linesman_name)VALUES ('{name}');"
        self.db_manager.execute_query_no_return(query)
    
    def addStadium(self,name,rows,seatsPerRow):
        query:str= f"INSERT INTO efa.stadium (stadium_name, rows, columns)" \
                    f"VALUES ('{name}', {rows}, {seatsPerRow});"
        response = self.db_manager.execute_query_no_return(query)
        #all this dummy code if needed later
        error = False
        if response is not None:
            #some error happened
            error = True
        else:
            #no error happened
            error = False
        return error
    
    def getTeams(self):
        query:str = f"SELECT * FROM efa.teams;"
        response = self.db_manager.execute_query(query)
        return response

    def getLinemen(self):
        query:str = f"SELECT * FROM efa.linesman;"
        response = self.db_manager.execute_query(query)
        return response

    def getReferees(self):
        query:str = f"SELECT * FROM efa.referee;"
        response = self.db_manager.execute_query(query)
        return response

    def getStadiums(self):
        query:str = f"SELECT * FROM efa.stadium;"
        response = self.db_manager.execute_query(query)
        return response

    def addMatch(self,stadiumId,homeTmId,AwayTmId,refId,line1,line2,mdate,mtime):
        query:str = "INSERT INTO efa.match(" \
	                "stadium_id, home_team, away_team, main_referee,linesman_1,linesman_2, mdate, mtime)" \
	                f"VALUES ({stadiumId}, {homeTmId}, {AwayTmId}, {refId},"\
                    f" {line1}, {line2}, '{mdate}', '{mtime}');"
        response = self.db_manager.execute_query_no_return(query)
        error = False
        if response is not None:
            #some error happened
            print(response)
            error = True
        else:
            
            #no error happened
            error = False
        return error