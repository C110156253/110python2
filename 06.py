list1 = list(input("輸入值為：").split(","))
Max = ""
Min = ""
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1.sort()
for i in range(len(list1)):
    Min += str(list1[i])
list1.reverse()
for i in range(len(list1)):
    Max += str(list1[i])

print("最大值數列與最小值數列差值為：", int(Max) - int(Min))