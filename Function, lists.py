# Python HW 5 Functions, Lists
# - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.

# 1. Написать скрипт который в создаст список целых чисел.
import random

int_list = list(range(70))
print('int_list', int_list)
# 2. Написать скрипт который в создаст список целых чётных чисел.
even_list = [e for e in range(0, 70) if e%2 == 0]
print('even_list', even_list)
# 3. Написать скрипт который в создаст список целых нечётных чисел.
odd_list = [o for o in range(0, 70) if o%2 == 1]
print('odd_list', odd_list)
# 4. Написать скрипт который из списка целых чисел выведет чётные числа.
for p in int_list:
    if p%2 ==0:
        print('4: ', p)
# 5. Написать скрипт который из списка целых чисел выведет нечётные числа.
for d in int_list:
    if d%2 ==1:
        print('5: ', d)
# 6. Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
for g in int_list:
    if g%2 ==0 and g%5 == 0:
        print('6: ', g)
# 7. Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
even_list_2 = [g for g in int_list if g%2 ==0 and g%5 == 0]
print('7: ', len(even_list_2))

# 8. Написать скрипт который в создаст список целых рандомных чисел.

import random
rand_list = []

rand = random.randint(0, 70)
for i in range(rand):
        rand_list.append(random.randint(0, 70))
        print('rand= ', rand)
print('rand_list: ',rand_list)


# 9. Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.

print#(split(int_list, 5))

# 10. Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
# 11. Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
# 12. Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
# 13. Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”
# 14. Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
# 15. Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA. Free implementation of function body logic
#
#
#
# 16. Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
# 17. Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.
# 18.  Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.
# 19. Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации
# 20. Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно),
# 21. Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)
# 22. Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
# 23. Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$
# 24. Написать скрипт который создаст список имён мужчин из gender.
# 25. Написать скрипт который создаст список имён женщин из gender.
# 26. Написать скрипт который создаст список имён неженатых мужчин из family.
# 27. Написать скрипт который создаст список имён незамужних женщин из family.
# 28. Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций
# 29. Реализуйте пункт 28 через через функции.
# 30. Поешьте и выспитесь)