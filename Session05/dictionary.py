dic = {"pt" : "phat trien",
        "eny" : "em nguoi yeu",
        "any" : "anh nguoi yeu",
        "ngta" : "nguoi ta",
        "stt" : "status"}
while True:
    for key in dic:
        print(key, end="\t") #xoac t = tab, xoac n = xuong dong
    print()
    code = input("Your code ")
    if code in dic:
        print("Code: ", code)
        print("Translation: ", dic[code])
    else:
        print("Not found")
        choice = input("Word not found. Would you like to contribute this code? Y/N?").lower()
        if choice == "y":
            translation = input("Translation? ")
            dic[code] = translation
            print("Updated")

        else:
            break
