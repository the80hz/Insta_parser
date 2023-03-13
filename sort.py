import csv
import re


if __name__ == '__main__':
    input_file = 'instagrapi_csv/info.csv'
    output_file = 'instagrapi_csv/packed.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['username', 'full_name'])

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            hashtags = re.findall(r"#(\w+)", line)
            if hashtags:
                hashtags = ', '.join(hashtags)
            else:
                hashtags = None
            username = re.search(r"username='(.+?)'", line)
            full_name = re.search(r"full_name='(.+?)'", line)
            if username:
                username = username.group(1)
            if full_name:
                full_name = full_name.group(1)
            if full_name == "', profile_pic_url=HttpUrl(":
                full_name = None

            with open(output_file, 'a', newline='', encoding='utf-8') as _f:
                writer = csv.writer(_f, delimiter=',')
                writer.writerow([username, full_name])


