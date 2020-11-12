from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
link = "https://ya.ru/"
browser.get(link)

input_ya = browser.find_element_by_css_selector("#text")
input_ya.send_keys("Анастасия Костяева")
button = browser.find_element_by_css_selector('.mini-suggest__button')
button.click()
wait = WebDriverWait(browser,10)
time.sleep(0.1)
link_VK = browser.find_element_by_xpath('//*[contains(text(), "Поиск людей")]')
link_VK.click()