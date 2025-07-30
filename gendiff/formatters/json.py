def to_json(data, replacer=' ', spacesCount=4, depth=1):
    if not isinstance(data, dict):
        return format_value(data)

    inner_indent = replacer * spacesCount
    new_data = []
    for key, value in data.items():
        inner_indent = (replacer * spacesCount * depth)
        if isinstance(value, dict) and 'parent' in value:
            new_data.append(
              f'{inner_indent}"{str(key)}": {str(to_json(value["value"], 
              replacer, spacesCount, depth + 1))}')

        else:
            new_data.append(
              f'{inner_indent}"{str(key)}": {str(to_json(value, 
              replacer, spacesCount, depth + 1))},')
    indent = replacer * (spacesCount * depth - 4)
    if depth == 0:
        text = "{\n" + "\n".join(new_data) + "\n}"
    else:
        text = (
            "{\n" 
            + "\n".join(new_data) 
            + "\n" 
            + indent 
            + "}"
        )
    old_pattern = f',\n{indent}}}'
    new_pattern = f'\n{indent}}}'
    new_text = text.replace(old_pattern, new_pattern)   
    return new_text 


def format_value(value):   
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f'"{value}"'
    else:
        return str(value)