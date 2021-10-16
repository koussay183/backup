import mysql.connector


all_err = ''

try :
    conn = mysql.connector.connect(
        host= 'localhost',
        user = 'userpython',
        passwd = 'python',
    )

        
    print('connected....')
except mysql.connector.Error as e :
    all_err += str(e) + ' , '

def dbrun(sql):
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute( sql )
            conn.commit()
            return True
        else :
            return False
    except mysql.connector.Error as e :
        all_err += str(e) + ' , '
        return False
