import time
from selenium import webdriver

options = webdriver.ChromeOptions()

# https://stackoverflow.com/q/24999318/selenium-use-chromium-instead-of-google-chrome
options.binary_location = "/usr/bin/chromium"

# https://blog.miguelgrinberg.com/post/using-headless-chrome-with-selenium
options.add_argument("headless")

# https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome(options=options)
driver.get('http://www.google.com/');
time.sleep(1)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(1)
driver.quit()