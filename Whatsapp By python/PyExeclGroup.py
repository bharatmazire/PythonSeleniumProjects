from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print ("1") 
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/home/nowhere/Downloads/chromedriver')

print ("2")
driver.get("https://web.whatsapp.com/")
#assert "Python" in driver.title
print ("3")
time.sleep(5)
'''
elem = driver.find_element_by_xpath('//*[@id="input-chatlist-search"]')
elem.clear()
'''
elem = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
elem.click()

	
print ("4")
'''
elem.send_keys("piyusha")
elem.send_keys(Keys.RETURN)
print ("5")
#assert "No results found." not in driver.page_source
'''
time.sleep(10)
print ("6")
driver.close()
print ("7")
