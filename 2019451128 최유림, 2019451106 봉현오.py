data=80
i=0
x=0
while (x!=data):
    x=int(input("please enter an integer:"))
    i+=1
    if (x>data):
        print('x>data')
    elif(x<data):
        print('x<data')
    else:
        print('congraturation!!!')
else:
    print(f'eteration : {i}')
    