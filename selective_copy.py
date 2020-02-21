#! python3
# Walks through a directory tree and searches for all files with a
# provided extension, then copies them to a folder with the extension
# as the name

import os, sys, re, shutil
from pathlib import Path

file_ext = sys.argv[1]  # First command line argument is the extension to search for
target_folder = sys.argv[2] # Second command line argument is the target folder

target_folder = Path(target_folder).absolute() # Ensures the path in an absolute path

if file_ext == "-help":
    print("Command Format is: selective_copy.py <file extension> <target directory>")
    sys.exit()

else:
    ext_format = re.compile(r'\.([a-zA-Z0-9]{2,4})') # Regex to start with a period, followed by 2-4 letters or numbers
    mo = ext_format.search(file_ext)
    if mo.group(0) == None: # Ensures the given extension meets the format of a period followed by 3-4 alphanumerics
        print('The file extension must be formatted as . followed by 2-4 letters or numbers')
        sys.exit()
    
    # Make the name of directory for files, check if it exists, and create it if it doesn't
    ext_folder = mo.group(1).upper() + " files"
    ext_folder_path = target_folder / ext_folder
    if ext_folder_path.exists() == False:
        creation_text = f'\nCreating folder {ext_folder_path}\n'
        print('-' * len(creation_text) + creation_text + '-' * len(creation_text))
        ext_folder_path.mkdir()
    
    # Find all files with that extension, and move them to the labeled directory
    for root, dirs, files in os.walk((target_folder)):
        os.chdir(root)
        for name in files:
            if Path.cwd() == ext_folder_path: # Checks to see if it's in the created folder, and skips if so
                continue
            elif name.endswith(file_ext) == True:
                print(f'Moving {name} to {ext_folder_path}\n')
                shutil.move(name, ext_folder_path)

sys.exit()
