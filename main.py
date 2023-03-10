from instagrapi import Client
from datetime import datetime
import auth_data


def main():
    client = Client()
    client.login(auth_data.username, auth_data.password)

    with open('posts.csv', 'r') as f:
        for line in f:
            # get the url
            url = line.split(',')[0]
            # get the pk
            pk = client.media_pk_from_url(url)
            # get the user
            user = client.media_user(pk)

            # write the str(user) to a file
            with open('users_1.txt', 'a') as w:
                w.write(str(user) + '\n')

            end = datetime.now().timestamp()
            print(f'{round(end - start, 2)} sec')

    client.logout()


if __name__ == '__main__':
    start = datetime.now().timestamp()
    main()
