from gendiff import get_args, get_file_data, gendiff, format
def main():    
    #args = get_args()
    file_data = get_file_data('./files/file1.json')
    diff = gendiff('./files/file1.json', './files/file2.json')
    format_diff = format(diff)
    print(format_diff)


if __name__ == "__main__":
	main()