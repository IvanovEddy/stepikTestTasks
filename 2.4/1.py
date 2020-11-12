from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
    btn1 = browser.find_element_by_css_selector("#book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn1.click()
    num1 = browser.find_element_by_css_selector('#input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", num1)
    num1_value = int(num1.text)
    answer = str(math.log(abs(12 * math.sin(num1_value))))
    input_box = browser.find_element_by_css_selector('#answer')
    input_box.send_keys(answer)
    btn2 = browser.find_element_by_css_selector('#solve')
    btn2.click()
finally:
    time.sleep(20)
    browser.quit()
