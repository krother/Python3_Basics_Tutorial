
# find all files that match a certain pattern in a directory tree.

import os, fnmatch

def search_tree(root, pattern):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)
                

if __name__ == '__main__':
    path = '/home/krother/projects/'
    for filename in search_tree(path, '*.py'):
        print(filename)
