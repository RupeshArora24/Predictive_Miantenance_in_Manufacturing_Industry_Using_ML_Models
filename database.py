import sqlite3


def create_usertable():
    conn = sqlite3.connect('userdata.db',check_same_thread=False) #conn: conn is a variable or object that represents a connection to a database. 
    c = conn.cursor() #.cursor(): The cursor() method is called on the connection object (conn). A cursor is a control structure that enables you to interact with the database. It allows you to execute SQL queries and retrieve data from the database. The cursor() method creates a new cursor object associated with the database connection.
    c.execute('CREATE TABLE IF NOT EXISTS usertable1(email text,username TEXT,Password TEXT)')

def add_userdata(email,username,Password):
    conn = sqlite3.connect('userdata.db',check_same_thread=False)
    c = conn.cursor() #c = conn.cursor(): This line of code creates a cursor object c that you can use to interact with the database associated with the conn connection
    
    c.execute('INSERT INTO usertable1 VALUES (?,?,?)',(email,username,Password))
    conn.commit()
    conn.close()

def login_user(email,username,Password):
    conn = sqlite3.connect('userdata.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT * FROM usertable1 WHERE email=? AND username=? AND Password=?',(email,username,Password))
    data = c.fetchone() #The c.fetchone() method is used in Python with database cursor objects to retrieve a single row of the result set obtained from executing a SQL query. 
    if data == None :
        return False
    else:
        return True 
    
def view(email,username,Password):
    conn = sqlite3.connect('userdata.db',check_same_thread=False)
    c = conn.cursor()     
    c.execute('SELECT * FROM usertable1 WHERE email=? AND username=? AND Password=?',(email,username,Password))
    data = c.fetchall()
    if data==None :
        return True
    else :
        return False


def view_all_users():
    conn = sqlite3.connect('userdata.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('select * from usertable1')
    data = c.fetchall() # #The c.fetchall() method is used in Python with database cursor objects to retrieve a multiple row of the result set obtained from executing a SQL query.
    return data 


    