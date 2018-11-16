import re
a = re.compile("^(0?[0-9]|1[0-4])\\s+(0?[0-9]|1[0-4])$")
b = a.search("12  14")
# print b.group()
# print b
if b:
    c = b.group(1)
    print b.group(0)
    print b.group(1)
    print b.group(2)
    print type(c)