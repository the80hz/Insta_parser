from instagrapi import Client
from datetime import datetime
import auth_data


def main():
    client = Client()
    client.login(auth_data.username[1], auth_data.password[1])

    while True:
        # read first line in file
        post_url = open('posts.csv', 'r').readline()
        # get the pk
        pk = client.media_pk_from_url(post_url)
        # get the user
        # if MediaNotFound error, then delete the first line in the file
        try:
            user = client.media_info(pk).user  # type: ignore
        except:
            with open('posts.csv', 'r') as f:
                lines = f.readlines()
            with open('posts.csv', 'w') as f:
                for line in lines[1:]:
                    f.write(line)
            continue

        # write the str(user) to a file
        with open('users.txt', 'a') as w:
            w.write(str(user) + '\n')
        # delete the first line in the file
        with open('posts.csv', 'r') as f:
            lines = f.readlines()
        with open('posts.csv', 'w') as f:
            for line in lines[1:]:
                f.write(line)
        # print the time
        end = datetime.now().timestamp()
        print(f'{round(end - start, 2)} sec')


if __name__ == '__main__':
    start = datetime.now().timestamp()
    main()
