import time
from concurrent.futures import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

                parse_username(_driver, hrefs, _filename_tag, _filename_users)
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


def parse_username(_driver: webdriver, _post_list: list, _filename_tag: str, _filename_users: str):
    """
    Opening posts in new tabs and parse username by need tag
    :param _driver: webdriver
    :param _post_list: list of posts
    :param _filename_tag: name of file with need tags
    :param _filename_users: name of file to write users
    :return: None
    """
    try:
        with ThreadPoolExecutor(max_workers=5) as executor:
            for post in _post_list:
                executor.submit(parse_username_by_tag, _driver, post, _filename_tag)

    except Exception as _ex:
        print(_ex)
        driver.close()


def parse_username_by_tag(_driver: webdriver, _post: str, _filename_tag: str, _filename_users: str):
    """
    Opening post in new tabs and if post have need tag, parse username
    :param _driver: webdriver
    :param _post: post url
    :param _filename_tag: name of file with need tags
    :param _filename_users: name of file to write users
    :return: None
    """
    try:
        _driver.execute_script(f"window.open('{_post}');")
        time.sleep(4)
        _driver.switch_to.window(_driver.window_handles[1])

        # get username
        username = _driver.find_element(By.XPATH, "//a[@class='FPmhX notranslate  _0imsa ']").text

        # get tags
        tags = _driver.find_elements(By.XPATH, "//a[@class='xil3i']")
        tags = [item.text for item in tags]

        # check tags
        with open(_filename_tag, "r") as file:
            need_tags = file.read().split("\n")

        if len(set(tags) & set(need_tags)) > 0:
            with open(_filename_users, "a") as file:
                file.write(f"{username}\n")

        _driver.close()
        _driver.switch_to.window(_driver.window_handles[0])

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
        parse_by_geo(driver, "110589025635590", "tags.csv", "users.csv")

    elif choice == 2:
        parse_by_file(driver, "posts.csv")
