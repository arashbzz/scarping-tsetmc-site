from numpy import array
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import threading
namads = pd.read_csv('c:/w/market_index/namad_url.csv',encoding="utf-8-sig")
print(array(namads))

driver = list()
result = dict()

def page_opening(namad_code, namad_name ):
    driver = webdriver.Firefox()
    driver.get(f'http://www.tsetmc.com/Loader.aspx?{namad_code}')
    elem = driver.find_elements_by_xpath('//td[@id="e9"]')
    time.sleep(10)
    e = elem[0].text
    result[namad_name] = e
    print(result)
    driver.close()


if __name__ == '__main__':
    for i in range(len(array(namads))):
        namad_code = array(namads)[i][1]
        namad_name = array(namads)[i][0]
        print(namad_code)
        thread = threading.Thread(
            target=page_opening, args=(namad_code, namad_name))
        thread.start()
