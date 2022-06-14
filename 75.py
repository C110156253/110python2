list1 = []
while True:
    s = input("請輸入代辦事項(若已無事項﹑請輸入end):")
    list1.append(s)
    if s == 'end':
        for i in range(len(list1)-1):
            print('%d. %s' %(i+1,list1[i]))
        break