#! python3
# blankRowInserter.py
# This program takes 3 arguments: a starting row, a gap size, and an Excel file
# then adds a gap after the specified row in that file

import sys, openpyxl

if len(sys.argv) < 4:
    print("""\n
    This adds blank rows to an Excel document. It takes 3 arguments:
    
    1. The row to start on
    2. The size of the gap (how many rows)
    3. The file you are adding them to.
    
    eg. blankRowInserter.py 3 5 example.xlsx\n""")
    sys.exit()

start_row = sys.argv[1]
gap_size = sys.argv[2]
wbfile = sys.argv[3]

try:
    start_row = int(start_row)
    gap_size = int(gap_size)

    wb = openpyxl.load_workbook(wbfile)

except ValueError:
    print('Starting row and gap size must be integers')
    sys.exit()

except FileNotFoundError:
    print('That file doesn\'t seem to exist')
    sys.exit()

sheet = wb.active

sheet.insert_rows(start_row, gap_size)

wb.save(wbfile)