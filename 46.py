n = int(input("輸入比數n:"))
win = {}
for i in range(n):
    med,value=input("").split()
    win[med]=value
for med , value in win.items():
    print(med,"牌得到",value,'面')