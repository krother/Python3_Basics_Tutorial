
# xlrd

## What is xlrd?

`xlrd` is a Python library for reading Excel documents.

## Installation

Write in the command line:

    `pip install xlrd`

## Exercises

### Exercise 1

Create an Excel table similar to the data in the `.txt` files.

| name | number |
|------|--------|
| Jacob | 34465 |
| Michael | 32025 |
| Matthew | 28569 |

### Exercise 2

Execute the following program:

    import xlrd

    workbook = xlrd.open_workbook("data.xlsx")
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])

    row = sheet.row(0)
    for row_idx in range(0, sheet.nrows):
        print ('-'*40)
        print ('Row: %s' % row_idx)
        for col_idx in range(0, sheet.ncols):
            cell_obj = sheet.cell(row_idx, col_idx)
            print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

### Exercise 3

Make the program work and print the data from the document to the screen.

### Exercise 4

Calculate the sum of numeric values in the Python program.
