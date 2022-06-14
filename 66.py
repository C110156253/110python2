a = list(input("請輸入string_a:"))
b = list(input("請輸入string_b:"))
list1 = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if a[i] not in list1:
                list1.append(a[i])

list1.sort()
s = ""
if len(list1) > 0:
    for i in range(len(list1)):
        s += list1[i]
    print(s)
else:
    print("N")