from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()



class cheese:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def get_free_proxies(driver):
        driver = webdriver.Chrome()
        driver.get('https://sslproxies.org')

        table = driver.find_element(By.TAG_NAME, 'table')
        thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
        tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        headers = []
        for th in thead:
            headers.append(th.text.strip())

        proxies = []
        for tr in tbody:
            proxy_data = {}
            tds = tr.find_elements(By.TAG_NAME, 'td')
            for i in range(len(headers)):
                proxy_data[headers[i]] = tds[i].text.strip()
            proxies.append(proxy_data)
    
        return proxies

    def extract_ip_addresses(self, ip_list):
    # Initialize an empty list to store the extracted IP addresses
        ip_addresses = []
    
    # Iterate over each dictionary in the list
        for entry in ip_list:
        # Extract the 'IP Address' value from the dictionary
            ip = entry.get('IP Address')
            if ip:
                ip_addresses.append(ip)
    
        return ip_addresses


p1= cheese()


a1 = p1.get_free_proxies()
b1 = p1.extract_ip_addresses(a1)
print(b1)
