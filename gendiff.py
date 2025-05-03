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


def gendiff(file_path1, file_path2):
    file1_read = get_file_data(file_path1)
    file2_read = get_file_data(file_path2)
    all_keys = sorted(file1_read.keys() | file2_read.keys())
    
    diff = {}
    for key in all_keys:
        if key not in file1_read.keys():
            diff[key] = {
                'type': 'added',
                'value': file2_read[key]
            }
        elif key not in file2_read.keys():
            diff[key] = {
                'type': 'removed',
                'value': file1_read[key]
            }
        elif file1_read[key] != file2_read[key]:
            diff[key] = {
                'type': 'updated',
                'value_old': file1_read[key],
                'value_new': file2_read[key]
            }
        else:
            diff[key] = {
                'type': 'same',
                'value': file1_read[key]
            }
    return diff

def format(dict):
    list = []
    for key, item in dict.items():
        if item['type'] == 'added':
            list.append(f'  + {key}: {item['value']}')
        elif item['type'] == 'removed':
            list.append(f'  - {key}: {item['value']}')
        elif item['type'] == 'updated':
            list.append(f'  - {key}: {item['value_old']}')
            list.append(f'  + {key}: {item['value_new']}')
        else:
            list.append(f'  {key}: {item['value']}')

    return f"{{\n{'\n'.join(list)}\n}}"