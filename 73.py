time1 = input("請輸入時間1(時:分:秒)：")
h1,m1,s1 = (time1.split(":"))
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)
time2 = int(input("請輸入時間2(秒)："))
s2 = time2
m2 = 0
h2 = 0
while True:
    if h1 > 0:
        m1 += 60 * h1
        h1 = 0
        if m1 > 0:
            s1 += 60 * m1
            m1 = 0
            print("時間1",str(time1),"格式轉換後為",str(s1),"秒")
            break
while True:
    if s2 >= 60:
        m2 = s2 / 60
        s2 = s2 % 60
        if m2 >= 60:
            h2 = m2 / 60
            m2 = m2 % 60
            print("時間2",str(time2),"=","%d:%d:%d"%(h2,m2,s2))
            break
    