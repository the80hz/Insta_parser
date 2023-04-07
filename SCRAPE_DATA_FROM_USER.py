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
from fake_useragent import UserAgent
import instagrapi

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


def parse_user_selenium(_driver: webdriver, _input: str, _output: str):
    """
    Parse all info from user
    :param _driver: webdriver
    :param _input: csv file with post links
    :param _output: csv file with all info about users
    :return: None
    """
    try:
        with open(_input, 'r', encoding='utf-8') as f:
            count = 0
            lines = csv.reader(f)
            for line in lines:
                username = line[0]
                user_url = 'https://www.instagram.com/' + username + '/'
                _driver.get(f"{user_url}")

                # get fullname
                try:
                    fullname = WebDriverWait(_driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'span._aacl._aaco._aacw._aacx._aad7._aade'))
                    )
                    fullname = fullname.text
                except Exception as _ex:
                    fullname = ''

                # get category
                try:
                    category = WebDriverWait(_driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'div._aacl._aaco._aacu._aacy._aad6._aade'))
                    )
                    category = category.text
                except Exception as _ex:
                    category = ''

                # get bio
                try:
                    bio = WebDriverWait(_driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'h1._aacl._aaco._aacu._aacx._aad6._aade'))
                    )
                    bio = bio.text
                except Exception as _ex:
                    bio = ''

                # get website
                try:
                    website = WebDriverWait(_driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'div._aacl._aaco._aacw._aacz._aada._aade'))
                    )
                    website = website.text
                except Exception as _ex:
                    website = ''

                # write info to csv
                with open(_output, 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([username, fullname, line[1], category, bio, website, line[2]])

                count += 1

        # delete count first lines from _input
        with open(_input, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open(_input, 'w', encoding='utf-8') as f:
            for line in lines[count:]:
                f.write(line)

    except Exception as _ex:
        print(_ex)
        _driver.close()


def parse_user_api(_input: str, _output: str):
    """
    Parse all info from user by instagrapi
    :param _input:
    :param _output:
    :return:
    """
    # for every line in _input csv file get username, open it in api, get info and write it to _output csv file
    try:
        while True:
            # read lines in file
            with open(_input, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # get the user url
            line = lines[0].strip()
            line = line.replace('\n', '')
            user_url = line.split(',')[0]

            print(user_url)
            cl = instagrapi.Client()
            cl.login(account[0], account[1])
            user = cl.user_info_by_username(user_url).dict()
            with open(_output, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                # write all user values to csv file
                for key, value in user.items():
                    writer.writerow([key, value])
            time.sleep(2)

            # delete first line in file
            with open(_input, 'w', encoding='utf-8') as f:
                f.writelines(lines[1:])

    except IndexError:
        print('Done')

    except Exception as _ex:
        print(_ex)


def main():
    """
    Main function
    :return: None
    """

    # selenium method
    try:

        """options = webdriver.ChromeOptions()
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')"""
        driver = webdriver.Chrome("""options=options""")

        auth(driver, account[0], account[1])

        parse_user_selenium(driver, 'users_info.csv', 'users_info_extend.csv')
    except Exception as _ex:
        print(_ex)

    # api method
    """try:
        parse_user_api('users_info.csv', 'users_info_extend.csv')
    except Exception as _ex:
        print(_ex)"""


if __name__ == "__main__":
    main()
