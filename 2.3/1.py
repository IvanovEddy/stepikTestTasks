from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    btn1 = browser.find_element_by_css_selector('.btn')
    btn1.click()
    alert = browser.switch_to.alert
    alert.accept()
    WebDriverWait(browser, 10).until(
        EC.title_is('Alert redirect')
    )
    num1 = browser.find_element_by_css_selector('#input_value')
    num1_value = int(num1.text)
    answer = str(math.log(abs(12 * math.sin(num1_value))))
    input_box = browser.find_element_by_css_selector('#answer')
    input_box.send_keys(answer)
    btn2 = browser.find_element_by_css_selector('.btn')
    btn2.click()
finally:
    time.sleep(20)
    browser.quit()