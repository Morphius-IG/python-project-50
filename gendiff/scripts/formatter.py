def to_stylish(data, replacer=' ', spacesCount=4, depth=1):
    if not isinstance(data, dict):
        return str(data)
        
    inner_indent = replacer * spacesCount
    new_data = []
    for key, value in data.items():
        if isinstance(value, dict) and 'status' in value:
            if value['status'] == 'parent':
                inner_indent = (replacer * spacesCount * depth)
                new_data.append(
                  f"{inner_indent}{str(key)}: {str(to_stylish(value['value'], 
                  replacer, spacesCount, depth + 1))}"
                  )

            if value['status'] == 'added':
                inner_indent = replacer * (spacesCount * depth - 2) + '+ '
                new_data.append(
                  f"{inner_indent}{str(key)}: {str(to_stylish(value['value'], 
                  replacer, spacesCount, depth + 1))}")

            if value['status'] == 'deleted':
                inner_indent = replacer * (spacesCount * depth - 2) + '- '
                new_data.append(
                  f"{inner_indent}{str(key)}: {str(to_stylish(value['value'], 
                  replacer, spacesCount, depth + 1))}")

            if value['status'] == 'changed':
                inner_indent = replacer * (spacesCount * depth - 2) + '- '
                new_data.append(
                  f"{inner_indent}{str(key)}: {str(to_stylish(value['old'], 
                  replacer, spacesCount, depth + 1))}")
                inner_indent = replacer * (spacesCount * depth - 2) + '+ '
                new_data.append(
                  f"{inner_indent}{str(key)}: {str(to_stylish(value['new'], 
                  replacer, spacesCount, depth + 1))}")
                
            if value['status'] == 'not changed':
                inner_indent = (replacer * spacesCount * depth)
                new_data.append(
                  f"{inner_indent}{str(key)}: {str(to_stylish(value['value'], 
                  replacer, spacesCount, depth + 1))}")   
        else:
            inner_indent = (replacer * spacesCount * depth)
            new_data.append(
              f'{inner_indent}{str(key)}: {str(to_stylish(value, 
              replacer, spacesCount, depth + 1))}')

    if depth == 0:
        return "{\n" + "\n".join(new_data) + "\n}"
    else:
        return (
            "{\n" 
            + "\n".join(new_data) 
            + "\n" 
            + replacer * (spacesCount * depth - 4) 
            + "}"
        )