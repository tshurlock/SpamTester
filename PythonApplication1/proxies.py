from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import localVariables
import time
import proxyGetter

p1= proxyGetter.get_proxies()


a1 = p1.get_free_proxies()
proxies = p1.extract_ip_addresses(a1)
print('These are the proxies')
print(proxies)
print('End of the proxies')

for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome( service=  Service(localVariables.chromedriverPath), 
        options=options)
        driver = webdriver.Chrome(options=options, executable_path= localVariables.chromedriverPath)
        driver.get("https://www.whatismyip.com/proxy-check/?iref=home")
       
        if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
            break
    except Exception:
        driver.quit()
print("Proxy Invoked")
