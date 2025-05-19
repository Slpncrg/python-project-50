from pathlib import Path

from gendiff import format, gendiff

DIR_FILE = Path(__file__).parent / 'tests' / 'fixtures'


def main():    
    diff = gendiff(DIR_FILE / 'file1.json', DIR_FILE / 'file2.json')
    format_diff = format(diff)
    print(format_diff)


if __name__ == "__main__":
	main()