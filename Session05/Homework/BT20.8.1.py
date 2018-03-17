counts = {}
string = input("What's your sentence? ").lower()

for letter1 in string:
    counts[letter1] = counts.get(letter1, 0) + 1

sorted_count = list(counts.keys())
sorted_count.remove(" ")
sorted_count.sort()

for letter2 in sorted_count:
    print(letter2, ":", counts[letter2])
