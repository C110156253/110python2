s1 = input("輸入傳送密碼(6位數):")
while len(s1) != 6:
    print("請輸入六位數密碼")
    s1 = input("輸入傳送密碼(6位數):")

print("解密後的密碼：",end="")
for i in s1:
    for j in range(10):
        if(j*4%7 == int(i)):
            print(j,end="")
            break