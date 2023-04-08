"""
Getting userid from post
"""

import time
import random
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from auth_data import acc3 as account


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


def parse_similar_users(_driver: webdriver, _input: str, _output: str):
    """
    Parse similar users
    :param _driver: webdriver
    :param _input: csv file with favorite users
    :param _output: csv file with similar users
    :return: None
    """
    try:
        with open(_input, 'r', encoding='utf-8') as f:
            lines = csv.reader(f)
            for line in lines:
                username = line[0]
                print(username)
                user_url = 'https://www.instagram.com/' + username + '/'
                _driver.get(f"{user_url}")

                time.sleep(random.randint(3, 5))

                # click on follow button
                try:
                    follow_button = WebDriverWait(_driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button._acan._acap._acas._aj1-"))
                    )
                    follow_button.click()
                except Exception as _ex:
                    print(_ex)


                # find all div._aacl._aaco._aacw._aacx._aada
                try:
                    similar_users = WebDriverWait(_driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                             'div._aacl._aaco._aacw._aacx._aada'))
                    )
                except Exception as _ex:
                    similar_users = []
                    print(_ex)


                # write similar users to csv
                with open(_output, 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    for user in similar_users:
                        writer.writerow([user.text])

                # write info to csv
                with open(_output, 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([username])

    except Exception as _ex:
        print(_ex)
        _driver.close()


def main():
    """
    Main function
    :return: None
    """

    # selenium method
    try:
        driver = webdriver.Chrome()

        auth(driver, account[0], account[1])

        parse_similar_users(driver, 'users_info_fav.csv', 'usernames_similar.csv')
    except Exception as _ex:
        print(_ex)


if __name__ == "__main__":
    main()
