import pymysql

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
        command = "SELECT phone_number FROM info"
        cursor.execute(command)
        # 取得所有資料
        result = cursor.fetchall()
        print(result)
        add_phone = '0979-611-619'
        if (add_phone not in result):
            command = "INSERT IGNORE INTO info(name, phone_number )VALUES(%s, %s) "
            cursor.execute(
                command,("make",add_phone)
            )
            # 儲存變更
            conn.commit()

    # 資料表相關操作
except Exception as ex:
    print(ex)
finally:
    conn.close();
