def menu():
    item=int(input('Time calculations:\n1 sum of two time\n2 Subtraction of two time\n3 Convert seconds to time\n4 Convert time to seconds\n5 exit'))

    if item==1:
        print('Please enter two times:\nTime 1:')
        hour = int(input("hour : "))
        minute = int(input("Minutes : "))
        second = int(input("Seconds :"))
        hh = int(input("Time 2:\nhour : "))
        mm = int(input("Minutes : "))
        ss = int(input("Seconds :"))
        print("sum of two time: ", sum_time(hour, minute, second,hh,mm,ss))
        menu()

    elif item==2:
        print('Please enter two times:\nTime 1:')
        hour = int(input("hour : "))
        minute = int(input("Minutes : "))
        second = int(input("Seconds :"))
        hh = int(input("Time 2:\nhour : "))
        mm = int(input("Minutes : "))
        ss = int(input("Seconds :"))
        print("Subtraction of two time: ", sub_time(hour, minute, second, hh, mm, ss))
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


def my_second(times):
    t={}
    t['h']=int(times/3600)
    times=times%3600
    t['m']=int(times/60)
    t['s']=int(times%60)
    return t

def my_time(h,m,s):
    h=h*3600
    m=m*60
    r=h+m+s
    return r

def sum_time(h,m,s,hh,mm,ss):
    h = h * 3600
    m = m * 60
    hh=hh*3600
    mm=mm*60
    r = h + m + s+hh+mm+ss
    return r


def sub_time(h,m,s,hh,mm,ss):
    h = h * 3600
    m = m * 60
    hh = hh * 3600
    mm = mm * 60
    r =( h + m + s )- (hh + mm + ss)
    return r




menu()