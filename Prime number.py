while True:
    number=int(input('Please enter one:\n1 Specify a number\n2 The prime number between two intervals\n3 exit'))

    if number==1:
        num=int(input('Enter the number:'))
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "*", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")


    elif number==2:
        a=int(input('The prime number between two intervals:\nnumber 1 '))
        b=int(input('number 2 '))
        for num in range(a, b + 1):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

    elif number==3:
        exit()
