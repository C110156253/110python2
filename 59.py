x = int(input("請輸入金額："))
tmp = 0 
while True:
    if x >= 100:
        x -= 100
        tmp += 1
    elif (50 <= x < 100):
        x -= 50
        tmp += 1
    elif (10 <= x < 50):
        x -= 10
        tmp += 1
    elif (5 <= x < 10):
        x -= 5
        tmp += 1
    elif (1 <= x < 5):
        x -= 1
        tmp += 1
    elif(x == 0):
        print(tmp)
        break

