#########################################################################
#																		#
#	SaveContacts.py														#
#																		#
#	This program will read .xlsx {excel} file and store its content		#
#	to contact.google.com												#
#																		#
#########################################################################

import pandas as pd
import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time


def loginDetails():
    username = str(input("Enter User name : "))
    password = str(getpass.getpass("Enter Password : "))
    return username , password

    
def browserSetup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome('/home/nowhere/Downloads/chromedriver',chrome_options = chrome_options)
    return driver
    
    
def goToSite(driver,site):
    driver.get(site)

    
def readExcel():
    excel_name = str(input("Enter Excel file name : "))
    df = pd.read_excel(excel_name,names = [x for x in range(8)])
    return df

def enterValue(driver,username,password,df,n,p):
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
        
        print(df[n][i],end = " ")
        
        name = df[n][i]
        elem = driver.find_element_by_xpath('/html/body/div[9]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
        elem.send_keys(name)
        elem.send_keys(Keys.RETURN)
        
        print(df[p][i])
        
        phone = df[p][i]
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


def closeBrowser(driver):
    driver.close()

def main():
    site = "https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https%3A%2F%2Fcontacts.google.com%2F&followup=https%3A%2F%2Fcontacts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    username , password =  loginDetails()
    n = int(input("Enter name column number {starting from 0}"))
    p = int(input("Enter phone column number {starting from 0}"))
    driver = browserSetup()
    goToSite(driver,site)
    df = readExcel()
    time.sleep(1)
    enterValue(driver,username,password,df,n,p)
    time.sleep(2)
    closeBrowser(driver)

if __name__=='__main__':
    main()
