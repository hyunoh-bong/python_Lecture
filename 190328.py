''' <slide 72>
x=int(input("please enter an integer"))
if x<0:
    x=0
    print('Negative changed to zero')
elif x==0:
    print('zero')
elif x==1:
    print('single')
else:
    print('More')
'''

'''<example 1>
x=int(input("please enter an integer:"))
if x>0:
    print('x is positive')
elif x<0:
    print('x is negative')
else:
    print('x is zero')
'''

'''
n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print('Loop ended')
'''

'''
n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print('Loop ended')
'''
'''
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
'''    
''' 숫자 인덱싱
for i,v in enumerate('abcdefg'):
    print(i,v)
'''
'''
number=range(101)
s=0
for i in number:
    s=s+i
print(s)

number2=range(2,101,2)
s2=0
for i in number2:
    s2=s2+i
print(s2)
'''

''' numbering 해서 명령문 쓰기
questions=['name', 'job', 'favorite color']
answers=['Jane','a teacher','blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))
    
    f-string 활용
questions=['name', 'job', 'favorite color']
answers=['Jane','a teacher','blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
'''

'''
for i in reversed(range(1,8,2)):
   print(i)
'''


''' sorting
for f in sorted('qwertyuiopasdfghjklzxcvbnm'):
    print(f)
'''
'''
squares=[x**2 for x in range(10)]
print(squares)

squares2=[]
for x in range(10):
    squares2.append(x**2)
print(squares2)

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    ]
print(matrix)
'''
def add(a,b):
    return a+b
print(add(2,3))

def my_function(country="Korea"):
    print("I am from " + country)
print(my_function("china"))

def tri_recursion(k):
    if k>0:
        result=k+tri_recursion(k-1)
    else:
        result=0
    return result
print(tri_recursion(100))

def factorial_iter(n):
    ans=1
    for i in range(2,n):
        ans=ans*n
    return ans
def factorial_rec(n):
    if n<1:
        result=1
    else:
        result=n*factorial_rec(n-1)
    return result

