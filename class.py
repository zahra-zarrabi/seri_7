
class fraction:
    def __init__(self):
        self.sorat1=int(input('Please enter the form of first deduction: '))
        self.makhrag1=int(input('Please enter the denominator of the first fraction:'))
        self.sorat2=int(input('Please enter the form of Second deduction: '))
        self.makhrag2=int(input('Please enter the denominator of the Second fraction:'))


    def mul(self):
        s=self.sorat1*self.sorat2
        m=self.makhrag1*self.makhrag2
        return (str(s) + '/' + str(m))

    def sum(self):
        s=(self.sorat1*self.makhrag2)+(self.sorat2*self.makhrag1)
        m=self.makhrag1*self.makhrag2
        return (str(s) + '/' + str(m))

    def sub(self):
        s=(self.sorat1*self.makhrag2)-(self.sorat2*self.makhrag1)
        m=self.makhrag1*self.makhrag2
        return (str(s) + '/' + str(m))

    def div(self):
        s=(self.sorat1*self.makhrag2)/(self.makhrag1*self.sorat2)
        return s


class my_time():
    def __init__(self):
        if item==1 or item==2:
            self.hour = int(input("Time 1:\nhour : "))
            self.minute = int(input("Minutes : "))
            self.second = int(input("Seconds :"))
            self.hh = int(input("Time 2:\nhour : "))
            self.mm = int(input("Minutes : "))
            self.ss = int(input("Seconds :"))

    def sum_time(self):
        h = self.hour * 3600
        m = self.minute * 60
        hh = self.hh * 3600
        mm = self.mm * 60
        r = h + m + self.second + hh + mm + self.ss
        return r
    def sub_time(self):
        h = self.hour * 3600
        m = self.minute * 60
        hh = self.hh * 3600
        mm = self.mm * 60
        r = (h + m + self.second) - (hh + mm + self.ss)
        return r

    def my_second(self):
        times=int(input('second'))
        hour= int(times / 3600)
        times = times % 3600
        minute = int(times / 60)
        second = int(times % 60)
        return str(hour)+':'+str(minute)+':'+str(second)

    def time(self):
        hour = int(input("Time 1:\nhour : "))
        minute = int(input("Minutes : "))
        second = int(input("Seconds :"))
        h = hour * 3600
        m = minute * 60
        r = h + m + second
        return r


while True:
    input_number = int(input('Choose one:\n1 Calculations of fractions\n2 Time calculations\n3 exit'))

    if input_number == 1:
        print('Calculations of fractions')
        obj = fraction()

        print('(', obj.sorat1, '/', obj.makhrag1, ')*(', obj.sorat2, '/', obj.makhrag2, ')=', obj.mul())

        print('(', obj.sorat1, '/', obj.makhrag1, ')+(', obj.sorat2, '/', obj.makhrag2, ')=', obj.sum())

        print('(', obj.sorat1, '/', obj.makhrag1, ')-(', obj.sorat2, '/', obj.makhrag2, ')=', obj.sub())

        print('(', obj.sorat1, '/', obj.makhrag1, ')/(', obj.sorat2, '/', obj.makhrag2, ')=', obj.div())


    elif input_number==2:
        item=int(input('Time calculations:\n1 sum of two time\n2 Subtraction of two time\n3 Convert seconds to time\n4 Convert time to seconds'))
        if item==1:
            objj=my_time()
            print('sum of two time:',objj.sum_time())
        elif item==2:
            objj=my_time()
            print('Subtraction of two time:',objj.sub_time())
        elif item==3:
            objj = my_time()
            print('is time: ', objj.my_second())
        elif item==4:
            objj = my_time()
            print('Seconds: ', objj.time())

    elif input_number==3:
        exit()