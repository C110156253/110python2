x = input("輸入字串(至少10個字):")
list1 = []
for i in x:
    a = x.count(i,0,len(x))
    if a > 1 and i not in list1:
        list1.append(i)

print(list1)