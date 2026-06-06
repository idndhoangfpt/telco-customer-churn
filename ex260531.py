print("Hello, World!")

# dictionary
user = {"username": "Hoang", "age": "12", "pass": "12"}
print(user.items())

print(user["age"])

print(user.items())


# Tuples tuples
# z[0]  = 34  -> mac định giá trị không thay đổi
# z1 = list(z) => force về list
z = (1, 2, 4, 45)


# phân biệt list dictionary set


# function
def test():
    print("xin chao test")


def test2(lastName, firstName):
    fullName = lastName + firstName

    return fullName


tst = test2("s", "xsxs")
print(tst)

import Tong

numbers = [1, 2, 3, 4, 5]
print(Tong.tinh_tong(numbers))


# looping

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
