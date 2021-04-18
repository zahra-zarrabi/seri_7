def mul(a,b):
    result={'s':None,'m':None}
    result['s']=a['s']*b['s']
    result['m']=a['m']*b['m']
    return result

def sum(a,b):
    result={}
    result['s']=(a['s']*b['m'])+(a['m']*b['s'])
    result['m']=a['m']*b['m']
    return result

def sub(a,b):
    result = {}
    result['s'] = (a['s'] * b['m']) - (a['m'] * b['s'])
    result['m'] = a['m'] * b['m']
    return result

def div(a,b):
    result={}
    result['s']=(a['s']*b['m'])/(a['m']*b['s'])
    return result

sorat1=int(input('Please enter the form of first deduction: '))
makhrag1=int(input('Please enter the denominator of the first fraction:'))
sorat2=int(input('Please enter the form of Second deduction: '))
makhrag2=int(input('Please enter the denominator of the Second fraction:'))
a={'s':sorat1,'m':makhrag1}
b={'s':sorat2,'m':makhrag2}

c=mul(a,b)
print('Multiply of two fractions: ',c['s'],'/',c['m'])

c=sum(a,b)
print('sum of two fractions: ',c['s'],'/',c['m'])

c=sub(a,b)
print('Submission of two fractions: ',c['s'],'/',c['m'])

c=div(a,b)
print('Division of two fractions: ',c['s'])