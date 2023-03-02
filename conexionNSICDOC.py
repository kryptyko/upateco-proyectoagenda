import pymssql

conn = pymssql.connect(server='10.0.0.219', user='rafael', password='rr', database='NSICDOC')
cursor = conn.cursor()
cursor.execute("SELECT * FROM OPERADORES")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()