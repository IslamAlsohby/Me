User = input("Enter the word ------> ").lower()

contain_a = "a"
contain_e = "e"
contain_i = "i"
contain_o = "o"
contain_u = "u"


count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for letter in User:
    if letter == contain_a:
        count_a += 1
        continue
    elif letter == contain_e:
        count_e += 1
        continue
    elif letter == contain_i:
        count_i += 1
        continue
    elif letter == contain_o:
        count_o += 1
        continue
    elif letter == contain_u:
        count_u += 1
        continue
     
print(f"There is {count_a} (a)")
print(f"There is {count_e} (e)")
print(f"There is {count_i} (i)")
print(f"There is {count_o} (o)")
print(f"There is {count_u} (u)")