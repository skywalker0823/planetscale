
from dotenv import load_dotenv
import os
import MySQLdb


load_dotenv()

connection = MySQLdb.connect(
    host= os.getenv("HOST"),
    user=os.getenv("USERNAME"),
    passwd= os.getenv("PASSWORD"),
    db= os.getenv("DATABASE"),
    autocommit = True,
    ssl_mode = "VERIFY_IDENTITY",
    ssl      = {
        "ca": "/etc/ssl/cert.pem"
    }
)

# test if connection is working
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM queue")
        result = cursor.fetchall()
        print(result)
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    connection.close()


class DB:
    def get_user(self, username):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print("Exeception occured:{}".format(e))
            return None
    def insert_user(self, username, password):
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            return False