"""n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))

list_main = []
list = [x for x in range(n1,n2+1)]
for el in list:
    if el % 2 == 0:
        list_main.append(el)
print(list_main)"""





d = {"Bob":19,"Boba":20,"Boban":18,"Alex":21,"Sas":15,"Anj":12}
list_of_name = []
list_of_age = []
main_age = []
for el in d:
    list_of_name.append(el)
print(list_of_name)
for name in list_of_name:
    list_of_age.append(d[name])
print(list_of_age)
list_of_age.sort()
main_age.append(list_of_age[len(list_of_age)-1])
main_age.append(list_of_age[len(list_of_age)-2])
main_age.append(list_of_age[len(list_of_age)-3])
for main in main_age:
    for name in list_of_name:
        if main == d[name]:
            print(name, d[name])

