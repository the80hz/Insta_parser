import csv
import re


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
            s2 = re.findall(r'https://www.instagram.com/\S{1,}/', line)
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


if __name__ == "__main__":
    make_url("google_csv/posts_g.csv", "google_csv/posts_g2s.csv")
    unique("google_csv/posts_g2s.csv")

