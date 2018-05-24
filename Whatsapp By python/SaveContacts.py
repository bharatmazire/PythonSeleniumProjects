import pandas as pd
import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

username = str(input("Enter User name : "))
password = str(getpass.getpass("Enter Password : "))

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome('/home/nowhere/Downloads/chromedriver',chrome_options = chrome_options)

driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https%3A%2F%2Fcontacts.google.com%2F&followup=https%3A%2F%2Fcontacts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")



df = pd.read_excel("sample.xlsx",names = [x for x in range(8)])

time.sleep(2)

elem = driver.find_element_by_xpath('//*[@id="identifierId"]')
elem.send_keys(username)
elem.send_keys(Keys.RETURN)

time.sleep(1)

elem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

time.sleep(1)

for i in range(df.count()[0]):
	
	elem = driver.find_element_by_xpath('/html/body/div[9]/c-wiz/div[4]/div/content/div')
	elem.click()
	time.sleep(3)
	
	print(df[2][i],end = " ")
	name = df[2][i]
	elem = driver.find_element_by_xpath('/html/body/div[9]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
	elem.send_keys(name)
	elem.send_keys(Keys.RETURN)
	
	print(df[6][i])
	phone = df[6][i]
	elem = driver.find_element_by_xpath('/html/body/div[9]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input')
	elem.send_keys(str(phone))
	elem.send_keys(Keys.RETURN)
	
	print("contact entered !!!")
	elem = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div[1]/div[17]/div/div[3]/content')
	elem.click()
	time.sleep(3)

	print("contact saved !!!")
	elem = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[4]/div/div[2]/content/div/div[1]/div/div[3]/div[4]')
	elem.click()
	time.sleep(3)

time.sleep(2)
driver.close()