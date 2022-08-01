import re

something = 'something'

# substitute
something = re.sub('[^A-Za-z0-9]+', '', something)

# match
re.fullmatch('[A-Z][0-9]', 'A1')
