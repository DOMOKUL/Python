import re

s = 'И волны клянутся всеводному Цику  оружие бурь до победы не класть.'

s2 = re.sub(r'\s+', '\n', s)
print(s2)