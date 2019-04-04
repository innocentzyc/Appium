import re

with open("result.txt") as f:
    res = f.readlines()

a = []
for line in res:
    line = line.replace("\n", "")
    pattern = re.compile("(.*)'tel': '(.*)'}")
    a.append(pattern.match(line).group(2))
length = len(a)

