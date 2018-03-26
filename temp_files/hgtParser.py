from gmalthgtparser import HgtParser

FILE_NAME = 'N35W002.hgt'

with HgtParser(FILE_NAME) as parser:
    for elev_value in parser.get_value_iterator():
        # each value is a tuple (zero based line number, zero based column number, zero based index, square corners of the elevation value, elevation value)
        print(elev_value)
        break