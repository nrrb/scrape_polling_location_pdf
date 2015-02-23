import csv
import re
import sys

output_file = 'polling_locations.csv'

if len(sys.argv) < 2:
    print '''Syntax:

python %s <html file>

This will output to '%s'.
    ''' % (__file__, output_file)
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    lines = f.read().split('\n')

br_lines = filter(lambda line: '<br>' in line, lines)

data = []
record_data = False
for line in br_lines:
    # start of section:
    # beginning of line is 'Polling Places'
    # end of section:
    # line after end of data starts with '* '
    if re.search('^Polling Place', line):
        record_data = True
        continue
    if re.search('^\* ', line):
        record_data = False
        continue
    if record_data:
        data.append(line)

# Strip the <br> html tag from all lines
stripped_lines = map(lambda line: re.search(r'(?P<text>.*)<br>', line).groupdict()['text'], data)

# Each line of data is comprised of four lines in this array
# 1. ward
# 2. precinct
# 3. name of polling location
# 4. polling location address
locations = []
for starting_index in range(0, len(stripped_lines), 4):
    location = dict(zip(['ward', 'precinct', 'name', 'address'], stripped_lines[starting_index:starting_index+4]))
    locations.append(location)

# in the translation from PDF to HTML, the column between precinct and location name is either blank or contains an x,
# with the presence of an x indicating that the location is NOT handicapped accessible.
for i, location in enumerate(locations):
    if re.search(r'^x ', location['name']):
        locations[i]['accessible'] = False
        locations[i]['name'] = re.search(r'^x (?P<name>.*)', locations[i]['name']).groupdict()['name']
    else:
        locations[i]['accessible'] = True

with open(output_file, 'wb') as f:
    dict_writer = csv.DictWriter(f, fieldnames=['ward', 'precinct', 'name', 'address', 'accessible'])
    dict_writer.writeheader()
    dict_writer.writerows(locations)

