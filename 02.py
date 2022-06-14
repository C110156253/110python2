x =float(input("請輸入度數(正整數)"))
if(x>=701):
    summer = 2.10 * 120 +3.02 * 210 + 4.39 * 170 + 4.97 * 200 +5.63 * (x-700)
    notsummer = 2.10 * 120 +2.68 * 210 + 3.61 * 170 + 4.01 * 200 +4.5 * (x-700)
elif(x>=501 and x < 701):
    summer = 2.10 * 120 +3.02 * 210 + 4.39 * 170 + 4.97 * (x-500)
    notsummer = 2.10 * 120 +2.68 * 210 + 3.61 * 170 + 4.01 * (x-500)
elif(x>=331 and x < 501):
    summer = 2.10 * 120 +3.02 * 210 + 4.39 * (x-330)
    notsummer = 2.10 * 120 +2.68 * 210 + 3.61 * (x-330) 
elif(x>=121 and x<331):
    summer = 2.10 * 120 +3.02 * (x-120)
    notsummer = 2.10 * 120 +2.68 * (x-120)
elif(x<121):
    summer = 2.10 * x
    notsummer = 2.10 * x
print("summermonth："+ str(summer))
print("summermonth："+str(notsummer))