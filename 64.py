s1 = 0
s2 = 0
x1 = int(input("請輸入第一個要判斷的數字:"))
x2 = int(input("請輸入第二個要判斷的數字:"))
if x2-x1 != 2:
    print("N")
else:
    for i in range(1, x1+1):
        if x1%i == 0:
            s1 += 1
    for i in range(1, x2+1):
        if x2%i == 0:
            s2 += 1
    if s1 == 2:
        if s2 == 2:
            print("Y")
        else:
            print("N")
    else:
        print("N")