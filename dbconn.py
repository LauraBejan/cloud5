import pyodbc
server = 'cct5sqlserver.database.windows.net'
database = 'CCT5'
username = 'adminrole'
password = 'adminpass1!'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def customQuery(query):
    return cursor.execute(query).fetchone()

def exists(key):
    key = "'" + key + "'"
    result = cursor.execute("SELECT USES FROM SearchKeys WHERE VAL = {}".format(key)).fetchone()
    if result != None:
        return True
    return False

def getRandKey():
    number_of_rows = cursor.execute("SELECT COUNT(*) FROM SearchKeys;").fetchone()
    number_of_rows = int(list(number_of_rows)[0])
    import random
    rand_row = random.randint(1,number_of_rows)
    rand_key = cursor.execute("Select VAL From (Select Row_Number() Over (Order By USES) As RowNum , * From SearchKeys) t2 Where RowNum = {}".format(rand_row)).fetchone()
    return list(rand_key)[0]

def delete(key):
    key = "'" + key + "'"
    cursor.execute("DELETE FROM SearchKeys WHERE VAL = {}".format(key))
    cnxn.commit()

def insertKey(key):
    if exists(key) != True:
        key = "'" + key + "'"
        cursor.execute("INSERT INTO SearchKeys VALUES({},{})".format(key,0))
        cnxn.commit()

# insertKey("Trump")
# insertKey("Prank video")
# insertKey("Reaction")
# insertKey("Trump")
# insertKey("Prank video")
