"""
Getting user id from post
"""

import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

from auth_data import acc1 as acc

ALL_UNIQUE_POSTS = []


def auth(_driver: webdriver, _username: str, _password: str):
    """
    Authentication in instagram
    :param _driver: webdriver
    :param _username: username
    :param _password: password
    :return: None
    """
    try:
        _driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(random.randint(5, 7))

        username_input = _driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(_username)

        time.sleep(random.randint(1, 2))

        password_input = _driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(_password)

        password_input.send_keys(Keys.RETURN)

        time.sleep(random.randint(3, 5))

    except Exception as _ex:
        print(_ex)
        _driver.close()


def parse_from_post_link(_driver: webdriver, _input: str, _output: str):
    """
    Parse all info from post, open user page and get all info about user
    :param _driver: webdriver
    :param _input: file with post links
    :param _output: file with all info about users
    :return: None
    """
    try:
        while True:
            # read lines in file
            with open(_input, 'r') as f:
                lines = f.readlines()

            # get the post url
            post_url = lines[0].strip()
            post_url = post_url.replace('\n', '')
            print(post_url)

            _driver.get(f"{post_url}")
            time.sleep(random.randint(6, 10))

            # delete first line in file
            with open(_input, 'w') as f:
                f.writelines(lines[1:])
            time.sleep(random.randint(1, 2))

    except Exception as _ex:
        print(_ex)
        _driver.close()


def main():
    """
    Main function
    :return: None
    """
    try:
        options = webdriver.ChromeOptions()

        '''ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')'''

        '''options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")'''

        driver = webdriver.Chrome(options=options)

        # auth(driver, acc[0], acc[1])

        parse_from_post_link(driver, '213911969.csv', 'users_info.txt')

    except Exception as _ex:
        print(_ex)


if __name__ == "__main__":
    main()
