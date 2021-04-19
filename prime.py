def my_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
number1=int(input('Enter number1: '))
number2=int(input('Enter number2: '))
for i in range(number1,number2+1):
    if my_prime(i)==True:
        print(i,end=',')
