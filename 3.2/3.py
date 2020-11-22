from selenium import webdriver
import time
import unittest


class RegistrationTest(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Firefox()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element_name = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        element_name.send_keys("111")
        element_last_name = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        element_last_name.send_keys("111")
        element_email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        element_email.send_keys("111")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Firefox()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element_name = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        element_name.send_keys("111")
        element_last_name = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        element_last_name.send_keys("111")
        element_email = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        element_email.send_keys("111")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
