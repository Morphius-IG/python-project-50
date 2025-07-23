def generate_diff(file1, file2):
    merged_keys = sorted({*file1.keys(), *file2.keys()})
    diff = {}
    for key in merged_keys:
        if (
            key in file2
            and key in file1
            and isinstance(file1[key], dict)
            and isinstance(file2[key], dict)
        ):
            diff[key] = {'status': 'parent', 
                         'value': generate_diff(file1[key], file2[key])}
        else:
            # Если текущего ключа нету в изначальном варианте
            if key not in file1: 
                # значит его добавили
                diff[key] = {'status': 'added', 'value': file2[key]}
                # Если текущего ключа нету в конечном варианте 
            elif key not in file2:
                # значит его удалили
                diff[key] = {'status': 'deleted', 'value': file1[key]}
                # Если значения ключей отличаются  
            elif file1[key] != file2[key]:  
                
                diff[key] = {'status': 'changed', 
                             'old': file1[key], 
                             'new': file2[key]}
            elif file1[key] == file2[key]:
                diff[key] = {'status': 'not changed', 
                             'value': file1[key]}               
    return diff
    
