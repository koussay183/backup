import mysql.connector

global all_err
all_err = ''

try :
    conn = mysql.connector.connect(
        host= 'localhost',#
        user = 'root',#
        passwd = 'mysql',#
        
    )
    
    
    print('SQL connected....')
except mysql.connector.Error as e :
    all_err += str(e) + ' , '

def dbrun(sql):
    global all_err
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute( sql )
            conn.commit()
            return True
        else :
            return False
    except mysql.connector.Error as e :
        all_err += str(e) + " , "
        return False
def dbget(sql):
    global all_err
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute( sql )
            all_rows = cur.fetchall()
            return all_rows
        else:
            return []
    except mysql.connector.Error as e:
        all_err += str(e) + " , "
        
dbrun("CREATE DATABASE IF NOT EXISTS easylife DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci")


