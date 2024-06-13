from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib3.packages.six import b
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time




options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    service=  Service(chromedriverPath), 
    options=options,
)



ptp = target

#Open parkrun page
driver.get(ptp)

first_name = driver.find_element(By.ID, 'input_12_1')  # Replace 'username' with the actual element ID
first_name.send_keys('your_firstname')
surname = driver.find_element(By.ID, 'input_12_2')  # Replace 'username' with the actual element ID
surname.send_keys('chocolate')
tel_number = driver.find_element(By.ID, 'input_12_13')
tel_number.send_keys('08001234')
email = driver.find_element(By.ID, 'input_12_4')
email.send_keys('example@aol.com')
location= driver.find_element(By.ID, 'input_12_11')
location.send_keys('Wordington')
rooms = driver.find_element(By.ID, 'input_12_8')
rooms.send_keys('3')
availability = driver.find_element(By.ID, 'input_12_9')
availability.send_keys('6 Months')
status = driver.find_element(By.ID, 'input_12_7')
status.send_keys('Homeowner')
day = driver.find_element(By.ID, 'input_12_14_2')
day.send_keys('01')
month = driver.find_element(By.ID, 'input_12_14_1')
month.send_keys('06')
year = driver.find_element(By.ID, 'input_12_14_3')
year.send_keys('2024')
check = driver.find_element(By.ID, 'field_12_10')
check.click()
#submit= driver.find_element(By.ID, "gform_submit_button_12")
#submit.click()


time.sleep(10)


