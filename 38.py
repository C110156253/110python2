n = int(input("小狗有可能跑到的n個地方:"))
list1 = []
for i in range(n):
    list1.append(int(input("輸入猜想的點和家的距離:")))
for i in range(len(list1)):
    if list1[i]%9==0 or list1[i]%11==0:
        print("第"+str(i+1)+"個點", list1[i])