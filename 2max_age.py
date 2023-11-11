age = int(input("enter age: "))

my_list = []

while age!=-1:
    my_list.append(age)
    age = int(input("enter age: "))


print(my_list)
my_list.sort()
print(my_list[-1], " ", my_list[-2])




