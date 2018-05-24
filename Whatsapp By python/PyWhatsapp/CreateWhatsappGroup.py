#############################################################################
#																			#
#	CreateWhatsappGroup.py													#
#																			#
#	This program will read .xlsx {excel} file and store its content			#
#	to contact.google.com (if user want) and create group of those			#
#																			#
#############################################################################

import SaveContacts as sc

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

def createGroup(driver,df,p,group_name):
    elem = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
    elem.click()
    
    elem = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
    elem.click()
    
    for i in range(df.count()[0]):
        phone = df[p][i]
        elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[1]/div/div/input')
        elem.send_keys(str(phone))
        time.sleep(2)
        try:
            elem1 = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div/div[2]')
            elem.send_keys(Keys.RETURN)
        except NoSuchElementException:
            for p in range(10):
                elem.send_keys(Keys.BACKSPACE)
    
    elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/span/div')
    elem.click()
    
    elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div[1]/div[2]')
    elem.send_keys(group_name)
    elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div/span/div/div')
    elem.click()
    
    time.sleep(3)
    
    elem = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]')
    elem.send_keys("Welcome to "+ group_name +" Group ...")
    elem.send_keys(Keys.RETURN)
    

def main():
	#sc.main()
    print ("contact saved to contacts.google.com ...")
    site = "https://web.whatsapp.com/"
    group_name = str(input("Enter Group name : "))  
    driver = sc.browserSetup()
    df = sc.readExcel()
    p = int(input("Enter the column number having phone numbers {starting index 0}"))
    sc.goToSite(driver,site)
    time.sleep(5)
    createGroup(driver,df,p,group_name)
    time.sleep(4)
    sc.closeBrowser()

if __name__ == '__main__':
    main()
