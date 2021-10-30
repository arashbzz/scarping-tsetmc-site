from os import close
from numpy import array
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
import threading 

namads = pd.read_csv('c:/w/market_index/namad_url.csv')
print (array(namads))
print(array(namads)[0][1])

driver=[]
result=[]
driver = webdriver.Firefox()
for i in range(len(array(namads))):
     namad = array (namads)[i][1]
     
     driver.get(f'http://www.tsetmc.com/Loader.aspx?{namad}')
# # assert "Python" in driver.title
# # elem = driver.find_element_by_name("q")
     elem = driver.find_elements_by_xpath('//td[@id="e9"]')
     # elem.send_keys(Keys.COMMAND + 't')
     time.sleep(10)
     e = elem[0].text
     result.append(e)
     # driver.close()
     print(result)
print(result)
# print(elem)
# print(elem[0])
# print(elem[0].text)

# salaries_list = []
# for i in range(len(elem)):
#      salaries_list.append(str(elem[i].text))

# print (salaries_list)
# print (elem[0].text)

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()