import random

print("===============================")
print("Task #7")
print("===============================")

def get_num_fibon(n):
    f1 = 1
    f2 = 2
    list_fibon = [1, 2]
    for i in range(3,n+1):
        b = f1
        f1 = f2
        f2 = b+f1
        list_fibon.append(f2)
    return list_fibon

check_number = 10
list_fibon = get_num_fibon(check_number)
sum_list_fibon = sum(list_fibon)
print("The sum of the first %d numbers of the Fibonacci series: %s\nWill be = %d" % (check_number, list_fibon, sum_list_fibon))


print("===============================")
print("Task #8")
print("===============================")

list = [1, 2, 3, 4, 11, 6, 7, 8, 9, 0]

def is_swap_max_min_lst(list):
    list_swap = list[:]
    maxi = list_swap.index(max(list_swap))
    mini = list_swap.index(min(list_swap))
    list_swap[maxi], list_swap[mini] = list_swap[mini], list_swap[maxi]
    return list_swap

result = is_swap_max_min_lst(list)
print("Swap the maximum and minimum number of list: %s" % list)
print("Result:\t\t\t\t\t\t\t\t\t\t %s" % result)


print("===============================")
print("Task #9")
print("===============================")

def get_list_random_num(low_range, upp_range, low_random, upp_random):
    list = [random.randint(low_random,upp_random) for x in range(low_range, upp_range)]
    return list

def get_list_normaliz(list):
    maxi_abs = max(list, key=abs)
    list_normaliz = [abs(round(x / maxi_abs, 2)) for x in list]
    return list_normaliz

list_random_num = get_list_random_num(0, 10, -20, 20)
list_normaliz = get_list_normaliz(list_random_num)

print("A list of random numbers:\t\t\t\t\t\t\t%s" % list_random_num)
print("Normalized list of random numbers in the interval:  %s" % list_normaliz)
