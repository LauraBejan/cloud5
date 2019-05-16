import pyodbc
server = 'cct5server.database.windows.net'
database = 'cct5DB'
username = 'adminrole'
password = 'adminpass1!'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def customQuery(query):
    return cursor.execute(query).fetchone()
