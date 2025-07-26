def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def create_plain_item(item, path=''):
    key = item.get('name')
    action = item.get('type')
    value_old = format_value(item.get('value_old'))
    value_new = format_value(item.get('value_new'))
    current_path = f"{path}.{key}" if path else key

    ADD = ' was added with value: '
    REMOVE = ' was removed'
    UPD = ' was updated. From '
    UPD_TO = ' to '
    PROP = 'Property '

    if action == 'added':
        return f"{PROP}'{current_path}'{ADD}{value_new}"
    if action == 'removed':
        return f"{PROP}'{current_path}'{REMOVE}"
    if action == 'updated':
        return f"{PROP}'{current_path}'{UPD}{value_old}{UPD_TO}{value_new}"
    if action == 'nested':
        children = item.get('children')
        return make_plain_diff(children, current_path)
    return None


def make_plain_diff(diff, path=''):
    result = []
    for item in diff:
        formatted_item = create_plain_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(diff):
    return make_plain_diff(diff)