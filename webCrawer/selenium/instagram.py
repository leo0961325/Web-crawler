from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

PATH = "C:/Users/M4610-1/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

# explict wait
username = WebDriverWait(driver, 10).until(  # 等20到看板的class出現後再去取得
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(  # 等20到看板的class出現後再去取得
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()
username.send_keys('harvey09613257@gmail.com')
password.send_keys('leo77777')

login.click()
time.sleep(5)

next_time = driver.find_element_by_class_name('HoLwm')
next_time.click()

# IG搜尋比較特別，要停頓一下子
search = driver.find_element(By.CLASS_NAME,"XTCLo")
keyword = "#cats"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(3)

#讓他滑個10次好了
for i in range(10):
    # 執行javaScript 把滾輪滑到底
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)

imgs = driver.find_elements(By.CLASS_NAME,"FFVAD")
# 創建資料夾
path = os.path.join(keyword)
os.mkdir(path)

count=0
for img in imgs :
    save_as = os.path.join(path , keyword+str(count)+".jpg")
    #wget.download下載甚麼，存放在哪裡
    wget.download(img.get_attribute("src"),save_as)
    print(img.get_attribute("src"))
    count+=1