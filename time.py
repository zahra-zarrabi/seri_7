def menu():
    item=int(input('Time calculations:\n1 sum of two time\n2 Subtraction of two time\n3 Convert seconds to time\n4 Convert time to seconds\n5 exit'))

    if item==1:
        print('Please enter two times:\nTime 1:')
        gettime()
        print("sum of two time: ", sum_time())

        menu()

    elif item==2:
        print('Please enter two times:\nTime 1:')
        gettime()
        print("Subtraction of two time: ", sub_time())
        menu()

    elif item==3:
        times=int(input('Please enter time in seconds:'))
        c=my_second(times)
        print(c['h'],':',c['m'],':',c['s'])
        menu()

    elif item==4:
        print('Please enter the following times:')
        hour=int(input("hour : "))
        minute=int(input("Minutes : "))
        second=int(input("Seconds :"))
        print("Time in seconds : ",my_time(hour,minute,second))
        menu()

    else:
        exit()

def gettime():
    hour = int(input("hour : "))
    minute = int(input("Minutes : "))
    second = int(input("Seconds :"))
    hh = int(input("Time 2:\nhour : "))
    mm = int(input("Minutes : "))
    ss = int(input("Seconds :"))
    global time1
    global time2
    time1 = {'h': hour, 'm': minute, 's': second}
    time2 = {'h': hh, 'm': mm, 's': ss}

def my_second(times):

    time1['h']=int(times/3600)
    times=times%3600
    time1['m']=int(times/60)
    time1['s']=int(times%60)
    return time1

def my_time(h,m,s):
    h=h*3600
    m=m*60
    r=h+m+s
    return r

def sum_time():
    h = time1['h'] + time2['h']
    m = time1['m'] + time2['m']
    s=time1['s']+time2['s']
    if s>60:
        s-=60
        m+=1
    if m>60:
        m-=60
        h+=1
    return (str(h) + ':' + str(m)+':'+str(s))


def sub_time():
    h = time1['h'] - time2['h']
    m = time1['m'] - time2['m']
    s = time1['s'] - time2['s']
    if s<0:
        s+=60
        m-=1
    elif m<0:
        m+=60
        h-=1
    return (str(h) + ':' + str(m)+':'+str(s))




menu()
