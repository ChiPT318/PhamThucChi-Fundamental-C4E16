from random import choice
words = ["one", "two", "three", "four"]

random_word = choice(words)
characters = list(random_word)
jumble = ""
for i in range(len(characters)):
    random_char = choice(characters)
    jumble += random_char
    characters.remove(random_char)
print(jumble)
while True:
    n = input("What's the word")
    if n != random_word:
        print("Try again")
    else:
        print("Congrats")
        break
