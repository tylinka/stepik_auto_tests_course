from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    input3.send_keys("www@asdf.com")

    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.first")
    input4.send_keys("+995123123123")

    input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.second")
    input5.send_keys("Earth")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла