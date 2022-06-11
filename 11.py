m , d = input("輸入月及日：").split(" ")
m , d = int(m) ,int(d)
star = ["水瓶座Aquarius","雙魚座Pisces","牡羊座Aries","金牛座Taurus","雙子座Gemini","巨蟹座Cancer","獅子座Leo","處女座Virgo","天秤座Libra","天蠍座Scorpio","射手座Sagittarius","摩羯座Capricorn"]
if m == 1:
    if (21 <= d <=31) :
        print("星座為："+star[0])
    elif (1 <= d <21) :
        print("星座為："+star[11])
elif m == 2:
    if (19 <= d <=28) :
        print("星座為："+star[1])
    elif (1 <= d <19) :
        print("星座為："+star[0])
elif m == 3:
    if (21 <= d <=31) :
        print("星座為："+star[2])
    elif (1 <= d <21) :
        print("星座為："+star[1])
elif m == 4:
    if (21 <= d <=30) :
        print("星座為："+star[3])
    elif (1 <= d <21) :
        print("星座為："+star[2])
elif m == 5:
    if (22 <= d <=31) :
        print("星座為："+star[4])
    elif (1 <= d <22) :
        print("星座為："+star[3])
elif m == 6:
    if (22 <= d <=30) :
        print("星座為："+star[5])
    elif (1 <= d <22) :
        print("星座為："+star[4])
elif m == 7:
    if (23 <= d <=31) :
        print("星座為："+star[6])
    elif (1 <= d <23) :
        print("星座為："+star[5])
elif m == 8:
    if (24 <= d <=31) :
        print("星座為："+star[7])
    elif (1 <= d <24) :
        print("星座為："+star[6])
elif m == 9:
    if (24 <= d <=30) :
        print("星座為："+star[8])
    elif (1 <= d <24) :
        print("星座為："+star[7])
elif m == 10:
    if (24 <= d <=31) :
        print("星座為："+star[9])
    elif (1 <= d <24) :
        print("星座為："+star[8])
elif m == 11:
    if (23 <= d <=30) :
        print("星座為："+star[10])
    elif (1 <= d <23) :
        print("星座為："+star[9])
elif m == 12:
    if (22 <= d <=31) :
        print("星座為："+star[11])
    elif (1 <= d <22) :
        print("星座為："+star[10])