import argparse, json

def get_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    return parser.parse_args()


def get_file_data(file_path):
    return json.load(open(file_path))