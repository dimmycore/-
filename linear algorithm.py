import math

print('1-прямоугольник, 2-треугольник, 3-круг')
figure = input('выберите фигуру:')

if figure == '1':
    a = float(input('a= '))
    b = float(input('b= '))
    print('площадь: %.2f' % (a * b))
elif figure == '2':
    a = float(input('a= '))
    b = float(input('b= '))
    c = float(input('c= '))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('площадь: %.2f' % s)

elif figure == '3':
    r = float(input('радиус круга:'))
    print('площадь: %.2f' % (math.pi * r ** 2))

else:
    print('ошибка ввода')
