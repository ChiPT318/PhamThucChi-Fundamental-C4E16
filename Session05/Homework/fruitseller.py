prices ={"banana": 4,
         "apple": 2,
         "orange": 1.5,
         "pear": 3}
stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}
for fruit in prices:
    print(fruit)
    print("Price: ", prices[fruit])
    if fruit in stock:
        print("Stock: ", stock[fruit])
        print("*"*34)
total = 0
for money in prices:
    money = prices[money]*stock[money]
    total += money
    
print(total)
