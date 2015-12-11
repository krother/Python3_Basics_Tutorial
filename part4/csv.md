
# csv

The `csv` module reads and writes tables from text files.

## Reading

    import csv

    reader = csv.reader(open('my_file.csv'))
    for row in reader:
        print row

## Writing
Similarly, tables can be written to files:

    write = csv.writer(open('my_file.csv','w'))
    write.writerow(table)

## Options of CSV file readers/writers
Both CSV readers and writers can handle a lot of different formats. Options you can change include:

* delimiter : the symbol separating columns.
* quotechar : the symbol used to quote strings.
* lineterminator : the symbol at the end of lines.

    reader = csv.reader(open('my_file.csv'), delimiter='\t', quotechar='"')

## Do I really need this?

Parsing a file with the common pattern

    for line in open('my_file.csv'):
        row = line.strip().split(',')

is almost as easy. It's your decision which you like more.
