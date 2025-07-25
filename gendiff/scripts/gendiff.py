import argparse

from gendiff.scripts.gendiff_script import generate_diff


def get_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str, help='set format of output', default='stylish')
    return parser.parse_args()


def main():
    args = get_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    result = generate_diff(file_path1, file_path2, formatter=args.format)
    print(result)


if __name__ == "__main__":
    main()