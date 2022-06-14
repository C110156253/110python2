M = int(input("小明身上有幾元:"))
N = int(input("販賣機有幾種飲料:"))
list1 = []
x = 0
for i in range(N):
    list1.append(input("每種飲料的價格:"))
list1 = list(map(int, list1))

for i in range(len(list1)):
    if M >= list1[i]:
        x += 1
print("可以買"+ str(x) + "種飲料")