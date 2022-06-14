n = int(input("輸入n值"))
name = []
email = []
for i in range(n):
    name.append(input("請輸入名字："))
    email.append(input("請輸入電子郵件："))
dict1 ={}
for i in range(n):
    dict1[name[i]]=email[i]
check = input("請輸入要查詢的電子郵件姓名：")
print(check,"的電子郵件為",dict1[check])
