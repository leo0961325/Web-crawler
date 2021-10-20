import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

PATH = "C:/Users/M4610-1/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://sale.591.com.tw/")

time.sleep(2)
pages = driver.find_elements(By.CLASS_NAME , 'pageNext')
total_page_num = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div[4]/a[7]')


for i in range(int(total_page_num.text)):
    page_next = driver.find_element(By.CLASS_NAME,"pageNext")
    action = ActionChains(driver)
    action.click(page_next)  # 點擊下一頁按鈕
    action.perform()
    time.sleep(10)


