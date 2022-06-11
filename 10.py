n , m = input("請輸入N及M值為：").split(" ")
n , m = int(n) , int(m)
list1 = []
for i in range(n):
    list1.append(input("輸入矩陣數值第%d列為："%(i+1)).split(" "))
for j in range(m):
    for k in range(n-1):
        print("輸出矩陣數值第%d列為："%(j+1),list1[k][j],list1[k+1][j])
