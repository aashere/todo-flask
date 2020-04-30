#models.py handles everything involving a database (Data)
#we will use Python SQLite
#In general, for sql queries, do the following:
#1) import sqlite3 module (a module is a Python file/library)
import sqlite3
#2) create a connection to database, name database todo.db:
# conn = sqlite3.connect('todo.db') 
#3) Write sql query with:
# query = "<SQLite Query goes here>"
#4) Execute the query with:
# result = conn.execute(query)

#2 classes: Schema, to create + maintain tables (users)
#           and Todo, for operations related to the todo table

#Schema
class Schema:
    #__init__(self) is the constructor, the first arg
    #is the instance of the class, similar to this in Java
    # always have to include self as first parameter of any
    #object-specific method declaration
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        #Create user table and THEN create todo table
        #Do in this order, because users have to exist
        #first, and then their todo tables can be created
        self.create_user_table()
        self.create_to_do_table()
    
    def create_to_do_table(self):
        #create table if it doesn't exist
        # INTEGER PRIMARY KEY 
        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """
        self.conn.execute(query)

    def create_user_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "User" (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT,
            CreatedOn Date default CURRENT_DATE        
        );
        """
        self.conn.execute(query)