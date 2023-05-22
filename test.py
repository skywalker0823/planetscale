
# from dotenv import load_dotenv
# import os
# import MySQLdb

# load_dotenv()

# connection = MySQLdb.connect(
#     host= os.getenv("HOST"),
#     user=os.getenv("USERNAME"),
#     passwd= os.getenv("PASSWORD"),
#     db= os.getenv("DATABASE"),
#     autocommit = True,
#     ssl_mode = "VERIFY_IDENTITY",
#     ssl      = {
#         "ca": "/etc/ssl/cert.pem"
#     }
# )

# test if connection is working
# try:
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM queue")
#         result = cursor.fetchall()
#         print(result)
# except Exception as e:
#     print("Exeception occured:{}".format(e))
# finally:
#     connection.close()