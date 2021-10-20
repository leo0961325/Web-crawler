from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v95 import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

PATH = "C:/Users/M4610-1/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://sale.591.com.tw/home/house/detail/2/9961916.html")

host_name = driver.find_element(By.CLASS_NAME,'info-span-name')
print(host_name.text)

phone_number = driver.find_element(By.CLASS_NAME,'info-host-word')
print(phone_number.text)