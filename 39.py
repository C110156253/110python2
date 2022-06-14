n = int(input("輸入整數n："))

for i in range(n+1):
    for k in range(n+1-i):
        print(" ",end='')
    for k in range(2*i-1):
        if k%2==0:
            print(" ",end='')
        else:
            print("*",end='')
    print()
for i in range(n+1,0,-1):
    for k in range(n+1-i):
        print(" ",end='')
    for k in range(2*i-1):
        if k%2==0:
            print(" ",end='')
        else:
            print("*",end='')
    print()
