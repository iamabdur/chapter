import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abdur@2002",
    database="project"
    )

# if mydb:
#     print("success")
# else:
#     print("unsuccess")

c=mydb.cursor()
query="select * from admin"
c.execute(query)
# query="select * from admin;"
print(c.fetchall())
# dat=c.fetchall()
# print(dat)
# mydb.commit()
# mydb.close()\
