def item_added(key, value):
    return {
        'type': 'added',
        'name': key,
        'value_new': value
    }

def item_removed(key, value):
    return {
        'type': 'removed',
        'name': key,
        'value_old': value
    }

def item_updated(key, value1, value2):
    return {
        'type': 'updated',
        'name': key,
        'value_old': value1,
        'value_new': value2
    }

def item_unchanged(key, value):
    return {
        'type': 'same',
        'name': key,
        'value': value
    }


def find_diff(data1, data2):
    keys_union = data1.keys() | data2.keys()
    keys_added = data2.keys() - data1.keys()
    keys_deleted = data1.keys() - data2.keys()

    diff = []

    for key in keys_union:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in keys_added:
            diff.append(item_added(key, value2))
        elif key in keys_deleted:
            diff.append(item_removed(key, value1))
        elif value1 != value2:
            diff.append(item_updated(key, value1, value2))
        else:
            diff.append(item_unchanged(key, value1))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff