import pymssql

# conn = pymssql.connect(server="210.115.229.92:11433", user="M22518", password="M22518@hallym", charset='utf8')
conn = pymssql.connect(server="localhost", database = 'test')
cursor = conn.cursor()

sql = "select * from student"
cursor.execute(sql)
cursor.fetchone()

for row in cursor :
    print(row)
conn.close()



