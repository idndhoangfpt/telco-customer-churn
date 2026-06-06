# regular expression
import re

string = "hi 123 test 0 nay 8"

pattern = "\d+"

result = re.findall(pattern, string)

total = sum(int(num) for num in result)

print(total)

total = 0

for num in result:
    total += int(num)

print(total)


total = sum(list(map(int, result)))

print(total)


# re.split()
# re.spit(pattern, string, maxsplit)
