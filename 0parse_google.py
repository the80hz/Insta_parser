"""
Parsing google.com, search "site:Instagram.com "#tag1" "#tag2""
Writing result to file
"""

import time
import random
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

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

    try:
        _driver.get(f"https://www.google.com/search?q=site%3AInstagram.com+%22{_tag1}%22+%22{_tag2}%22&filter=0")
        time.sleep(2)
        links = _driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            if href not in ALL_UNIQUE_POSTS:
                ALL_UNIQUE_POSTS.append(href)
                with open(_filename_posts, "a", encoding='utf-8') as _file:
                    _file.write(href + "\n")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    tag1 = "prague"
    with open('google_csv/tags.csv', "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for tag2 in row:
                print(tag2)
                options = Options()
                ua = UserAgent()
                userAgent = ua.random
                print(userAgent)
                options.add_argument(f'user-agent={userAgent}')
                driver = webdriver.Chrome(options=options)
                search_google(driver, "google_csv/posts_g.csv", tag1, tag2)

    driver.close()
