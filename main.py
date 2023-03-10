from instagrapi import Client
from datetime import datetime

import auth_data


def main():
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
        with open('users.txt', 'a') as w:
            w.write(str(user) + '\n')

        # delete the first line in the file
        with open('posts.csv', 'w') as f:
            for line in lines[1:]:
                f.write(line)

        # print the time
        end = datetime.now().timestamp()
        print(f'{round(end - start, 2)} sec')


if __name__ == '__main__':
    start = datetime.now().timestamp()
    main()
