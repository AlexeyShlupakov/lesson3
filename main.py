# Задание 1
def div(*args):
    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        deistvie = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Недопустимый делитель. На ноль делить нельзя!"
    return deistvie
print(f'result  {div()}')

# Задание 2
name_2 = str(input("Введите свое имя: "))
surname_2 = str(input("Введите свою фамилию: "))
year_2 = str(input("Введите свой возраст: "))
city_2 = str(input("Введите город проживания: "))
email_2 = str(input("Введите свой email: "))
phone_2 = str(input("Введите номер своего телефона: "))

def my_func(name,surname,year,city,email,phone):
    return ' '.join([ "Имя: ", name, ". Фамилия: ", surname, ". Возраст: ", year, ". Город: ", city, ". email адрес: ", email, ". Номер телефона: ", phone, "."])

print(my_func(name=name_2, surname=surname_2, year=year_2, city=city_2, email=email_2, phone=phone_2))

# Задание 3
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')

# Задание 4 1
def my_func(x, y):
    var1 = x**y
    return var1

print(my_func(int(input("Введите x: ")), int(input("Введите y: "))))

# Задание 4 2
def my_func(x, y):
    var2 = 1
    i = 1
    while i <= abs(y):
        var2 *= x
        i += 1
    return 1 / var2

print(my_func(int(input("Введите x: ")), int(input("Введите y: "))))

# Задание 5
def my_func ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа, цифры, либо введите Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Общая введенная сумма равна -  {sum_res}')
    print(f'Итоговая сумма равна - {sum_res}')

my_func ()

# Задание 6
a = input("Введите слова ")
def func(a):
    return a.title()


print(func(a))

# Задание 7
def int_func ():
    word = input("Введите слова ")
    print(word.title())
    return
int_func()
