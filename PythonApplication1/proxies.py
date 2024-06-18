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

'''proxies = ['189.240.60.168','172.183.241.1','189.240.60.163','221.140.235.236','203.205.9.105','85.111.60.196','221.140.235.237',
           '43.134.229.98','35.185.196.38','20.235.159.154','67.43.227.228','8.219.97.248','148.72.140.24','18.185.169.150',
           '3.127.62.252','15.236.145.64','3.37.125.76','18.228.198.164','3.122.84.99','52.16.232.164','52.67.10.183',
           '200.174.198.86','72.10.160.92','223.135.156.183','52.196.1.182','44.219.175.186','35.79.120.242','54.248.238.110',
           '52.73.224.54','3.212.148.199','44.195.247.145','13.37.89.201','15.236.106.236','46.51.249.135','13.38.176.104',
           '3.123.150.192','35.72.118.126','84.36.39.210','99.80.11.54','3.12.144.146','13.56.192.187','54.67.125.45',
           '13.59.156.167','3.21.101.158','43.134.32.184','67.43.228.254','35.243.227.100','43.134.33.254','72.10.160.90',
           '72.10.160.170','67.43.236.18','203.189.88.156','43.153.208.148','18.223.25.15','124.167.20.48','20.204.212.76',
           '20.44.190.150','20.204.212.45','20.204.214.23','67.43.227.230','13.212.30.209','20.44.189.184','188.247.194.210',
           '20.204.214.79','20.27.86.185','198.199.70.20','67.43.236.19','72.10.160.93','72.10.160.172','72.10.160.94',
           '185.217.136.67','180.88.100.7','154.236.189.19','163.172.33.137','80.66.81.44','209.121.164.50','41.65.251.47',
           '114.6.27.84','195.159.124.56','52.82.123.144','103.69.96.61','13.212.107.14','5.196.111.29','35.187.204.53',
           '41.111.243.133','8.213.151.128','5.189.184.6','34.215.74.117','20.219.176.57','185.141.134.120','62.210.37.74',
           '45.5.92.94','185.64.208.184','195.138.73.54','20.42.119.47','146.56.154.83','80.66.81.39','103.208.27.214',
           '134.209.144.177','38.60.254.99',]'''

p1= proxyGetter.get_proxies()


a1 = p1.get_free_proxies()
proxies = p1.extract_ip_addresses(a1)
print(proxies)

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
