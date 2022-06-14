x = int(input("搭了幾次電梯："))
tmp = 1
money = 0 
for i in range(x):
    y = int(input("輸入樓層："))
    if (tmp == y):
        print("你就在這層樓")
        y = int(input("輸入樓層："))
    else:
        if (y > tmp):
            money += (y-tmp)*20
        elif (y < tmp):
            money += (tmp-y)*10
    tmp = y
print("%d 元" %(money))