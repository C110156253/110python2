list1  = list(input("輸入一組四位數字為："))
x1 = (int(list1[0])+7) % 10
x2 = (int(list1[1])+7) % 10
x3 = (int(list1[2])+7) % 10
x4 = (int(list1[3])+7) % 10
print("輸出加密後的數字為：%d%d%d%d" %(x3,x4,x1,x2))