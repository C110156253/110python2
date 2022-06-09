method,time = list(input("輸入月租費型式及通話時間：").split(","))
method,time = int(method),int(time)
if(method==186):
    if(time*0.09 <= method ):
        print("通話費為：%.0f" %(method))
    elif(method < time*00.9 <= method*2):
        print("通話費為：%.0f" %(time*0.09*0.9))
    elif(time*0.09 >method*2):
        print("通話費為：%.0f" %(time*0.09*0.8))
elif(method == 386):
    if(time*0.08 <= method ):
        print("通話費為：%.0f" %(method))
    elif(method < time*0.08 <= method*2):
        print("通話費為：%.0f" %(time*0.08*0.8))
    elif(time*0.08 >method*2):
        print("通話費為：%.0f" %(time*0.08*0.7))
elif(method == 586):
    if(time*0.07 <= method ):
        print("通話費為：%.0f" %(method))
    elif(method < time*0.07 <= method*2):
        print("通話費為：%.0f" %(time*0.07*0.7))
    elif(time*0.07 >method*2):
        print("通話費為：%.0f" %(time*0.07*0.6))
elif(method == 986):
    if(time*0.06 <= method ):
        print("通話費為：%.0f" %(method))
    elif(method < time*0.06 <= method*2):
        print("通話費為：%.0f" %(time*0.06*0.6))
    elif(time*0.06 >method*2):
        print("通話費為：%.0f" %(time*0.06*0.5))