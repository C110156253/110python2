while True:
    s1 = input("檢測的字串(end結束):")
    if s1 == 'end':
        print("檢測結束")
        break
    else:
        list1 = []
        x = 0
        s2 = input("檢測的單一字元:")
        for i in range(len(s1)):
            list1.append(s1[i])
        for i in range(len(list1)):
            if s2 == list1[i]:
                x += 1
        print("字元%s出現次數為:%d" %(s2, x))