"""
Scrape posts from an instagram by geotag
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


def parse_by_geo(_driver: webdriver, _geotag: str, _filename_tag: str):
    """
    Parse posts by a geotag
    :param _driver: webdriver
    :param _geotag: geotag
    :param _filename_tag: name of file with need tags
    :return: None
    """
    try:
        _driver.get(f"https://www.instagram.com/explore/locations/{_geotag}/")
        time.sleep(random.randint(6, 10))

        while True:
            try:
                _driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(6, 8))

                hrefs = _driver.find_elements(By.XPATH, "//a[@href]")
                hrefs = [item.get_attribute("href") for item in hrefs]
                hrefs = [item for item in hrefs if "/p/" in item]
                hrefs = list(set(hrefs))
                hrefs = [item for item in hrefs if item not in ALL_UNIQUE_POSTS]
                with open(_filename_tag, "a", encoding='utf-8') as _file:
                    _file.write("\n".join(hrefs) + "\n")
                ALL_UNIQUE_POSTS.extend(hrefs)
                print(f"Sum: {len(ALL_UNIQUE_POSTS)}")
                print(f'New hrefs: {hrefs}')

            except Exception as _ex:
                print(_ex)
                break

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

        auth(driver, acc[0], acc[1])
        # 110589025635590 prague
        # 458937378003687 prague
        # 1953015018347533 prague
        # 213911969 plzen
        # 244516490 czech
        # 213262221 brno
        # 321962471320334 brno
        # 213641007 karlovy-vary
        # 360543173 karlovy-vary-district
        parse_by_geo(driver, "213911969", "tags.csv")

    except Exception as _ex:
        print(_ex)


if __name__ == "__main__":
    main()
