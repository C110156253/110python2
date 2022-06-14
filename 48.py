n = int(input("輸入筆數n:"))
dic = {}
for i in range(n):
    eng , chi = input().split()
    dic[eng] = chi
w = input("輸入欲查詢單字:")
if w in dic:
    print(w,"中文意思為",dic[w])
else:
    print("字典沒有此單字")
