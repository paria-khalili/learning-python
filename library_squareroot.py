from math import sqrt
n = int(input("enter the number of numbers you want to know the square root: "))
numbers = []
for i in range(n):
    x = int(input("enter the number: "))
    numbers.append(x)

sqlist = []
for i in range(n):
    sq = sqrt(numbers[i])
    sq1 = "{:.4f}".format(sq)
    sqlist.append(sq1)

for i in range(n):
    print(sqlist[i])

input()