"""
Parsing instagram by geotag or file with posts

1. Authentication in instagram
2. Parse posts by geotag or file with posts
3. Parse username by tag
"""


import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from auth_data import username, password

ALL_UNIQUE_POSTS = []


def search_tag(tags_akk, tags):
    for tag in tags_akk:
        if tag in tags:
            return True
    return False


def filter(akks):
    file = open("tags.csv", "r")
    groups = []
    for row in file.readlines():
        groups.append(row.replace("\n", ""))
    file.close()
    result = {}
    for group in groups:
        item = []
        for ak in akks:
            if search_tag(akks[ak], group):
                item.append(ak)
        result[group] = item
    return result


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

        password_input = _driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(_password)

        password_input.send_keys(Keys.RETURN)
        time.sleep(random.randint(3, 5))

    except Exception as _ex:
        print(_ex)
        driver.close()


def parse_by_geo(_driver: webdriver, _geotag: str, _filename_tag: str, _filename_users: str):
    """
    Parse posts by geotag, getting unique and then parse username by parse_username() function
    :param _driver: webdriver
    :param _geotag: geotag
    :param _filename_tag: name of file with need tags
    :param _filename_users: name of file to write users
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
                ALL_UNIQUE_POSTS.extend(hrefs)

                print(f"Posts: {len(hrefs)}")
                print(hrefs)

                parse_username_by_tag(_driver, hrefs, _filename_tag, _filename_users)

            except Exception as _ex:
                print(_ex)
                break

    except Exception as _ex:
        print(_ex)
        driver.close()


def parse_by_file(_driver: webdriver, _filename_posts: str, _filename_tag: str, _filename_users: str):
    """
    Parse posts by the file
    :param _driver: webdriver
    :param _filename_posts: file
    :param _filename_tag: name of file with need tags
    :param _filename_users: name of file to write users
    :return: None
    """
    try:
        while True:
            # read lines in file
            with open(_filename_posts, 'r') as f:
                lines = f.readlines()

            # get the post url
            post_url = lines[0].strip()
            post_url = post_url.replace('\n', '')
            print(post_url)

            # parse username by tag
            parse_username_by_tag(_driver, [post_url], _filename_tag, _filename_users)

            # delete first line in file
            with open(_filename_posts, 'w') as f:
                f.writelines(lines[1:])
            time.sleep(random.randint(1, 2))

    except Exception as _ex:
        print(_ex)
        driver.close()


def parse_username_by_tag(_driver: webdriver, _posts: list, _filename_tag: str, _filename_users: str):
    """
    Opening post in new tabs and if post have need tag, parse username
    :param _driver: webdriver
    :param _posts: list of posts or one post with url
    :param _filename_tag: name of file with need tags
    :param _filename_users: name of file to write users
    :return: None
    """
    accounts = {}
    for post in _posts:
        try:
            time.sleep(random.randint(1, 2))
            _driver.execute_script(f"window.open('{post}');")
            time.sleep(random.randint(10, 15))
            _driver.switch_to.window(_driver.window_handles[1])

            link = driver.find_elements(By.TAG_NAME, "a")
            tags = [item.text for item in link if "/tags/" in item.get_attribute('href')]
            all_tag = []
            for tag in tags:
                all_tag.append(tag.replace("#", ""))

            # for i in link:
                # print(i.get_attribute('href'))

            _username = link[11].text

            _driver.close()
            _driver.switch_to.window(_driver.window_handles[0])

            accounts[_username] = all_tag

            with open(_filename_users, 'a', encoding='utf-8') as _file:
                _file.write(_username)
                _file.write(",")
                _file.write(",".join(all_tag))
                _file.write("\n")

        except Exception as _ex:
            print(_ex)
            driver.close()


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
        parse_by_geo(driver, "110589025635590", "instagrapi_csv/hashtags.csv", "instagrapi_csv/users.csv")

    elif choice == 2:
        parse_by_file(driver, "instagrapi_csv/posts.csv", "instagrapi_csv/hashtags.csv", "instagrapi_csv/users.csv")
