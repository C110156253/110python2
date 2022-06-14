n = int(input("請輸入正整數："))
list1 = []
total = 0
for i in range(1,n):
    if n % i == 0 :
        list1.append(i)
for i in range(len(list1)):
    total += list1[i]
if total == n:
    print('perfect')
elif total > n:
    print('abundant')
else:
    print('deficient')