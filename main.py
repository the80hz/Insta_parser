import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from auth_data import username, password

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
        time.sleep(6)

        username_input = _driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(_username)

        password_input = _driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(_password)

        password_input.send_keys(Keys.RETURN)
        time.sleep(6)

    except Exception as _ex:
        print(_ex)
        driver.close()


def parse_by_geo(_driver: webdriver, _geotag: str):
    """
    Parse posts by geotag and open them in new tabs, then parse username by parse_username function
    :param _driver: webdriver
    :param _geotag: geotag
    :return: None
    """
    try:
        _driver.get(f"https://www.instagram.com/explore/locations/{_geotag}/")
        time.sleep(6)

        while True:
            try:
                _driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)
                hrefs = _driver.find_elements(By.XPATH, "//a[@href]")
                hrefs = [item.get_attribute("href") for item in hrefs]
                hrefs = [item for item in hrefs if "/p/" in item]
                hrefs = list(set(hrefs))
                hrefs = [item for item in hrefs if item not in ALL_UNIQUE_POSTS]
                ALL_UNIQUE_POSTS.extend(hrefs)
                print(f"Posts: {len(hrefs)}")
                print(hrefs)
                parse_username(_driver, hrefs, "tags.csv")
                time.sleep(4)

            except Exception as _ex:
                print(_ex)
                break

    except Exception as _ex:
        print(_ex)
        driver.close()


def parse_by_file(_driver: webdriver, _file: str):
    """
    Parse posts by the file
    :param _driver: webdriver
    :param _file: file
    :return: None
    """
    pass


def parse_username(_driver: webdriver, _post_list: list, _filename_tag: str):
    """
    Parse username by
    :param _driver: webdriver
    :param _post_list: list of posts
    :param _filename_tag: name of file with need tags
    :return: None
    """
    pass


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

    if choice == 1:
        parse_by_geo(driver, "110589025635590")

    elif choice == 2:
        parse_by_file(driver, "posts.csv")
