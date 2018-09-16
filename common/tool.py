import os

def getRootDir():
    filepath = os.path.abspath(__file__)
    current_dir = os.path.dirname(filepath)
    while current_dir:
        print(current_dir)
        if os.path.exists(os.path.join(current_dir,'readme.md')):
            break
    
        current_dir = current_dir[0:current_dir.rfind(os.path.sep)]
    
    return current_dir
