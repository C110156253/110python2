x = int(input("x軸座標"))
y = int(input("y軸座標"))
if (x == 0 and y  == 0):
    print("該點位於原點")
elif (x>0 and y>0):
    tmp = x*x+y*y
    print("該點位於第一象限，離原點距離為根號"+str(tmp))
elif (x<0 and y>0):
    tmp = x*x+y*y
    print("該點位於第二象限，離原點距離為根號"+str(tmp))
elif (x<0 and y<0):
    tmp = x*x+y*y
    print("該點位於第三象限，離原點距離為根號"+str(tmp))
elif (x>0 and y<0):
    tmp = x*x+y*y
    print("該點位於第三象限，離原點距離為根號"+str(tmp))
elif (x==0 and y<0):
    tmp = x*x+y*y
    print("該點位於下半平面y軸上，離原點距離為根號"+str(tmp))
elif (x==0 and y>0):
    tmp = x*x+y*y
    print("該點位於上半平面y軸上，離原點距離為根號"+str(tmp))
elif (x>0 and y==0):
    tmp = x*x+y*y
    print("該點位於右半平面x軸上，離原點距離為根號"+str(tmp))
elif (x<0 and y==0):
    tmp = x*x+y*y
    print("該點位於左半平面x軸上，離原點距離為根號"+str(tmp))