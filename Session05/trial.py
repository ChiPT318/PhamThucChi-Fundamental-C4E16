# person = ["Quy", 20, 0, "Hanoi", "Vinh Phuc", 3, ["Coding", "Manga", "Pingpong"]]
        #  name,  age, ex, ......
# dictionary: key : value couple
    # create
person = {

    "name" : "Quy",
    "age"  : 20,
    "ex"   : 0,
    "sex"  : "male"
}

    # read
# key = "age"
# if "key" in person:
#     print(person[key])
# else:
#     print("Not found")



    #update
person["age"] += 3

print(person)

    #delete: search yourself
    #them
person["school"] = "HUST"
print(person)
