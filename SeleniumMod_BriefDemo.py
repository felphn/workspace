from selenium import webdriver
from selenium.webdriver.common.keys import Keys # import special keyboard keys like "F1", "Enter", etc.

driver = webdriver.Edge('e.g. C:\\Users\\Username\\Desktop\\msedgedriver.exe')
driver.get('e.g. https://www.facebook.com/')
# find first element in html script by name method
# like "//input[@name='email']" or "//input[@name='pass']".
elem = driver.find_element_by_name('email') # Or driver.find_element_by_xpath("//input[@name...")
elem.send_keys('username@usermail.com') # send the str input (username@...)
elem = driver.find_element_by_css_selector('li') # finds css element with specified tag (<li>)
elem = driver.find_element_by_css_selector('li').get_attribute('href') # finds css element with specified tag and get the value of specified attribute 
elem = driver.find_element_by_name('pass')
elem.send_keys('userpassword')
elem.send_keys(Keys.RETURN) # "Enter" key.
driver.close() # close method.

driver.execute_script('e.g. console.log("Hello World")') # to execute an script on the console.
# for more info: https://selenium-python.readthedocs.io/
