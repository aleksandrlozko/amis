file=open("data/employee_birthday.txt", "r")

data =file.read()
print(data,"\n")

lines = data.splitlines()
print(lines,"\n")

for line in lines:
    print(line.split(","))


file.close()