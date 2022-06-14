from re import S


a = int(input("輸入a的係數:"))
b = int(input("輸入b的係數:"))
c = int(input("輸入c的係數:"))
s = b ** 2 - 4 * a * c
x1 = (-b + s ** 0.5) / 2
x2 = (-b - s ** 0.5) / 2
print(s)
if s == 0:
    print(int(x1))
elif s > 0 :
    print(int(x1),int(x2))
elif s < 0 :
     print("無解")

