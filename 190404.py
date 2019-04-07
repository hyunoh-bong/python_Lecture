'''
person=input('Enter your name: ')
print('Hello', person)

yes_votes=23_453_457
no_votes=65_463_454
percentage=yes_votes/(yes_votes+no_votes)
print('{:-9,} YES votes {:2.2%}'.format(yes_votes,percentage))

import math
print(f'Thevalue of pi is approximately {math.pi:.5f}.')

animals='eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
'''
'''
#py 파일과 불러올 파일을 같은 곳에 놓을 것
#안되면 절대경로로 /로 하면 될 듯
with open("workData.txt", "r") as f:
    print("This is the file name:", f.name)
    #line=f.read()
    #line=f.read(6)
    #line_data=f.readline()
    #line_data=f.readlines()
    for line in f:
        print(line)
'''
'''
values=[1234,5678,9012]

with open("workData.txt", "r+") as f:
    for value in values:
        str_value=str(value)
        f.write(str_value)
        #파일에 write
        f.write("\n")
        #줄 바꿔서 넣어라
'''
'''
f=open('workfile.txt','r+')
f.seek(5,0)
print(f.read(1))
f.seek(0,2)
print(f.read(1))
'''
f=open('newfile.dat','wb')
for i in range(10):
    f.write(b'0123456789abcdef')
f.close()