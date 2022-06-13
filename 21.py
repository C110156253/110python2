data = [["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
x = input("請輸入學生學號：")
for i in range(len(data)):
    if x == data[i][0]:
        print("學生資料為",x,data[i][1],data[i][2])
