from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib3.packages.six import b
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import localVariables
import personClass




options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    service=  Service(localVariables.chromedriverPath), 
    options=options,
)

p1 = personClass.random_person()
print(p1)
time.sleep(20)

target = localVariables.target

#Open target page
driver.get(target)

first_name = driver.find_element(By.ID, 'input_12_1')  
first_name.send_keys(p1.first_name)
surname = driver.find_element(By.ID, 'input_12_2')  
surname.send_keys(p1.surname)
tel_number = driver.find_element(By.ID, 'input_12_13')
tel_number.send_keys(p1.tel_number)
email = driver.find_element(By.ID, 'input_12_4')
email.send_keys(p1.email)
location= driver.find_element(By.ID, 'input_12_11')
location.send_keys(p1.location)
rooms = driver.find_element(By.ID, 'input_12_8')
rooms.send_keys(p1.rooms)
availability = driver.find_element(By.ID, 'input_12_9')
availability.send_keys(p1.availability)
status = driver.find_element(By.ID, 'input_12_7')
status.send_keys(p1.status)
day = driver.find_element(By.ID, 'input_12_14_2')
day.send_keys(p1.day)
month = driver.find_element(By.ID, 'input_12_14_1')
month.send_keys(p1.month)
year = driver.find_element(By.ID, 'input_12_14_3')
year.send_keys(p1.year)
check = driver.find_element(By.ID, 'field_12_10')
check.click()
#submit= driver.find_element(By.ID, "gform_submit_button_12")
#submit.click()


time.sleep(10)


