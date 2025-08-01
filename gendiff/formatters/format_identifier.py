from gendiff.formatters.json import format_diff_json
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.stylish import format_diff_stylish


def format_identifier(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)
    if formatter == 'json':
        return format_diff_json(diff)
    if formatter == 'plain':
        return format_diff_plain(diff)
    else:
        raise ValueError(f"Unsupported formatter: {formatter}")