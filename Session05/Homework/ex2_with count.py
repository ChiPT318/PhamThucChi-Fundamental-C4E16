numbers = [1, 6, 8, 1, 2, 1, 5, 6]
print(numbers)

n = int(input("Enter a number: "))
if n in numbers:
    count = 0
    for i in range(len(numbers)):
        if numbers[i-1] == n:
            count += 1
    print(n, " appears ", count, " times in the list")
else:
    print("Not found")


for i in range(len(numbers)):
    count = 0
