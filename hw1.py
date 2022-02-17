 
#____________________________________________________________________________________________
print('The path 1 of homework of Lesson1 - 3 варианта : ')

def convert_time(duration:int)-> str:
    if duration<60:
       res_date=(duration, 'сек')
    elif duration <3600:
        res_date=(duration//60, 'мин', duration%60, 'сек')
    elif duration <86400:
        res_date=(duration//3600, 'час', duration%3600//60, 'мин', duration%3600%60, 'сек')
    elif duration<31536000:
        res_date = (duration//86400, 'дн', duration%86400//3600, 'час', duration%86400%3600//60, 'мин', duration%86400%3600%60, 'сек')
    elif duration >31536000:
        res_date=('слишком большой промежуток больше 1 года')
    res_date = str (res_date)
    res_date= res_date.replace(',','')
    res_date = res_date.replace ( "'",'' )
    res_date = res_date.replace ( "(", '' )
    res_date = res_date.replace ( ")", '' )
    return str(res_date)

def convert_time2(duration:int)-> str: # через список - так код меньше
    if duration<60:
       my_list=[duration, 'сек']
    elif duration <3600:
       my_list=[duration//60, 'мин', duration%60, 'сек']
    elif duration <86400:
        my_list =[duration//3600, 'час', duration%3600//60, 'мин', duration%3600%60, 'сек']
    elif duration<31536000:
        my_list = [duration//86400, 'дн', duration%86400//3600, 'час', duration%86400%3600//60, 'мин', duration%86400%3600%60, 'сек']
    return my_list

print('Вариант 1')
duration=53
print(duration)
print (convert_time(duration))
duration=153
print(duration)
result=convert_time(duration)
print(result)
duration=4153
print(duration)
result=convert_time(duration)
print(result)
duration=400153
print(duration)
result=convert_time(duration)
print(result,'\n')


print('Вариант 2')
duration=53
print(duration)
print(*convert_time2(duration), sep=' ')# sep - Подсмотрел в Google
duration=153
print(duration)
print(*convert_time2(duration), sep=' ')
duration=4153
print(duration)
print(*convert_time2(duration), sep=' ')
duration=400153
print(duration)
print(*convert_time2(duration), sep=' ')
print ('\n')


print('<<<<Ручной ввод с клавиатуры Еще Вариант 3+>>>>')
try: # Проверка на ошибку, забегая вперед (привычка из VB), google в помощь
    duration_manual=input(f"Введите промежуток времени в секундах (целым числом):" '\n')
    result=convert_time(int(duration_manual))# преобразуем в целое число
    print ( result )
except ValueError:
    print(type(duration_manual))
    print("Ошибка ввода! (ввод только цифрами), перезапустите расчет")
else: pass
print('<<<<Ручной ввод с клавиатуры Еще Вариант 3+ еще разок!>>>>')
while True:
    try:  # Проверка на ошибку, забегая вперед (привычка из VB), google в помощь
        duration_manual = input ( f"Введите промежуток времени в секундах (целым числом):" '\n' )
        result = convert_time ( int ( duration_manual ) )  # преобразуем в целое число
        print ( result )
    except ValueError:
        print ( type ( duration_manual ) )
        print ( "Ошибка ввода! (вводите только цифры)" )
    else:

        break
print ('\n')
print ( 'The first task of the homework of lesson 1 is successfully done 17.02.2022' )
print ('\n')
#____________________________________________________________________________________________
print('The path 3 of homework of Lesson1')
print ('\n')

def transform_string(number:int) ->str:
    if number%10==0:
        return str(number)+" процентов"
    elif number >=11 and number <=14:
        return str(number) + " процентов"
    elif number%10 ==1:
        return str(number) + " процент"
    elif number%10 <=4:
        return str(number) + " процента"
    elif number%10 <=9:
        return str(number) + " процентов"

for n in range(1, 101):# по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
print ('\n')
print("The third task of the homework of lesson 1 is successfully done 17.02.2022")
#____________________________________________________________________________________________

def sum_list_1(dataset: list) -> int:
    summ_del_7 = 0
    for elem in range(len(dataset)):
        summ = 0
        number = dataset[elem]
        while (number != 0):
            summ = summ + number % 10
            number = number // 10
        if summ % 7 == 0:
            summ_del_7 = + dataset[elem]
    return summ_del_7

def sum_list_2(dataset: list) -> int:
    sum_del_7_2 = 0
    for i in range(len(dataset)):
        dataset[i] = dataset[i] +17  # Прибавил число 17 к каждому элементу
    # print ('к кубам прибавляем 17')
    # print(dataset)
    for elem in range(len(dataset)):
        sum = 0
        num = dataset[elem]
        while (num != 0):  # До тех пока не станет ноль
            sum = sum + num % 10  # берем первую цифру
            num = num // 10  # сдвигаемся на следующую цифру
        if sum % 7 == 0:
            sum_del_7_2 = +dataset[elem]
    return sum_del_7_2
my_list = []  # объявляем пустой лист
for cub_X in range(1, 1000, 2):
    my_list.append(cub_X ** 3)
# print("Кубы нечетных чисел от 1 до 1000")
# print(my_list) # Отображается список кубов нечетных чисел от 1 до 1000

result_1 = sum_list_1(my_list)
result_2 = sum_list_2(my_list)

print(' Общая сумма чисел, сумма чисел которых делится нацело на 7')
print(result_1)  # По моему избыточная переменная
print(' Общая сумма чисел, сумма чисел которых делится нацело на 7, после прибавки 17 к кубам')
print(result_2, '\n')
print('The second part of the homework of lesson 1 is successfully done 17.02.2022')

