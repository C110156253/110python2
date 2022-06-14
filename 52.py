str1 = '紅豆生南國，春來發幾枝。願君多采擷，此物最相思。'
str2 = '春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
s = '，。'
for i in range(len(s)):
    str1=str1.replace(s[i],'')
    str2=str2.replace(s[i],'')

repact = []
for i in str1:
    for j in str2:
        if j == i:
            repact.append(j)

print(repact)