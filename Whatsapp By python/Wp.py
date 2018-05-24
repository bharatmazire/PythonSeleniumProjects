#Different Selenium library automation tools will be required
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# following is path of Chrome driver
driver = webdriver.Chrome("/home/nowhere/Downloads/chromedriver")

#ayntax to open whatsapp.com
driver.get("https://web.whatsapp.com/")

#Now you need to scan the QR CODE on browser through your mobile whatsapp
wait = WebDriverWait(driver, 600)

#Person’s Name Whom you want to send message it should be exactly same as whatsapp name
target = '"Manya"'

#Write Message which you want to send
string = "MSG SENT BY PYTHON !!!"

#By this you will give the location where to search your target or contact
#So it will specify the place of message box on top
#and than search inside that your contact name if found than move ahead
x_arg = '//span[contains(@title,' + target + ')]'

#By.XPATH specifies a specific attribute in browser for example your message box
#wait.until() specifies that wait until your condition is found
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
#Now we perform the click task of the group_title to check every condition
group_title.click()
#Here input text xpath should be given for your input text message box
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
#This statement will perform the same task of waiting until your condition is satisfied
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
#Now for loop does the work of sending your content how many times you want to repeat
for i in range(10):
     #.send_keys is used to enter your string message inside input box and send it
     #By pressing Keys.Enter
     input_box.send_keys(string + Keys.ENTER)
    #sleep is used to take some time for send that is given 1 millisecond
     time.sleep(1)
