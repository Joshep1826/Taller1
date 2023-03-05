from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/")

driver.set_window_size(1024, 600)
driver.maximize_window()

element_web = driver.find_element(By.NAME, "search_query")
element_web.send_keys("willie colon che che cole itagüí" + Keys.ENTER)

time.sleep(15)