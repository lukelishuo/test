import re
string = '100,987.20'
p = re.compile("^\d{1,3}(,\d{3})*(\.\d{2})?")
print(re.match(r"^\d{1,3}(,\d{3})*(\.\d{2})", string))
print(bool(re.match(r"^\d{1,3}(,\d{3})*(\.\d{2})?", string)))
result = p.search(string)
print(p.findall(string))