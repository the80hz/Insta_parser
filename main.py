import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from auth_data import username, password


def auth(driver, _username, _password):
    # Авторизация
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(random.randrange(2, 4))

    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(_username)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(_password)

    password_input.send_keys(Keys.RETURN)

    time.sleep(random.randrange(2, 4))


if __name__ == "__main__":
    # что вы хотите сделать 1 - спарсить новые посты, 2 - спарсить посты из файла
    while True:
        try:
            choice = int(input("Что вы хотите сделать? \n1 - спарсить новые посты \n2 - спарсить посты из файла: \n"))
            if choice == 1:
                break
            elif choice == 2:
                break
            else:
                print("Неверный ввод")
        except Exception as ex:
            print(ex)

    # auth
    driver = webdriver.Chrome()
    auth(driver, username[0], password[0])
