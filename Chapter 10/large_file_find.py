#! python3
# This program starts at your home directory and walks through all the folders
# that it contains, then prints a list of paths for every file larger than 100 MB

import os, sys
from pathlib import Path

# Prints an opening statement because it's polite and looks nice
while True:
    print('\n\n' + '-' * 72)
    print('This will scan your disk for files larger than 100MB'.center(72))
    print('starting from your home folder, on down'.center(72))
    print('-' * 72 + '\n\n')
    
    # Gets the user's home folder
    usr_home = Path.home()
    print(f'Your home folder is: {usr_home}\n')

    try: 
        do_it = input('Press ENTER to continue, or CTRL-C to quit\n\n')
        break
    except KeyboardInterrupt:
        print('\n\nExiting program...')
        sys.exit()
    
# Walks through every file and directory in user's home folder    
for root, dirs, files in os.walk(usr_home):
    os.chdir(root)
    for name in files:
        # Checks if each file is equal or greater than 100MB in size
        if os.path.getsize(name) >= 104857600:
            mega_size = int(os.path.getsize(name) / 1048576)  # Gets filesize in MB rather than B
            file_abs_path = str(Path(name).absolute())  # Gets the absolute path of the file
            print(f'{name} is {mega_size} MB ---> {file_abs_path}\n\n')

sys.exit()
        

