from selenium import webdriver
import math
import time

browser = webdriver.Firefox()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    button = browser.find_element_by_css_selector(".btn")
    num1 = browser.find_element_by_css_selector('#input_value')
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    input_box = browser.find_element_by_css_selector('#answer')
    num1_value = int(num1.text)
    answer = str(math.log(abs(12*math.sin(num1_value))))
    input_box.send_keys(answer)
    checkbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button.click()
finally:
    time.sleep(20)
    browser.quit()
