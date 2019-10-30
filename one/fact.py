"""def fact(num: int):
    nums = range(1, num+1)
    m = 1
    for n in nums:
        print("n" + str(n))
        m = m * n 
        print("m" + str(m))
    return m
print(fact(3))"""




def fact(num: int):
    if num>1:
        return num * int(fact(num-1))
    elif num == 1:
        return 1

print(fact(10))