n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))

list_main = []
list = [x for x in range(n1,n2+1)]
for el in list:
    if el % 2 == 0:
        list_main.append(el)
print(list_main)

