import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import pymysql
import datetime


PATH = "C:/Users/M4610-1/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://591.com.tw/")

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "leo77777",
    "db": "house",
    "charset": "utf8"
}

WebDriverWait(driver, 10).until(  # 等20到看板的class出現後再去取得
    EC.presence_of_element_located((By.CLASS_NAME, "area-box-title"))
)
# 台北市
city = driver.find_element(By.XPATH, '//*[@id="area-box-body"]/dl[1]/dd[1]');
city.click()

time.sleep(1)
close = driver.find_element(By.CLASS_NAME, 'close')
close.click()
time.sleep(2)

choose = driver.find_element(By.XPATH, '/html/body/section[1]/div[3]/div/div[1]/a[2]')
action = webdriver.ActionChains(driver)
action.move_to_element(choose)
action.perform()

time.sleep(1)
search = driver.find_element(By.XPATH, '/html/body/section[1]/div[3]/div/div[2]/div[2]')
search.click()

time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".accreditPop .close").click()
driver.find_element(By.CLASS_NAME, 'tips-popbox-img').click()
# 到了搜尋結果頁面拉
# TODO 把TITLES全部裝進一個LIST 跑迴圈



def run():
    time.sleep(1)
    # 多個的find_elements
    titles = driver.find_elements(By.CSS_SELECTOR, ".houseList-item-title a")
    # print(titles[2].text)  # 印出第三個的Title
    for title in titles:
        # print(title.text)
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, title.text).click()

        handle = driver.current_window_handle
        handles = driver.window_handles

        # 對窗口進行遍歷
        for newhandle in handles:

            # 篩選新打開的窗口B
            if newhandle != handle:
                driver.switch_to.window(newhandle)
                # time.sleep(3)
                # 在新打开的窗口B中操作
                # 這裡開始找資料 house_detail.py
                try:
                    if(None != driver.find_element(By.CLASS_NAME,'info-span-name')):
                        host_name = driver.find_element(By.CLASS_NAME, 'info-span-name')
                        print(host_name.text)
                    if (None != driver.find_element(By.CLASS_NAME, 'info-host-word')):
                        phone_number = driver.find_element(By.CLASS_NAME, 'info-host-word')
                        print(phone_number.text)
                    try:
                        # 建立Connection物件
                        conn = pymysql.connect(**db_settings)
                        # 建立Cursor物件
                        with conn.cursor() as cursor:
                            # 新增資料SQL語法
                            command = "SELECT * FROM house_info"
                            cursor.execute(command)
                            date_now = datetime.datetime.now()
                            # 取得所有資料

                            result = cursor.fetchall()
                            result_list = list(result)
                            phone_num_list = []
                            for r in result_list:
                                id = r[0]
                                name = r[1]
                                phone_num = r[2]
                                phone_num_list.append(phone_num)
                                print(id, name, phone_number)

                            if (phone_number not in phone_num_list):
                                command = "INSERT IGNORE INTO house_info(name, phone_number,date_time)VALUES(%s, %s,%s) "
                                cursor.execute(
                                     command, (host_name.text, phone_number.text, date_now)
                                )
                                # 儲存變更
                                conn.commit()
                    except Exception as ex:
                        print(ex)
                    finally:
                        conn.close();
                except:
                    print("建商案>>>>>>>>>")
                    pass




                # 關閉當前窗口B
                driver.close()
                # 切换回窗口A
            driver.switch_to.window(handles[0])

run()
pages = driver.find_elements(By.CLASS_NAME , 'pageNext')
total_page_num = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div[4]/a[7]')

for i in range(int(total_page_num.text)):
    page_next = driver.find_element(By.CLASS_NAME,"pageNext")
    action = ActionChains(driver)
    action.click(page_next)  # 點擊下一頁按鈕
    action.perform()
    #跳轉後先執行在等待
    time.sleep(3)
    run()
