year = int(input())
year += 1
a = year // 1000
b = year // 100 % 10
c = year // 10 % 10
d = year % 10
while a == b or a == c or a == d or b == c or b == d or c == d:
    year += 1
    a = year // 1000
    b = year // 100 % 10
    c = year // 10 % 10
    d = year % 10
print(year)