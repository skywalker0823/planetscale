from dotenv import load_dotenv
import os

# pip install mysqlclient
# 如有錯誤通常是因為沒有安裝mysql相關開發工具 -> Mac:brew install mysql, 
import MySQLdb

load_dotenv()


class DB:
    def __init__(self):
        self.connection = MySQLdb.connect(
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
        self.cursor = self.connection.cursor()

    # is_connected
    def connected(self):
        if self.connection.open:
            return True
        else:
            return False
    
    # 關閉連線    
    def close(self):
        self.cursor.close()
        self.connection.close()

    # 查詢所有排隊資料
    def get_all_queue(self):
        self.cursor.execute("SELECT * FROM queue")
        result = self.cursor.fetchall()
        return result

    # 顯示所有table
    def show_all_tables(self):
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        return result
    
    # 建立table
    def create_queue(self):
        self.cursor.execute("CREATE TABLE queue (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(255), size INT)")
        return self.cursor.lastrowid

    def create_queue2(self):
        self.cursor.execute("CREATE TABLE queue2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(255), size INT)")
        return self.cursor.lastrowid

    def alter_queue(self):
        self.cursor.execute("ALTER TABLE queue ADD COLUMN more_data INT")
        return self.cursor.lastrowid

    # 刪除table
    def drop_all_tables(self):
        # drop all tables
        self.cursor.execute("DROP TABLE IF EXISTS queue2")
        self.cursor.execute("DROP TABLE IF EXISTS queue")
        return self.cursor.lastrowid
    
    # CRUD
    def insert_queue(self):
        name = input("請輸入姓名: ")
        phone = input("請輸入電話: ")
        size = input("請輸入人數: ")
        self.cursor.execute("INSERT INTO queue (name, phone, size) VALUES (%s, %s, %s)", (name, phone, size))
        return self.cursor.lastrowid
    
    def select_queue(self):
        id = input("請輸入要查詢的id: ")
        self.cursor.execute("SELECT * FROM queue WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result

    def update_queue(self):
        id = input("請輸入要修改的id: ")
        name = input("請輸入姓名: ")
        phone = input("請輸入電話: ")
        size = input("請輸入人數: ")
        self.cursor.execute("UPDATE queue SET name = %s, phone = %s, size = %s WHERE id = %s", (name, phone, size, id))
        return self.cursor.lastrowid
    
    def delete_queue(self):
        id = input("請輸入要刪除的id: ")
        self.cursor.execute("DELETE FROM queue WHERE id = %s", (id,))
        return self.cursor.lastrowid

    @staticmethod
    def invalid_selection():
        print("輸入錯誤，請重新輸入")
        return "->invalid selection"
    
    @staticmethod
    def quit_program():
        print("Goodbye")
        exit(0)

def run():
    try:
        db = DB()
        if not db.connected():
            print("Not connected to MySQL database")
            exit(1)
        print("Connected to MySQL database")
        options = {
            "1": db.get_all_queue,
            "2": db.show_all_tables,
            "3": db.create_queue,
            "4": db.create_queue2,
            "5": db.drop_all_tables,
            "6": db.insert_queue,
            "7": db.select_queue,
            "8": db.update_queue,
            "9": db.delete_queue,
            "10": db.alter_queue,
            "Q": db.quit_program,
            "q": db.quit_program,
        }

        while True:
            select = input(
            """
            請選擇要執行的功能: 
            1. 查詢 * FROM queue table
            2. 顯示所有table
            3. 建立table queue
            4. 建立queue2
            5. 刪除所有table queue & queue2
            6. 新增排隊資料
            7. 查詢排隊資料
            8. 修改排隊資料
            9. 刪除排隊資料
            10. 修改queue表格
            Q/q. 離開
            """
            )
            result = options.get(select, db.invalid_selection)()
            print(result)

    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        db.close()

if __name__ == "__main__":
    run()
