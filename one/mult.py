"""from itertools import product
mult = int(input("input an integer")) + 1
num, Num = list(range(1, mult)), list(range(1, mult))

for i in num:
    list_num  = []
    for j in Num:
        if j <= i:
            x = i*j
            list_num.append(x)
    print(list_num)"""

"""def multiply(num):
   len_num = len(str(num))
   span = len(str(num*num))
   outer = list(range(1, num + 1))
   for i in outer:
       line_str = ''
       j=1
       while (j <= (i+1)):
           product = (str(j).rjust(len_num) + ' x ' + str(i).rjust(len_num) + ' = ' + str(i*j).rjust(len_num)) + ' '
           line_str += product.ljust(span)
           j+=1
       print(line_str)

multiply(6)"""

def multiply(num: int):
    len_num = len(str(num))
    n = num + 1
    m = 0
    while m <= n:
        line_str = ''
        l=1
        while l <= m:
            product = (str(l).rjust(len_num) + ' x ' + str(m).rjust(len_num) + ' = ' + str(m*l).rjust(len_num)) + ' '
            line_str += product.ljust(len(str(num*num)))
            l+=1
        print(line_str)
        m += 1
multiply (10)