dataset = {
    "TheBestMilk":{
            "price": 99,
            "cover": "No",
            "shops": ["Fora", "ATB", "EKO", "Silpo"]
                  },
    "TheWorstMilk":{
            "price": 0.99,
            "cover": "No",
            "shops": ["ATB"]
                   },
    "TheMilk":{
            "price": 49,
            "cover": "Yes",
            "shops": ["EKO", "Fora", "Silpo"]

              }
          }
def price(dataset, list_keys):
    if list_keys == []:
        return None
    key = list_keys[0]
    prices = dataset[key]["price"]
    print(prices)
    price(dataset, list_keys[1:])

list_keys = [x for x in dataset.keys()]
print(price(dataset, list_keys))

list1 = [x for x in dataset.keys()]
set_with_shops = []
newdataset = {}
def cn(dataset, list_keys, newdataset):
    if list_keys == []:
        return 1
    key = list_keys[0]
    shop = dataset[key]["shops"]
    for each_shop in shop:
        set_with_shops.append(each_shop)
    cn(dataset, list_keys[1:], newdataset)
    set_shops = set(set_with_shops)
    for el in set_with_shops:
        if el in dataset[key]["shops"]:
            newdataset[el] = [key]
            print(newdataset)
print(cn(dataset, list_keys, newdataset))
#не полностью
