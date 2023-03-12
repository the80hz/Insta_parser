"""
Parsing google.com, search "site:Instagram.com "#tag1" "#tag2""
Writing result to file
"""

import time
import random
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from auth_data import username, password

ALL_UNIQUE_POSTS = []


def search_google(_driver: webdriver, _filename_posts: str,  _tag1: str, _tag2: str):
    """
    Search google.com with tag, (multiple pages)
    :param _driver: webdriver
    :param _filename_posts: filename with posts
    :param _tag1: tag1
    :param _tag2: tag2
    :return: None
    """
    _tag1 = _tag1.replace("#", "%23")
    _tag2 = _tag2.replace("#", "%23")
    for i in range(5):
        try:
            _driver.get(f"https://www.google.com/search?q=site%3AInstagram.com+%22{_tag1}%22+%22{_tag2}%22&filter=0"
                        f"&start={str((i - 0) * 10)}")
            time.sleep(random.randint(2, 4))

            posts = _driver.find_elements(By.CSS_SELECTOR, "div.g")
            for post in posts:
                link = post.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                if link not in ALL_UNIQUE_POSTS:
                    ALL_UNIQUE_POSTS.append(link)
                    with open(_filename_posts, "a") as file:
                        file.write(link + "\n")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/search")
    time.sleep(10)
    tag1 = "#prague"
    # enter tag1 in search
    search_input = driver.find_element(By.NAME, "q")
    search_input.clear()
    search_input.send_keys(f'site:Instagram.com "{tag1}"')
    search_input.send_keys(Keys.RETURN)
    time.sleep(random.randint(3, 5))
    # for every word in file "hashtags.csv" search google.com and change tag2
    with open("hashtags.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for tag2 in row:
                search_google(driver, "posts.csv", tag1, tag2)

    driver.close()
