"""
Getting userid from post
"""

import time
import random
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import instagrapi


def parse_user_selenium(_driver: webdriver, _input: str, _output: str):
    """
    Parse all info from user
    :param _driver: webdriver
    :param _input: file with post links
    :param _output: file with all info about users
    :return: None
    """
    try:
        while True:
            # read lines in file
            with open(_input, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # get the user url
            user_url = lines[0].strip()
            user_url = user_url.replace('\n', '')
            user_url = 'https://www.instagram.com/' + user_url + '/'
            print(user_url)

            _driver.get(f"{user_url}")

            # get location
            try:
                location = WebDriverWait(_driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619'
                                                    '.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r'
                                                    '.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq'
                                                    '.x1a2a7pz._aaqk._a6hd'))
                )
                location = location.text
            except Exception as _ex:
                location = ''

            # get username
            try:
                username = WebDriverWait(_driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "a.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s"
                                                    ".xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli"
                                                    ".x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz"
                                                    ".x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619"
                                                    ".x1ypdohk.x1i0vuye.xwhw2v2.xl56j7k.x17ydfre.x1f6kntn.x2b8uid"
                                                    ".xlyipyv.x87ps6o.x14atkfc.x1d5wrs8.x972fbf.xcfux6l.x1qhh985"
                                                    ".xm0m39n.xm3z3ea.x1x8b98j.x131883w.x16mih1h.xt7dq6l.xexx8yu"
                                                    ".x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xjbqb8w.x1n5bzlp.xqnirrm"
                                                    ".xj34u2y.x568u83.x3nfvp2"))
                )
                username = username.text
            except Exception as _ex:
                username = ''

            # get description
            try:
                description = WebDriverWait(_driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "h1._aacl._aaco._aacu._aacx._aad7._aade"))
                )
                description = description.text
            except Exception as _ex:
                description = ''

            # write info to csv
            with open(_output, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([username, location, description])

            print(username)

            time.sleep(random.randint(1, 2))

            # delete first line in file
            with open(_input, 'w', encoding='utf-8') as f:
                f.writelines(lines[1:])

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

            user = cl.user_info_by_username(user_url)
            with open(_output, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([user.username, user.account_type, user.biography, user.follower_count, user.following_count, user.address_street, user.business_category_name, user.business_contact_method, user.category, user.category_name, user.city_id, user.city_name, user.contact_phone_number, user.external_url, user.instagram_location_id, user.is_business, user.is_verified, user.media_count, user.public_email, user.public_phone_country_code, user.public_phone_number, user.zip, ])
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
    """try:
        options = webdriver.ChromeOptions()
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')

        driver = webdriver.Chrome(options=options)

        parse_user_selenium(driver, '110589025635590.csv', 'users_info.csv')
    except Exception as _ex:
        print(_ex)"""

    # api method
    try:
        parse_user_api('users_info.csv', 'users_info_extend.csv')
    except Exception as _ex:
        print(_ex)

if __name__ == "__main__":
    main()
