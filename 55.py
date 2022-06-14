listA = ["飢餓遊戲3","解憂雜貨店","怪獸與牠們的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
listB = ["房思琪的初戀樂園","等一個人的咖啡","鬼滅之刃14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]
search =  input("請輸入欲租借書籍：")
if search in listA:
    for i in range(len(listA)):
        if listA[i] == search:
            print("在書架A的第", i+1 ,"本")
elif search in listB:
    for i in range(len(listB)):
        if listB[i] == search:
            print("在書架A的第", i+1 ,"本")
else:
    print("查無此書籍")