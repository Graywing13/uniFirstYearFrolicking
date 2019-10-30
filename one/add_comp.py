def add_comp(num): 
    if num <= 3:
        return 0
    else:
        comp_num_sum = 0
        for n in range(3, num+1): 
            for m in range(2, n):
                if (n % m) == 0:
                    comp_num_sum += n
                    break
    return comp_num_sum

list_to_test = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 50]
for num in list_to_test:
    print("The sum of all composite numbers <= {} is ".format(num) + str(add_comp(num)))