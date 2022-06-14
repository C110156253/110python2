list1 = ["國文","英文","微積分","體育","程式設計"]
list2 = []
for i in range(len(list1)):
    list2.append(int(input("輸入"+list1[i]+"的分數")))
print("平均分數:%.2f分" %(sum(list2)/len(list1)))
print("最高分為 : " + list1[list2.index(max(list2))],max(list2),"分")
print("最低分為 : " + list1[list2.index(min(list2))],min(list2),"分")