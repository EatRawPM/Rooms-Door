from os import walk
from os.path import join
from pygame.image import load

def imports_files(folder_path):
    images = []

    for path, folders, files in walk(folder_path):
        for file in files:
            images.append(load(join(path, file)))

    return images

def imports_name_and_files(folder_path):
    images = {}
    
    for path, folders, files in walk(folder_path):
        print(f'Path: {path}, Folders: {folders}, Files: {files}')
        for file in files:
            name = file.split('.')[0]
            images[name] = load(join(path, file))
            
    return images

def imports_folder_and_files(folder_path):
    ret = {
        0: {
            'name': f'{folder_path}',
            'value': {}
        }
    }
    
    ret_value = ret[0]['value']
    print(ret_value)
    
    for path, folders, files in walk(folder_path):
        match path:
            case folder_path:
                ret[0]
        print(f'Path: {path}, Folders: {folders}, Files: {files}')
        
imports_folder_and_files('./assets/images')