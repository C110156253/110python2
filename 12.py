list1 = input("輸入一整數序列為:").split()
n = len(list1)/2
list2 = []
appear = 0
for i in list1:
    appear_str = ''
    if i not in list2:
        list2.append(i)
    else:
        appear += 1
        appear_str += i
if appear == 0:
    print("過半元素為:NO")
else:
    print("過半元素為:",appear_str)