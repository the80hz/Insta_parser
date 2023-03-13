import re
import pandas as pd
import csv


def make_url(_input: str, _output: str):
    """
    Read every line from file and make need url
    :param _input: input file
    :param _output: output file
    :return: None
    """
    with open(_input, "r", encoding='utf-8') as file:
        reader = file.readlines()
        for line in reader:
            line = line.replace("secure.", "")
            # write only https://www.instagram.com/p/\S{11}/
            s1 = re.findall(r'https://www.instagram.com/\S{1,2}/\S{11}/', line)
            s2 = re.findall(r'https://www.instagram.com/\S+/', line)
            if s1:
                line = s1[0]
            elif s2:
                line = s2[0]
            else:
                continue

            with open(_output, "a", encoding='utf-8') as _file:
                _file.write(line)
                _file.write("\n")


def unique(_input: str):
    """
    Delete duplicates from file
    :param _input: input file
    :return: None
    """
    with open(_input, "r", encoding='utf-8') as file:
        reader = file.readlines()
        unique_list = list(set(reader))
        unique_list.sort()
        with open(_input, "w", encoding='utf-8') as _file:
            for line in unique_list:
                _file.write(line)


def pack_to_csv_posts(input_f, output_f):
    data = pd.DataFrame(columns=['username', 'full_name', 'hashtags', 'location'])

    with open(input_f, 'r', encoding='utf-8') as f:
        for line in f:
            hashtags = re.findall(r"#(\w+)", line)
            if hashtags:
                hashtags = ', '.join(hashtags)
            else:
                hashtags = ''

            username = re.search(r"username='(.+?)'", line)
            if username:
                username = username.group(1)

            full_name = re.search(r"full_name='(.+?)'", line)
            if full_name:
                full_name = full_name.group(1)
            if full_name == "', profile_pic_url=HttpUrl(":
                full_name = None

            location = re.search(r"Location\((.+?)\)", line)
            if location:
                location = location.group(1)

            if username in data['username'].values:
                data.loc[data['username'] == username, 'hashtags'] += ', ' + hashtags
            else:
                data = data.append({'username': username, 'full_name': full_name, 'hashtags': hashtags,
                                    'location': location}, ignore_index=True)

    data.to_csv(output_f, mode='a', index=False, header=False)


def pack_to_csv_users(input_f, output_f):
    data = pd.DataFrame(columns=['username', 'full_name', 'biography', 'address_street', 'city_name'])
    with open(input_f, 'r', encoding='utf-8') as f:
        for line in f:
            username = re.search(r"username='(.+?)'", line)
            if username:
                username = username.group(1)

            full_name = re.search(r"full_name='(.+?)'", line)
            if full_name:
                full_name = full_name.group(1)
            if full_name == "', profile_pic_url=HttpUrl(":
                full_name = None

            biography = re.search(r"biography='(.+?)'", line)
            if biography:
                biography = biography.group(1)

            address_street = re.search(r"address_street='(.+?)'", line)
            if address_street:
                address_street = address_street.group(1)

            city_name = re.search(r"city_name='(.+?)'", line)
            if city_name:
                city_name = city_name.group(1)

            with open(output_f, 'a', encoding='utf-8') as _file:
                print(f'"{username}","{full_name}","{biography}","{address_street}","{city_name}"')
                _file.write(f'"{username}","{full_name}","{biography}","{address_street}","{city_name}"')
                _file.write('\n')





def find_prague(input_f, output_f):
    """
    find lines with prague or прага words
    """
    count = 0
    with open(input_f, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if 'prague' in line.lower() or 'прага' in line.lower():
                with open(output_f, 'a', encoding='utf-8') as _file:
                    _file.write(line)
                    count += 1
    print(count)


if __name__ == '__main__':
    # make_url("google_csv/posts_g.csv", "google_csv/posts_g2s.csv")

    # unique("google_csv/posts_g2s.csv")

    # pack_to_csv_posts('google_csv/info.csv', 'instagrapi_csv/packed.csv')
    # pack_to_csv_users('info_userid.csv', 'instagrapi_csv/packed.csv')

    find_prague('instagrapi_csv/packed.csv', 'instagrapi_csv/right.csv')
