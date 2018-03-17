numbers = [1, 6, 8, 1, 2, 1, 5, 6]
print(numbers)
count = {}

for number in numbers:
    count[number] = count.get(number, 0) + 1

while True:
    n = int(input("Enter a number? "))
    if n in count:
        print(n, " appears", count[n], " times in my list.")
    else:
        print("Not found")
