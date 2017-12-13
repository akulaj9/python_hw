print("===============================")
print("Task #4")
print("===============================")

n = int(input("Enter the number in which you want to find product is not even digits:"))

def is_even(n):
    return n % 2 == 0

def get_product_odd_num(n):
    product = 1
    while (n > 0):
        digit = n % 10
        n = n // 10
        if not is_even(digit):
            product *= digit
    return product
result = get_product_odd_num(n)
print("The product does not even numbers %d will be %d" % (n, result))


print("===============================")
print("Task #5")
print("===============================")

check_num = 10

input_data = input("Enter two numbers and find out how close to the top %0.2f (x, y):" % check_num)

x, y = [float(x.strip()) for x in input_data.split(',')]

def get_nearest_num(x, y, check_num):
    differ_x = abs(check_num - x)
    differ_y = abs(check_num - y)
    if differ_x > differ_y:
        return y
    elif differ_x == differ_y:
        return x, y
    else:
        return x

result = get_nearest_num(x, y, check_num)

if result == x or result == y:
    print("The closest number to %0.2f will be %0.2f" % (check_num, result))

else:
    print("The closest number to %0.2f will be %0.2f and %0.2f" % (check_num, x, y))


print("===============================")
print("Task #6")
print("===============================")
