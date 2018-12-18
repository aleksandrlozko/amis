def getName(line):
    name, line = getElement(line)
    name = name[0].upper()+name[1:].lower()
    return name, line

def getDate(line):
    result = re.split(r',', line, maxsplit=1)
    date = re.findall(r'\d{2}\.\d{2}\.\d{4}', result[0])[0]
    return date, result[1]

def getProduct(line):
    product, line = getElement(line)
    return product.lower(), line


def getQuantity(line):
    quantity, line = getElement(line)
    if quantity:
        return float(quantity), line
    else:
        return 0, line

def getPrice(line):
    result = re.split(r'"', line, maxsplit=2)
    price = re.findall(r'\d+,{0,1}\d*', result[1])[0]
    # price = price.replace(",",".")
    return float(price), result[2][1:]

try:
    with open(input_file, encoding="utf-8", mode='r') as file:

        # skip header
        file.readline()

        line_number = 1
        for line in file:
            line = line.strip().rstrip()
            line_number += 1
            if not line:
                continue

            name, line = getName(line)
            date, line = getDate(line)
            product,line = getProduct(line)
            quantity,line = getQuantity(line)
            price,comment = getPrice(line)
            print(name,date,product,quantity,price,comment)


    # [l for l in (line.strip() for line in f) if l]

except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number)