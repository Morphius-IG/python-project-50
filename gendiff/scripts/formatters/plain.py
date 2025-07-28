def to_plain(data, parent_key=''):
    new_data = []
         
    for key, value in data.items():
        current_key = f'{parent_key}.{key}' if parent_key else key
        
        if isinstance(value, dict) and 'status' in value:            
            if value['status'] == 'nested':     
                new_data.append(to_plain(value['value'], current_key))
                
            elif value['status'] == 'added':
                val = format_value(value['value'])
                new_data.append(f"Property '{current_key}' was added with value: {val}")

            elif value['status'] == 'deleted':
                new_data.append(f"Property '{current_key}' was removed")

            elif value['status'] == 'changed':
                val_new, val_old = format_value((value['new'])), format_value((value['old']))
                new_data.append(f"Property '{current_key}' was updated. From {val_old} to {val_new}")
                
        elif isinstance(value, dict):
            new_data.append (f"Property '{current_key}' was added with value: [complex value]")

    return "\n" .join(new_data)


def format_value(value):
  if isinstance(value, dict):
      return '[complex value]'
      
  elif isinstance(value, bool):
      return str(value).lower()
  elif value is None:
      return 'null'
  elif isinstance(value, str):
      return f"'{value}'"
  else:
      return str(value)