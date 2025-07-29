from gendiff.scripts.parser import parse_files


def generate_diff(file1, file2):
    if not isinstance(file1, dict) and not isinstance(file2, dict):
        new_file1, new_file2 = parse_files(file1, file2)
    else:
        new_file1, new_file2 = file1, file2
    
    merged_keys = sorted({*new_file1.keys(), *new_file2.keys()})
    diff = {}
    for key in merged_keys:
        if (
            key in new_file2
            and key in new_file1
            and isinstance(new_file1[key], dict)
            and isinstance(new_file2[key], dict)
        ):
            diff[key] = {'status': 'nested', 
                         'value': generate_diff(new_file1[key], new_file2[key])}
        else:
            # Если текущего ключа нету в изначальном варианте
            if key not in new_file1: 
                # значит его добавили
                diff[key] = {'status': 'added', 'value': new_file2[key]}
                # Если текущего ключа нету в конечном варианте 
            elif key not in new_file2:
                # значит его удалили
                diff[key] = {'status': 'deleted', 'value': new_file1[key]}
                # Если значения ключей отличаются  
            elif new_file1[key] != new_file2[key]:  
                
                diff[key] = {'status': 'changed', 
                             'old': new_file1[key], 
                             'new': new_file2[key]}
            elif new_file1[key] == new_file2[key]:
                diff[key] = {'status': 'not changed', 
                             'value': new_file1[key]}               
    return diff
    
