n = int(input("0 < n < 1,000,000"))
list1 = [n]
s = ''
while True:
    if n == 1:
        break
    else:
        if n % 2 == 0:
            n /= 2
            list1.append(int(n))
        else:
            n = 3*n+1
            list1.append(int(n))
list1=list(map(str,list1))
for i in range(len(list1)):
    s = s + list1[i] + ' '
print("數列:", s)