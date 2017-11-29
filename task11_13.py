import math
print("===============================")
print("Task #11")
print("===============================")

def grad2rad(grad):
    rad = grad * math.pi/180
    return rad


angle1= 60
angle2 = 45
angle3 = 40
result1= math.cos(grad2rad(angle1))
result2= math.cos(grad2rad(angle2))
result3= math.cos(grad2rad(angle3))
print("Косинус угла в %.0f градусов = %.2f" % (angle1,result1))
print("Косинус угла в %.0f градусов = %.2f" % (angle2,result2))
print("Косинус угла в %.0f градусов = %.2f" % (angle3,result3))


print("===============================")
print("Task #12")
print("===============================")

def summa(n):
    n1 = n % 10
    n2 = n % 100 // 10
    n3 = n // 100
    summa = n1 + n2 + n3
    return summa

n = 123
result = summa(n)
print("Сумма цыфер числа %.0f = %.0f" % (n, result))


print("===============================")
print("Task #13")
print("===============================")

def result (ab, ac):
    gipotenuza = math.sqrt(ab ** 2 + ac ** 2)
    area = (ab * ac) / 2
    perimetr = ab + ac + gipotenuza
    power = "\u00B2"
    print("Вводные данные: катеты прямоугольного треугольника равны %.0fсм и %.0fсм" % (ab, ac))
    print ("")
    print("Вопрос: найти площадь и периметр треугольника")
    print ("")
    print("Ответ: площадь равна %.2fсм%s, а периметр %.2fсм" % (area, power, perimetr))

ab = 5
ac = 10
print_result = result(ab, ac)