import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import time
import math
#
# # @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
# #                                   'https://stepik.org/lesson/236896/step/1',
# #                                   'https://stepik.org/lesson/236897/step/1',
# #                                   'https://stepik.org/lesson/236898/step/1',
# #                                   'https://stepik.org/lesson/236899/step/1',
# #                                   'https://stepik.org/lesson/236903/step/1',
# #                                   'https://stepik.org/lesson/236904/step/1',
# #                                   'https://stepik.org/lesson/236905/step/1'])
def answer_f():
    answer = str(math.log(int(time.time())))
    return answer

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # browser = webdriver.Firefox()
    yield browser
    print('\nquit browser')
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_params(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)
    button_ent = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "navbar__auth_login")))
    button_ent.click()
    email = "melaniya.s2001@gmail.com"
    input_email = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.ID, "id_login_email")))
    input_email.send_keys(email)
    input_password= browser.find_element(By.ID, "id_login_password")
    password = "govno2001"
    input_password.send_keys(password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    try:
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, 'button.again-btn.white').click()
    except NoSuchElementException:
        print('textarea чистый, кнопку "решить снова" нажимать не надо')
    finally:
        time.sleep(5)
        answer = answer_f()
        text_area = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'ember-text-area')))
        text_area.send_keys(answer)
        button = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        button.click()
        response = WebDriverWait(browser,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        text = response.text
        assert text == 'Correct!', text




@pytest.mark.parametrize('urls', ['236895/step/1',
                                  '236896/step/1',
                                  '236897/step/1',
                                  '236898/step/1',
                                  '236899/step/1',
                                  '236903/step/1',
                                  '236904/step/1',
                                  '236905/step/1'
                                  ])
def test_get_link(browser, urls):
    link = f'https://stepik.org/lesson/{urls}'
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    input_email = browser.find_element(By.ID, 'id_login_email')
    input_email.send_keys('-')  # ваш email
    input_pass = browser.find_element(By.ID, 'id_login_password')
    input_pass.send_keys('-')  # ваш пароль
    button = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader')
    button.click()
    try:
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, 'button.again-btn.white').click()
    except NoSuchElementException:
        print('textarea чистый, кнопку "решить снова" нажимать не надо')
    finally:
        time.sleep(5)
        our_time = str(math.log(int(time.time())))
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(our_time)
        button_answer = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
        )
        button_answer.click()
        answer = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint'))
        ).text
        assert answer == 'Correct!', answer