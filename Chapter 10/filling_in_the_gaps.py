#! python3
# Finds numbered files with a given prefix, such as spam001.txt,
# in a single folder and renumbers them if there is a gap, or 
# adds a gap if chosen.

import os, shutil, re
from sys import exit

# This function renumbers files in numerical order, with no gaps
# from 1 to 999 max
def renumber(prefix, extension):
    num_suffix = 1
    extension = '.' + extension
    total_matches = 0
    total_changes = 0
    name_format = re.compile(prefix + r'(\d\d\d)' + extension) # Format of filename, 3 numbers, and a 2-4 character extension
    file_list = os.listdir()
    
    for file in file_list:
        file_match = name_format.search(file)
        if file_match == None: # Checks if current file doesn't match format, proceed to next
            continue
        elif file_match != None: # If current file does match format, check its numbering and rename if necessary
            total_matches += 1
            if file == prefix + str(num_suffix).zfill(3) + extension:
                num_suffix += 1
                continue
            # This next line is long but I had trouble coming up with a better solution.
            # It tests if the file name starts with the prefix, ends with the extension, 
            # but that the prefix with numbering is not what's expected, then renumbers it
            # appropriately
            elif file.startswith(prefix) == True and file.endswith(extension) == True and file.startswith(prefix + str(num_suffix).zfill(3)) == False:
                print('Renaming ' + file + ' to ' + prefix + str(num_suffix).zfill(3) + extension)
                shutil.move(file, prefix + str(num_suffix).zfill(3) + extension)
                total_changes += 1
        num_suffix += 1
    if total_changes > 0:
        print('\n' + str(total_matches) + ' files were found, and ' + str(total_changes) + ' files were renamed')
    elif total_changes == 0:
        print('\nNo files matching ' + prefix + 'nnn' + extension + ' found in ' + os.getcwd())
    elif total_changes < 0:
        print('\nThis shouldn\'t be possible. Screencap this and get Justin to fix whatever just happened') 


# This one adds a gap to the
def make_gap(prefix, extension, cut_after, gap_size):
    num_suffix = 1
    cut_after = int(cut_after)
    gap_size = int(gap_size)
    total_matches = 0
    total_changes = 0
    extension = '.' + extension
    name_format = re.compile(prefix + r'(\d\d\d)' + extension) # Format of filename, 3 numbers, and a 2-4 character extension
    file_list = os.listdir()
    
    # The list must be iterated backwards to avoid overwriting files
    # ie, renaming spam005.txt to spam010.txt could overwrite an existing
    # spam010.txt if done from beginning to end
    i = len(file_list) - 1

    while i >= 0:
        file_match = name_format.search(file_list[i])
        if file_match == None:
            i -= 1
            continue
        elif file_match != None:
            total_matches += 1
            if int(file_match.group(1)) > cut_after:
                print('Renaming ' + file_list[i] + ' to ' + prefix + str(int(file_match.group(1)) + gap_size).zfill(3) + extension)
                shutil.move(file_list[i], prefix + str(int(file_match.group(1)) + gap_size).zfill(3) + extension)
                total_changes += 1
        i -= 1
        num_suffix += 1
    
    if total_changes > 0:
        print('\n' + str(total_matches) + ' files were found, and ' + str(total_changes) + ' files were renamed')
    elif total_changes == 0:
        print('\nNo files matching ' + prefix + 'nnn' + extension + ' found in ' + os.getcwd())
    elif total_changes < 0:
        print('\nThis shouldn\'t be possible. Screencap this and get Justin to fix whatever just happened') 

try:
    print('-' * 50)
    print("\nEnter '1' to close gaps")
    print("\nEnter '2' to create a gap\n")
    choice = input()

    if choice == '1':
        print('\nWhat is the prefix of the files?')
        usr_prefix = input().lower()
        print('\nWhat is the 2-4 character file extension? eg. PDF, TXT, etc...')
        usr_extension = input().lower()
        renumber(usr_prefix, usr_extension)
        exit

    elif choice == '2':
        print('\nWhat is the prefix of the files?')
        usr_prefix = input().lower()
        print('\nWhat is the 2-4 character file extension? eg. PDF, TXT, etc...')
        usr_extension = input().lower()
        print('\nWhat is the last number before cutoff?')
        usr_cut = input()
        print('\nHow big of a gap should be made?')
        usr_gap = input()
        make_gap(usr_prefix, usr_extension, usr_cut, usr_gap)
        exit
    else:
        exit

except ValueError:
    print('\n~~The cutoff and gap values *must* be numbers~~')