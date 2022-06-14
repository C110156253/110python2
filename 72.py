n = int(input("請輸入n:"))
k = int(input("請輸入k:"))
N = n
s1 = 0
while True:
    s1 = s1 + (n//k)
    n = n//k
    if n < k:
        break
print("Peter可以抽",N+s1,'支紙菸')