from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:/Users/M4610-1/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")

# TODO 搜尋比特幣
search = driver.find_element_by_name("query")
search.clear()
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

# explict wait
WebDriverWait(driver, 20).until( #等20到看板的class出現後再去取得
                      EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
                      )

# TODO 取得標題
titles = driver.find_elements_by_class_name("tgn9uw-3")
for title in titles :
    print(title.text)
time.sleep(5)

link = driver.find_element_by_link_text("#新聞 Tribe Capital 將推出 7500 萬美元的加密貨幣基金")
link.click()
time.sleep(5)
driver.back()
driver.back()
driver.forward()

driver.quit()