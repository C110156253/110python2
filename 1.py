# 找出數字字串中的最大質數
str1 = input("請輸入正整數：")
list1 = []
for i in range(len(str1)):
    for j in range(i+1):
        s1 = int(str1[j : len(str1)-i+j])
        if s1 % 2 == 1 :
            list2 = []
            for k in range(1, s1+1):
                if s1 % k == 0 :
                    list2.append(k)
            if len(list2) == 2 :
                list1.append(s1)

if len(list1) == 0:
    print("子字串最大的質數值為:No prime found")
elif len(list1) == 1 and 1 in list1:
    print("子字串中最大的質數值為:No prime found")
else:
    print("子字串中最大的質數值為：", max(list1))