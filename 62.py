from turtle import color


color = {"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
fruit = input("請輸入水果:")
if fruit in color:
    print("%s是%s"%(fruit,color[fruit]))