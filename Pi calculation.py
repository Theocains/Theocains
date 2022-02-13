import math
from math import factorial
from decimal import Decimal, getcontext

list = []
coefficient = -0.0625
value = 0.5
for i in range(1, 500):
    value = 0.5
    if i == 1:
        coefficient = 1
        exponent = 1
       # print(coefficient)
        #print (exponent)
        integrated_exponent = 1
        intergrated_coefficient = 1
       # print(inco)
        calc = intergrated_coefficient * (0.5 ** integrated_exponent)
        list.append(calc)#print (list)
        '''
        print()
        print()```
        '''
    elif i == 2:

        coefficient = -0.5
        exponent = (i-1)*2
      #  print(coefficient)
      #  print(exponent)
        integrated_exponent = exponent + 1
        intergrated_coefficient = coefficient / integrated_exponent
      #  print(inco)
        value = 1
        test = ((value) ** 3)
       # print(test)
        calc = intergrated_coefficient * ((0.5) ** integrated_exponent)
        #print(calc)
        list.append(calc)
       # print(list)
        '''
        print()```
        print()```
        '''

    elif i == 3:

        coefficient = -1/8
        exponent = (i-1)*2
        '''
        print(coefficient)
        print(exponent)
        '''
        integrated_exponent = exponent + 1
        intergrated_coefficient = coefficient / integrated_exponent
       # print(inco)
        calc = intergrated_coefficient * ((value) ** integrated_exponent)
        list.append(calc)
       # print(list)
        '''
        print()```
        print()```
        '''

    elif i == 4:
        coefficient = -1 / 16
        exponent = (i-1)*2
        '''
        print(coefficient)
        print(exponent)
        '''
        integrated_exponent = exponent + 1
        intergrated_coefficient = coefficient / integrated_exponent
        '''
        print(intergrated_coefficient)
        '''
        calc = intergrated_coefficient * ((value) ** integrated_exponent)
        list.append(calc)
       # print(list)
        '''print()```
        print()
        '''


    else:

        for o in range(3, 50):
            value = 0.5
            coefficient = coefficient * ((0.5 - o) / (o + 1))
            '''
            print(-abs(coefficient))
            '''
            exponent = 2*(o+1)
            '''
            print(coefficient)
            print(exponent)
            '''
            integrated_exponent = exponent + 1
            intergrated_coefficient = -abs(coefficient)/ integrated_exponent
            '''
            print(intergrated_coefficient)
            '''
            calc = intergrated_coefficient * ((value) ** (integrated_exponent))
            list.append(calc)

            #print(list)
            '''
            print()```
            print()```
            '''


total = 0
for n in range(0, len(list)):
    total = total + list[n]
    '''
```print(total)```
'''
pi = (Decimal(total) -(Decimal(math.sqrt(3))/8))*12
print(pi)
'''
```print(list)```
'''
