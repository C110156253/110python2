a = int(input("任教班級："))
list1 =[]
for i in range(a):
    b = int(input("班級人數："))
    list1.append(b)
    c = max(list1)
print(c)    