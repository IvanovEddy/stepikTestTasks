import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()


a = ["https://stepik.org/lesson/236895/step/1",
     "https://stepik.org/lesson/236896/step/1",
     "https://stepik.org/lesson/236897/step/1",
     "https://stepik.org/lesson/236898/step/1",
     "https://stepik.org/lesson/236899/step/1",
     "https://stepik.org/lesson/236903/step/1",
     "https://stepik.org/lesson/236904/step/1",
     "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('url', a)
def test_correct_answer(browser, url):
    link = f"{url}"
    browser.get(link)
    answer = math.log(int(time.time()))
    answer_input = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
                                                   )
    answer_button = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission"))
                                                   )
    answer_input.send_keys(str(answer))
    answer_button.click()
    feedback_elm = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
                                                   )
    feedback_text = feedback_elm.text
    assert "Correct!" == feedback_text
