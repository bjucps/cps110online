# To use openpyxl, execute:
#   pip install openpyxl

import openpyxl

# load spreadsheet
wb = openpyxl.load_workbook('produceSales.xlsx')

ws = wb.worksheets[0] # get first worksheet

sum = 0
rows = list(ws.values)  # convert rows in worksheet to a list

# iterate over values and sum up the pounds
for row in rows[1:]:
    print(row[0], '|', row[2])
    sum += row[2]

print('Total pounds sold:', sum)

# Update value in a cell
ws.cell(1, 3).value = "POUNDS"

# Add a new record to bottom of sheet
ws.append(['Potatoes, Russet', 2.0, 2.5, 5.0])

print('Saving changes in updatedProduceSales.xlsx')

# Save
wb.save('updatedProduceSales.xlsx')
