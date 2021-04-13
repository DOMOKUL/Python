import re

s = 'Раз два три'

print(len(re.sub(r'\s+', '', s)))