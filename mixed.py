def sum(x,y):
    r=x+y
    return r
def sub(x,y):
    r=x-y
    return r

def mul(x,y):
    r=x*y
    return r

def div(x,y):
    s={'a':None,'b':None}
    s['a']=x*(complex(real_2,-imaginary_2))
    s['b']=y*(complex(real_2,-imaginary_2))
    return s

real_1=int(input('Enter the real part of the first number: '))
imaginary_1=int(input('Enter the imaginary part of the first number: '))
real_2=int(input('Enter the real part of the Second number: '))
imaginary_2=int(input('Enter the imaginary part of the Second number: '))
a = complex(real_1, imaginary_1)
b = complex(real_2, imaginary_2)

result=sum(a,b)
print(a,'+',b,'=',result)

result=sub(a,b)
print(a,'-',b,'=',result)

result=mul(a,b)
print(a,'*',b,'=',result)

result=div(a,b)
print(a,'/',b,'=',result['a'],'/',result['b'])

