from selenium import webdriver
import time, math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


""" 
    В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
    
    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и 
    отправить решение
    
    Чтобы определить момент, когда цена аренды уменьшится до $100, 
    используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
    https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
"""
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def main():
    try:
        browser = webdriver.Chrome()
        # открыть траницу
        browser.get("http://suninjuly.github.io/explicit_wait2.html")


        # дождаться когда цена уменьшится до 100
        button = browser.find_element_by_id("book")
        wait = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), r"$100"))
        button.click()

        # читать значение для переменной x
        x_element = browser.find_element_by_id("input_value")
        x = int(x_element.text)

        # Посчитать математическую функцию от x
        result = calc(x)

        # Ввести ответ в текстовое поле
        pole = browser.find_element_by_css_selector("[id='answer']")
        pole.send_keys(result)

        # Нажать на кнопку Submit
        button = browser.find_element_by_css_selector("[type='submit']").click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()



if __name__ == "__main__":
    main()

# не забываем оставить пустую строку в конце файла
