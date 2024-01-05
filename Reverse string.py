user = input("Enter the word-------> ")
count = -1
lis = []

for letter in user:
    print(f"{user[count]}", end="")
    lis.append(user[count])
    count -= 1
    