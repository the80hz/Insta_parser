import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from auth_data import username, password


def hashtag_search(_username, _password, _geotag, _file):
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

        try:

            browser.get(
                f'https://www.instagram.com/explore/locations/{_geotag}/')
            time.sleep(5)

            while True:
                browser.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

                hrefs = browser.find_elements(By.TAG_NAME, 'a')
                posts_urls = [item.get_attribute(
                    'href') for item in hrefs if "/p/" in item.get_attribute('href')]
                for url in posts_urls:
                    _file.write(url)
                    _file.write("\n")

            links = []
            for url in posts_urls:
                try:
                    browser.get(url)
                    time.sleep(10)
                    hrefs = browser.find_elements(By.TAG_NAME, 'a')
                    # like_button = browser.find_element(By.CLASS_NAME, "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _acan _acao _acat _acaw _aj1- _a6hd")
                    all_links = [item.get_attribute('href') for item in hrefs]
                    links.append(all_links[11])
                    # time.sleep(random.randrange(80, 100))
                except Exception as ex:
                    print(ex)
            print(links)

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


file = open("posts.csv", "a")
hashtag_search(username[0], password[0], '110589025635590', file)
file.close()
