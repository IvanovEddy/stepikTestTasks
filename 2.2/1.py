from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)
    num1 = browser.find_element_by_css_selector('#num1')
    num1_value = int(num1.text)
    num2 = browser.find_element_by_css_selector('#num2')
    num2_value = int(num2.text)
    sum1_2 = str(num2_value+num1_value)
    select = Select(browser.find_element_by_css_selector('select'))
    select.select_by_value(sum1_2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
