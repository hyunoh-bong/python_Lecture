#2019451106 봉현오
#대문자는 -64, 소문자는 -96
score=0
for w in 'words':
    a=ord(w)
    if (a>96):
        a=a-96
    else:
        a=a-64
    score=score+a
print(score)