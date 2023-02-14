import pymysql
# class dbhandler(Exception):
#     pass
# from main import user
# class Database:
#     def __init__(self,host,user,password,port,database):
#         self.host=host
#         self.user = user
#         self.port=port
#         self.password=password
#         self.database=database
#     def print(self):
#         mydb = None
#         mydbCursor=None
#         try:
#             # Get DB Connection
#             mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
#             # Get cursor object
#             mydbCursor = mydb.cursor()
#             # sql="Select * from students"
#             mydbCursor.execute("Select* from users")
#             users = mydbCursor.fetchall()
#             for user in users:
#                 print(user)
#             # for r in myresults:
#             #     print(r)
#             #     # print("id:",r[0],"Rollno:",r[1],"Name:",r[2],"Semmester:",r[3],"CGPA:",r[4])
#             #     print("Rollno:", r[0], "Name:", r[1], "Semmester:", r[2])
#
#         except Exception as e:
#             print(str(e))
#         finally:
#             if mydbCursor != None:
#                 mydbCursor.close()
#             if mydb != None:
#                 mydb.close()

# a= Database('localhost','root','SAMA786000',3306,'new_schema1')
# a.print()
