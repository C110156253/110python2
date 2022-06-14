x = int(input("請輸入正整數(<10)"))
for i in range(x):
    tmp = i+1
    for j in range(i+1):
        print(tmp,end=" ")
        tmp += i+1  
    print()