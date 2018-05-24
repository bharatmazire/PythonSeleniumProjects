import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import time

name = str(input("Enter name for group : "))

df = pd.read_excel("sample.xlsx",names = [x for x in range(8)])

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('/home/nowhere/Downloads/chromedriver',chrome_options = chrome_options)

driver.get("https://web.whatsapp.com/")
#assert "Python" in driver.title
time.sleep(3)


elem = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
elem.click()

elem = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
elem.click()
'''
for i in range(df.count()[0]):
	phone = df[6][i]
	elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[1]/div/div/input')
	elem.send_keys(str(phone))
	time.sleep(2)
	try:
		elem1 = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div/div[2]')
		elem.send_keys(Keys.RETURN)
	except NoSuchElementException:
		for p in range(10):
			elem.send_keys(Keys.BACKSPACE)
'''
elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[1]/div/div/input')
elem.send_keys("940483")
time.sleep(2)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/span/div')
elem.click()	

elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div[1]/div[2]')
elem.send_keys(name)
#elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/span/div/div')
elem.click()

time.sleep(3)
elem = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]')
elem.send_keys("Welcome to "+ name +" Group ...")
elem.send_keys(Keys.RETURN)

time.sleep(2)
driver.close()

