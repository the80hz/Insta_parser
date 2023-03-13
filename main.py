from datetime import datetime
import re

from instagrapi import Client

import auth_data


def get_userid():
    client = Client()
    client.login(auth_data.username[1], auth_data.password[1])

    while True:
        # read lines in file
        with open('posts.csv', 'r') as f:
            lines = f.readlines()

        # get the post url
        post_url = lines[0].strip()

        # get the pk
        pk = client.media_pk_from_url(post_url)

        # get the user
        try:
            user = client.media_info(pk).user
        except Exception as e:
            if 'Media not found or unavailable' in str(e):
                print('Media not found or unavailable')
                with open('posts.csv', 'w') as f:
                    for line in lines[1:]:
                        f.write(line)
                continue
            else:
                raise e

        # write the str(user) to a file
        with open('users.csv.csv', 'a') as w:
            w.write(str(user) + '\n')

        # delete the first line in the file
        with open('posts.csv', 'w') as f:
            for line in lines[1:]:
                f.write(line)

        # print the time
        end = datetime.now().timestamp()
        print(f'{round(end - start, 2)} sec')


def get_postinfo(post_filename, info_filename):
    """
    Get post info from url in every line in file
    :param post_filename:
    :param info_filename:
    :return:
    """
    client = Client()
    client.login(auth_data.username[0], auth_data.password[0])

    while True:
        # read lines in file
        with open(post_filename, 'r', encoding='utf8') as f:
            lines = f.readlines()

        # get the post url
        post_url = lines[0].strip()

        # get the pk
        pk = client.media_pk_from_url(post_url)

        # get the post info
        try:
            post = client.media_info(pk)
            # write str(post) to a file
            with open(info_filename, 'a', encoding='utf8') as w:
                w.write(str(post) + '\n')

        except Exception as e:
            if 'Media not found or unavailable' in str(e):
                print('Media not found or unavailable')
                with open(post_filename, 'w') as f:
                    for line in lines[1:]:
                        f.write(line)
            else:
                raise e

        # delete the first line in the file
        with open(post_filename, 'w', encoding='utf8') as f:
            for line in lines[1:]:
                f.write(line)

        # print the time
        end = datetime.now().timestamp()
        print(f'{round(end - start, 2)} sec')


def get_userinfo(users_filename, info_filename):
    client = Client()
    client.login(auth_data.username[2], auth_data.password[2])

    while True:
        # read lines in file
        with open(users_filename, 'r', encoding='utf8') as f:
            lines = f.readlines()

        # get the username from the first line
        username = lines[0].strip()
        username = re.findall('https://www.instagram.com/(.*)/', username)[0]
        print(username)
        # get the user info
        try:
            userinfo = client.user_info_by_username(username)
            # write str(userinfo) to a file
            with open(info_filename, 'a', encoding='utf8') as w:
                w.write(str(userinfo) + '\n')

        except Exception as e:
            print(e)
            with open(users_filename, 'w') as f:
                for line in lines[1:]:
                    f.write(line)

        # delete the first line in the file
        with open(users_filename, 'w', encoding='utf8') as f:
            for line in lines[1:]:
                f.write(line)


if __name__ == '__main__':
    start = datetime.now().timestamp()
    get_userinfo('users.csv', 'info_userid.csv')
