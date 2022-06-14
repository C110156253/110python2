km = float(input("請輸入路程公里數(km):"))
basic = 75
bkm = 1.5
exkm = 0.25
total = 75
while True:
    if km <= 1.5:
        print("所需車資為:", total)
        break
    else:
        while km > 1.5 :
            km -= exkm
            total += 5
            if km <= bkm :
                print("所需車資為:", total)
                break
        break