import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from auth_data import username, password


def auth(_driver, _username, _password):
    _driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(6)

    username_input = _driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(_username)

    password_input = _driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(_password)

    password_input.send_keys(Keys.RETURN)
    time.sleep(6)


if __name__ == "__main__":
    while True:
        try:
            choice = int(input("1 - Parse new posts \n2 - Parse from file\n"))
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


