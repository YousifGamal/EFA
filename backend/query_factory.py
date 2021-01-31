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
