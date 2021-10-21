import pymysql
import datetime

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "leo77777",
    "db": "house",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "SELECT * FROM house_info"
        cursor.execute(command)

        add_phone = '0979-611-629'
        date_now = datetime.datetime.now()
        # 取得所有資料
        result = cursor.fetchall()
        result_list = list(result)
        phone_num_list = []
        for r in result_list:
            id = r[0]
            name = r[1]
            phone_number = r[2]
            phone_num_list.append(phone_number)
            print(id , name , phone_number)

        if (add_phone not in phone_num_list):
            command = "INSERT IGNORE INTO house_info(name, phone_number,date_time)VALUES(%s, %s,%s) "
            cursor.execute(
            command,("make",add_phone,date_now)
            )
            # 儲存變更
            conn.commit()

    # 資料表相關操作
except Exception as ex:
    print(ex)
finally:
    conn.close();
