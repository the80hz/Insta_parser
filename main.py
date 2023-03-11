import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from auth_data import username, password


def get_posts_by_geo(_geotag, _filename, _browser):
    try:
        _browser.get(
            f'https://www.instagram.com/explore/locations/{_geotag}/')
        time.sleep(5)

        while True:
            _browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

            hrefs = _browser.find_elements(By.TAG_NAME, 'a')
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
            posts_urls = list(set(posts_urls))

            with open(_filename, 'w') as file:
                for url in posts_urls:
                    file.write(url + '\n')
            print(f'Found {len(posts_urls)} posts')

    except Exception as ex:
        print(ex)
        _browser.close()
        _browser.quit()


def get_users_by_posts(_filename, _users_filename, _browser):
    try:
        with open(_filename, 'r') as file:
            posts_urls = file.read().splitlines()

        users = []
        for url in posts_urls:
            try:
                _browser.get(url)
                time.sleep(10)
                hrefs = _browser.find_elements(By.TAG_NAME, 'a')
                all_links = [item.get_attribute('href') for item in hrefs]
                users.append(all_links[11])
                time.sleep(random.randrange(80, 100))
            except Exception as ex:
                print(ex)

        with open(_users_filename, 'w') as file:
            for user in users:
                file.write(user + '\n')

    except Exception as ex:
        print(ex)
        _browser.close()
        _browser.quit()


def main(_username, _password, geotag, posts_filename, users_filename):
    browser = webdriver.Chrome('../chromedriver/chromedriver')
    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(5, 10))

        username_input = browser.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(_username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(_password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # get posts by geotag
        # get_posts_by_geo(geotag, posts_filename, browser)

        # get users by posts
        get_users_by_posts(posts_filename, users_filename, browser)

        browser.close()
        browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


if __name__ == '__main__':
    main(username[0], password[0], '110589025635590', 'posts.csv', 'users.txt')
