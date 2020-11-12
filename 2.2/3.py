from selenium import webdriver
import os
import time

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys("111")
    surname = browser.find_element_by_css_selector('[name="lastname"]')
    surname.send_keys("222")
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("333")
    send_file = browser.find_element_by_css_selector('[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'tt.txt')
    send_file.send_keys(file_path)
    button = browser.find_element_by_css_selector('.btn')
    button.click()
finally:
    time.sleep(20)
    browser.quit()