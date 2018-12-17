# Створити dataset та працювати з ним

# Які продукти купляли усі покупці?

# Як змінювалась ціна на яблука? (графік)

# Скільки грошей витрачає кожний покупець на покупки? (графік)

# Який найпопулярніший товар?

# Якого товару було куплено найменше?

# Який найдорожчий товар?

# Якого товару, скільки покупців купляє? (графік)

# Написати функціонал для додавання нових даних
def add():
    name = input("Введите имя:")
    data = input("Введите дату:")
    product = input("Введите продукт:")
    quan = input("Введите количество:")
    price = input("Введите цену:")
    f.write(name + "," + data + "," + product + "," + quan + "," + price)
import plotly
import plotly.graph_objs as go

file = open('data/orders.csv', 'r+')

with file as f:
    add()
#==========create dict==================
    header = f.readline()
    header = header.rstrip().split(",")
    line = f.readline()
    names = []
    product = []
    prices = []
    final_price = []
    quantity1 = []
    while line:
        lines = line.rstrip().split(",")
        dict_main = dict(zip(header, lines))
        #print(dict_main)
        line = f.readline()
        name = dict_main['client']
        product_f = dict_main[' product']
        price = dict_main[' price']
        quantity = dict_main[' quantity']
        quantity1.append(quantity)
        final_pr = float(quantity) * float(price)
        final_price.append(final_pr)
        product.append(product_f)
        prices.append(price)
        names.append(name)
        print(name, product_f)
    data = [go.Bar(
        x = names,
        y = final_price
    )]
    plotly.offline.plot(data, filename="bar.html")

    max_of = max(prices)
    print(max_of)

    trace = go.Pie(labels = names, values = quantity1)
    plotly.offline.plot([trace], filename = 'pie.html')


