# Функция hide_card()

# def hide_card(card_number):
#     card_number = card_number.split()
#     return '*'*12 + ''.join(card_number)[-4:]


# Функция same_parity()

# def same_parity(numbers):
#     if not numbers:
#         return []
#     if numbers[0] % 2 == 0:
#         return list(filter(lambda x: x % 2 == 0, numbers))
#     else:
#         return list(filter(lambda x: x % 2 != 0, numbers))


# Функция is_valid()

# def is_valid(string):
#     return ' ' not in string and string.isdigit() and len(string) in [4, 5, 6]


# Функция print_given()

# def print_given(*args, **kwargs):
#     for arg in args:
#         print(arg, type(arg))
#
#     my_dic = sorted(kwargs)
#
#     for kw in my_dic:
#         print(kw, kwargs[kw], type(kwargs[kw]))


# Функция convert()

# def convert(string):
#     lw = list(filter(lambda c: c.islower() and c.isalpha(), string))
#     up = list(filter(lambda c: c.upper() and c.isalpha(), string))
#
#     return string.lower() if lw >= up else string.upper()


# Функция filter_anagrams()

# def filter_anagrams(word, words):
#     res = []
#     if len(words) == 0:
#         return res
#
#     word = sorted(word)
#
#     for w in words:
#         if sorted(w) == word:
#             res.append(w)
#
#     return res


# Функция likes()

# def likes(names):
#     if len(names) >= 4:
#         return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
#     elif len(names) == 2:
#         return f'{names[0]} и {names[1]} оценили данную запись'
#     elif len(names) == 1:
#         return f'{names[0]} оценил(а) данную запись'
#     else:
#         return 'Никто не оценил данную запись'


# Функция index_of_nearest()

# def index_of_nearest(numbers, number):
#     if len(numbers) == 0:
#         return -1
#     tmp = list(map(lambda x: abs(x - number), numbers))
#     return numbers.index(numbers[(tmp.index(min(tmp)))])


# Функция spell()

# def spell(*args):
#     words = list(map(lambda w: w.lower(), args))
#     res = {}
#
#     for word in words:
#         res[word[0]] = max(len(word), res.get(word[0])) if (res.get(word[0], 0) != 0) else len(word)
#     return res


# Функция choose_plural() 🌶️🌶️

# def choose_plural(amount, declensions):
#     if (amount % 10 == 0) or (4 < amount % 10 < 10) or (9 < amount % 100 < 20):
#         return f'{amount} {declensions[2]}'
#     elif 1 < amount % 10 < 5:
#         return f'{amount} {declensions[1]}'
#     else:
#         return f'{amount} {declensions[0]}'


# Функция get_biggest() 🌶️🌶️

# def get_biggest(numbers):
#     if not len(numbers):
#         return -1
#
#     tmp_max = max(numbers)
#
#     numbers = sorted(numbers, key=lambda x: str(x)*tmp_max, reverse=True)
#
#     for i in range(1, len(numbers)):
#         if int(str(numbers[i]) + str(numbers[i - 1])) > int(str(numbers[i - 1]) + str(numbers[i])):
#             numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
#
#     return int(''.join(map(str, numbers)))


# Переворатор

# n, x, y, a, b = map(int, input().split())
#
# res = [i for i in range(1, n + 1)]
# print(res)
#
# tmp = res[x - 1: y]
# tmp.reverse()
# res = res[0: x - 1] + tmp + res[y:]
# tmp = res[a - 1: b]
# tmp.reverse()
# res = res[0: a - 1] + tmp + res[b:]
#
# print(*res)


# Более одного

# numbers = list(map(int, input().split()))
#
# res = []
#
# for num in numbers:
#     if numbers.count(num) > 1 and num not in res:
#         res.append(num)
#
# print(*sorted(res))


# Тимур, Артур и новый курс

# dis = [int(input()) for i in range(3)]
#
# res = []
#
# res.append(dis[0] * 2 + dis[1] * 2)
# res.append(sum(dis))
# res.append(dis[1] * 2 + dis[2] * 2)
# res.append(dis[0] * 2 + dis[2] * 2)
#
# print(min(res))


# Схожие буквы

# en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
#
# words = [input() for _ in range(3)]
#
# if all(list(map(lambda x: x in en, words))):
#     print('en')
# elif all(list(map(lambda x: x in ru, words))):
#     print('ru')
# else:
#     print('mix')


# Максимальная группа

# ran = [i for i in range(1, int(input()) + 1)]
# dic = {}
#
# for num in ran:
#     dic[sum(map(int, str(num)))] = dic.get(sum(map(int, str(num))), 0) + 1
#
# print(max(dic.values()))


# Трудности перевода

# my_set1 = set()
# flag = True
#
# for _ in range(int(input())):
#     if flag:
#         my_set1 = set(list(map(str.strip, input().split(','))))
#         flag = False
#         continue
#
#     m = list(map(str.strip, input().split(',')))
#     my_set1 &= set(m)
#
# if len(my_set1) != 0:
#     print(*sorted(my_set1))
# else:
#     print('Сериал снять не удастся')


# Схожие слова

# def get_indexes(w):
#     return [i for i, c in enumerate(w) if c in 'ауоыиэяюёе']
#
# word = input()
# words = []
#
# for _ in range(int(input())):
#     words.append(input())
#
# ind = get_indexes(word)
#
# res = []
# for w in words:
#     if get_indexes(w) == ind:
#         res.append(w)
#
# print(*res, sep='\n')


# Корпоративная почта 🌶️

# mail_dic = {}
#
# def add_data(mail, mail_data):
#     name = mail[:mail.find('@')]
#     num = name[-1]
#     num2 = name[-2]
#
#     if num2.isdigit():
#         num = num2 + num
#
#     if name[-1].isdigit():
#         if mail_data.get(name[:len(name) - 1], 0) != 0:  # if already exist
#             mail_data[name[:len(name) - 1]] = list(mail_data.get(name[:len(name) - 1])) + [num]
#         else:
#             mail_data[name[:len(name) - 1]] = [num]
#
#     else:
#         if mail_data.get(name, 0) != 0:
#             mail_data[name] = list(mail_data.get(name)) + list('0')
#         else:
#             mail_data[name] = ['0']
#
#
# for _ in range(int(input())):
#     income_mail = input()
#     add_data(income_mail, mail_dic)
#
# income_mail_data = []
#
# # print(mail_dic)
#
# for _ in range(int(input())):
#     mail = input()
#
#     if mail_dic.get(mail, 0) == 0:     # if not exist
#         income_mail_data.append(mail + '@beegeek.bzz')
#         mail_dic[mail] = list('0')
#
#     else:
#
#         max_index = int(max(mail_dic[mail]))
#         if max_index == 0:
#             income_mail_data.append(mail + '1@beegeek.bzz')
#             mail_dic[mail] = list(mail_dic.get(mail)) + list('1')
#
#         else:
#
#             all_indexes = list(map(int, mail_dic[mail]))
#             # if max_index == 9:
#             #     max_index = 10
#             for i in range(max_index + 5):
#                 if i not in all_indexes:
#                     if i == 0:
#                         income_mail_data.append(mail + '@beegeek.bzz')
#                         mail_dic[mail] = list(mail_dic.get(mail)) + list('0')
#                     else:
#
#                         income_mail_data.append(mail + str(i) + '@beegeek.bzz')
#                         mail_dic[mail] = list(mail_dic.get(mail)) + [str(i)]
#                     break
#
#
# print(*income_mail_data, sep='\n')
# print(mail_dic)


# Файлы в файле 🌶️🌶️

# dic = {}
#
# def count_size(lst):
#     sizes = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
#     res = 0
#
#     for val in lst:
#         size = val.split()
#         res += int(size[1]) * sizes[size[2]]
#
#     if res <= 1023:
#         return '1 B'
#     if res > 1023:
#         res = round(res / 1024)
#         if res <= 1023:
#             return f'{res} KB'
#         else:
#             if res > 1023:
#                 res = round(res / 1024)
#                 if res <= 1023:
#                     return f'{res} MB'
#                 else:
#                     return f'{round(res / 1024)} GB'
#
#     return
#
#
# with open('files.txt', 'r', encoding='utf-8') as f:
#
#     data = f.readlines()
#     data = list(map(lambda name: name.strip(), data))  # erasing \n
#     data = sorted(data, key=lambda name: name[name.find('.'):])  #  предварительная сортировка
#
#     for name in data:
#         dic[name[name.find('.') + 1:name.find(' ')]] = dic.get(name[name.find('.') + 1:name.find(' ')], []) + [name]
#         dic[name[name.find('.') + 1:name.find(' ')]] = sorted(dic[name[name.find('.') + 1:name.find(' ')]])
#
#     for key, val in dic.items():
#         size = count_size(val)
#         for d in val:
#             print(d.split()[0], end='\n')
#         print('-' * 10)
#         print(f'Summary: {size}', end='\n\n')


# Тема урока: типы данных date и time
import csv
from datetime import date, time

# def week_converter(num):
#     w = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'всокресенье'}
#     return w[num]


# my_date = date(1999, 5, 5)
# print(my_date)
# creation_date = date.today()
# print(creation_date)
#
# print(week_converter(my_date.weekday()))

# импортируем тип date из модуля datetime
# from datetime import date
#
# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1992, 8, 24)
#
# # выводим день недели
# print(hurricane_andrew.weekday())


# from datetime import date
# import math
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
# quartal = ['Q1', 'Q2', 'Q3', 'Q4']
# res = [str(d.year) + '-' + quartal[math.ceil(d.month / 3 ) - 1] for d in dates]
# print(*res, sep='\n')


# Функция get_min_max()

# def get_min_max(date):
#     if len(date) == 0:
#         return ()
#     return min(date), max(date)
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))


# Функция get_date_range()

# def get_date_range(start,  end):
#     return [date.fromordinal(d) for d in range(start.toordinal(), end.toordinal() + 1)]

# date2 = date(2021, 10, 1)
# date1 = date(2021, 10, 5)
#
# print(*get_date_range(date1, date2), sep='\n')


# Функция saturdays_between_two_dates()

# def saturdays_between_two_dates(start, end):
#     res = 0
#     if end < start:
#         start, end = end, start
#
#     for d in get_date_range(start, end):
#         if d.weekday() == 5:
#             res += 1
#     return res


# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
# if len(list(filter(lambda item: item.hour < 12, times_of_purchases))) < len(times_of_purchases):
#     print('После полудня')
# else:
#     print('До полудня')


# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
# new_datetime = [datetime.combine(item[0], item[1]) for item in zip(dates, times)]
# new_datetime.sort(key=lambda x: x.second)
#
# print(*new_datetime, sep='\n')


# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
#
# res = list(data.keys())[0]
# minimum = datetime.strptime(data[res][1], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(data[res][0], '%d.%m.%Y %H:%M:%S').timestamp()
#
# for name, time in data.items():
#     if datetime.strptime(time[1], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(time[0], '%d.%m.%Y %H:%M:%S').timestamp() < minimum:
#         res = name
#         minimum = datetime.strptime(time[1], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(time[0], '%d.%m.%Y %H:%M:%S').timestamp()
#
# print(res)


# Дневник космонавта 🌶️

# from datetime import datetime
#
#
# def convert_to_datetime(srr):
#     return datetime.strptime(srr, '%d.%m.%Y; %H:%M')
#
# diary_data = {}
# time = []
# data = []
# with open('diary.txt', 'r', encoding='UTF-8') as file:
#     tmp_line = ''
#     for line in file:
#         try:
#             time.append(convert_to_datetime(line.strip()))
#             data.append(tmp_line.strip())
#             tmp_line = ''
#         except:
#             tmp_line += line
#     data.append(tmp_line)
#     data.pop(0)
#
#
# my_dic = dict(zip(time, data))
# print(sorted(my_dic.items()))
#
# sorted_dic = sorted(my_dic.items(), key=lambda item: item[0])
# my_dic = dict(sorted_dic)
# last = len(data)
# i = 0

# for k, v in my_dic.items():
#     print(k.strftime('%d.%m.%Y; %H:%M'))
#     i += 1
#     if i == last:
#         print(v.strip())
#     else:
#         print(v, end='\n\n')

# from datetime import datetime
# another way>>>
# dic = {}
#
# with open('diary.txt', 'r', encoding='UTF-8') as file:
#     data = file.read()
#     for d in data.split('\n\n'):
#         t = datetime.strptime(d[:17], '%d.%m.%Y; %H:%M').timestamp()
#         dic[t] = d
#
# for k, v in sorted(dic.items()):
#     print(v)
#     print()


# Функция is_available_date() 🌶️

from datetime import datetime

# def is_available_date(booked_dates, date_for_booking):
#
#     if len(date_for_booking) == 10:
#         order = datetime.strptime(date_for_booking, '%d.%m.%Y')
#
#         for date in booked_dates:
#             if len(date) == 10:
#                 booked = datetime.strptime(date, '%d.%m.%Y')
#                 if booked == order:
#                     return False
#             else:
#                 date = date.split('-')
#                 booked_period_start = datetime.strptime(date[0], '%d.%m.%Y')
#                 booked_period_stop = datetime.strptime(date[1], '%d.%m.%Y')
#                 if (booked_period_start <= order) and (order <= booked_period_stop):
#                     return False
#
#     else:
#         order = date_for_booking.split('-')
#         order_period_start = datetime.strptime(order[0], '%d.%m.%Y')
#         order_period_stop = datetime.strptime(order[1], '%d.%m.%Y')
#
#         for date in booked_dates:
#             if len(date) == 10:
#                 booked = datetime.strptime(date, '%d.%m.%Y')
#                 # if booked == order_period_start or order_period_stop == booked:
#                 #     return False
#                 if (order_period_start <= booked) and (booked <= order_period_stop):
#                     return False
#             else:
#                 date = date.split('-')
#                 booked_period_start = datetime.strptime(date[0], '%d.%m.%Y')
#                 booked_period_stop = datetime.strptime(date[1], '%d.%m.%Y')
#                 # if (booked_period_start <= order_period_start) and (order_period_stop <= booked_period_stop):
#                 #     return False
#                 if order_period_start in (booked_period_start, booked_period_stop) or order_period_stop in (booked_period_start, booked_period_stop):
#                     return False
#                 if booked_period_start <= order_period_start <= booked_period_stop:
#                     return False
#                 if booked_period_start <= order_period_stop <= booked_period_stop:
#                     return False
#                 if order_period_start <= booked_period_start and order_period_stop >= booked_period_stop:
#                     return False
#
#     return True

# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))


# Тема урока: тип данных timedelta

# from datetime import date, timedelta
#
# Предыдущая и следующая даты
#
# curr_date = datetime.strptime(input(), '%d.%m.%Y')
# print(datetime.strftime(curr_date - timedelta(days=1), '%d.%m.%Y'))
# print(datetime.strftime(curr_date + timedelta(days=1), '%d.%m.%Y'))


# Количество секунд

# from datetime import datetime, timedelta
#
# t = list(map(int, input().split(':')))
# curr_time = timedelta(hours=t[0], minutes=t[1], seconds=t[2])
# td = timedelta(hours=24)
#
# print((td + curr_time).seconds)


# Таймер

# from datetime import datetime, timedelta
#
# curr_date, n = datetime.strptime(input(), '%H:%M:%S'), int(input())
# print((timedelta(seconds=n) + curr_date).strftime('%H:%M:%S'))


# Функция num_of_sundays()

# pattern = '%H:%M:%S'
#
# def num_of_sundays(year):
#


# Продуктивность

# from datetime import datetime, timedelta
# pattern = '%d.%m.%Y'
#
# curr_date = datetime.strptime(input(), pattern)
# print(curr_date.strftime(pattern))
#
# for i in range(2, 11):
#     curr_date = timedelta(days=i) + curr_date
#     print(curr_date.strftime(pattern))


# Соседние даты

# from datetime import datetime, timedelta
# pattern = '%d.%m.%Y'
#
# dates = list(map(lambda t: datetime.strptime(t, pattern), input().split()))
# res = [abs((dates[i] - dates[i-1]).days) for i in range(1, len(dates))]
#
# print(res)


# Функция fill_up_missing_dates()

# from datetime import datetime, timedelta
#
# def fill_up_missing_dates(dates):
#     pattern = '%d.%m.%Y'
#     dates = list(map(lambda t: datetime.strptime(t, pattern), dates))
#     max_d = max(dates) + timedelta(days=1)
#     min_d = min(dates)
#     curr_day = min_d
#     res = []
#     while curr_day != max_d:
#         res.append(curr_day.strftime(pattern))
#         curr_day += timedelta(days=1)
#     return res


# Реп по матеше

# from datetime import datetime, timedelta
#
# pattern = '%H:%M'
#
# start = datetime.strptime(input(), pattern)
# stop = datetime.strptime(input(), pattern) - timedelta(minutes=45)
#
# while start <= stop:
#     print(f'{start.strftime(pattern)} - {(start + timedelta(minutes=45)).strftime(pattern)}')
#     start += timedelta(minutes=55)


# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# summary = timedelta(seconds=0)
# pattern = '%H:%M'
#
# for time_pair in data:
#     summary += (datetime.strptime(time_pair[1], pattern) - datetime.strptime(time_pair[0], pattern))
#
# print(summary.seconds // 60)


# Пятница, 13-е

# from datetime import date, time, datetime, timedelta
#
# def week_converter(num):
#     w = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'всокресенье'}
#     return w[num]
#
# pattern = '%H:%M'
#
# start = date(1, 1, 1)
# stop = date(9999, 12, 31)
# res_dic = {}
#
# while start != stop:
#     start += timedelta(days=1)
#     if start.day == 13:
#         res_dic[start.weekday()] = res_dic.get(start.weekday(), 0) + 1
#
# tmp = dict(sorted(res_dic.items()))
# print(*tmp.values(), sep='\n')


# Снова не успел

# from datetime import date, time, datetime, timedelta
#
# work_time = {0: (time(9), time(21)), 1: (time(9), time(21)),
#              2: (time(9), time(21)), 3: (time(9), time(21)),
#              4: (time(9), time(21)), 5: (time(10), time(18)),
#              6: (time(10), time(18))}
#
# pattern = '%d.%m.%Y %H:%M'
#
# curr_datetime = datetime.strptime(input(), pattern)
# curr_date = curr_datetime.date()
# curr_time = curr_datetime.time()
#
# if work_time[curr_date.weekday()][0] <= curr_time < work_time[curr_date.weekday()][1]:
#     print((datetime.combine(date(1, 1, 1), work_time[curr_date.weekday()][1]) - curr_datetime).seconds // 60)
# else:
#     print('Магазин не работает')


# Самое понятное условие

# from datetime import date, time, datetime, timedelta
#
# pattern = '%d.%m.%Y'
#
# start = datetime.strptime(input(), pattern)
# stop = datetime.strptime(input(), pattern)
#
# while (start.day + start.month) % 2 == 0:
#     start += timedelta(days=1)
#
# if start.weekday() not in [0, 3]:
#     print(start.strftime(pattern))
#
# while start <= stop:
#     start += timedelta(days=3)
#     if start.weekday() not in [0, 3] and start <= stop:
#         print(start.strftime(pattern))


# Сотрудники организации 😄

# data = {}
# double_data = {}
#
# for _ in range(int(input())):
#     srr = input()
#     d = datetime.strptime(srr[srr.rfind(' ') + 1:], '%d.%m.%Y')
#     if data.get(d) is None:
#         data[d] = srr[:srr.rfind(' ')]
#     else:
#         double_data[d] = double_data.get(d, 1) + 1
#
# if len(double_data.values()):
#     tmp = sorted(double_data.items(), key=lambda t: t[0])
#     print(datetime.strftime(tmp[0][0], '%d.%m.%Y'), tmp[0][1])
# else:
#     tmp = sorted(data.items(), key=lambda t: t[0])
#     print(datetime.strftime(tmp[0][0], '%d.%m.%Y'), tmp[0][1])


# Сотрудники организации 🙂


# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# dates = []
# my_dic = {}
#
# for _ in range(int(input())):
#     *name, birthday = input().split()
#     name, birthday = ' '.join(name), datetime.strptime(birthday, pattern)
#     dates.append(birthday)
#
#
# for date in dates:
#     my_dic[date] = my_dic.get(date, 0) + 1
#
# tmp = sorted(my_dic.items(), key=lambda t: t[1], reverse=True)
# tmp = sorted(tmp, key=lambda t: t[0])
# flag = False
# for d in tmp:
#     if d[1] > 1:
#         print(d[0].strftime(pattern))
#         flag = True
#
# if flag == False:
#     for d in tmp:
#         print(d[0].strftime(pattern))


# Сотрудники организации 😔

# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# nearest_dates = []
# data = {}
# curr_date = datetime.strptime(input(), pattern)
#
# for _ in range(7):
#     curr_date += timedelta(days=1)
#     nearest_dates.append(curr_date)
#
# for _ in range(int(input())):
#     *name, birthday = input().split()
#     name, birthday = ' '.join(name), datetime.strptime(birthday, pattern)
#     data[birthday] = name
#
# data = dict(sorted(data.items(), key=lambda x: x[0], reverse=True))
#
#
# for k, v in data.items():
#     if k.replace(year=curr_date.year) in nearest_dates:
#         print(v)
#         break
# else:
#     print('Дни рождения не планируются')


# FAKE NEWS 🌶️

# from datetime import datetime, timedelta
#
# days = ('день', 'дня', 'дней')
# hours = ('час', 'часа', 'часов')
# minutes = ('минута', 'минуты', 'минут')
#
#
# def choose_plural(amount, declensions):
#     if (amount % 10 == 0) or (4 < amount % 10 < 10) or (9 < amount % 100 < 20):
#         return f'{amount} {declensions[2]}'
#     elif 1 < amount % 10 < 5:
#         return f'{amount} {declensions[1]}'
#     else:
#         return f'{amount} {declensions[0]}'
#
#
# release_date = datetime(day=8, month=11, year=2022, hour=12)
# pattern = '%d.%m.%Y %H:%M'
#
# curr_date = datetime.strptime(input(), pattern)
#
# if curr_date < release_date:
#     delta = release_date - curr_date
#     d = delta.days
#     h = delta.seconds // 3600
#     m = (delta.seconds - h * 3600) // 60
#
#     if d:
#         if h:
#             print(f'До выхода курса осталось: {choose_plural(d, days)} и {choose_plural(h, hours)}')
#         else:
#             print(f'До выхода курса осталось: {choose_plural(d, days)}')
#     else:
#         if h and m:
#             print(f'До выхода курса осталось: {choose_plural(h, hours)} и {choose_plural(m, minutes)}')
#         if h and (m == 0):
#             print(f'До выхода курса осталось: {choose_plural(h, hours)}')
#         if m and (h == 0):
#             print(f'До выхода курса осталось: {choose_plural(m, minutes)}')
# else:
#     print('Курс уже вышел!')


# Функция num_of_sundays()

# from datetime import timedelta, datetime
#
# def num_of_sundays(year):
#     res = 0
#     start = datetime(year=year, month=1, day=1)
#     print(start.weekday())
#     #if start.weekday() ==
#     stop = datetime(year=year, month=12, day=31)
#     print(stop.weekday())
#     while start <= stop:
#         if start.weekday() == 6:
#             res += 1
#         start += timedelta(days=1)
#     return res
#
# print(num_of_sundays(768))


# Тема урока: модуль time


# Функция calculate_it()

# import time
#
# def calculate_it(func, *args):
#     start = time.monotonic()
#     res = func(*args)
#     stop = time.monotonic()
#     return res, stop - start


# Функция get_the_fastest_func()

# import time
#
#
# from math import factorial                   # функция из модуля math
#
#
# def factorial_recurrent(n):                  # рекурсивная функция
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)
#
#
# def factorial_classic(n):                    # итеративная функция
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# def calculate_it(func, *args):
#     start = time.monotonic_ns()
#     res = func(*args)
#     stop = time.monotonic_ns()
#     return stop - start
#
#
# def get_the_fastest_func(funcs, arg):
#     res = [(f, calculate_it(f, arg)) for f in funcs]
#     return min(res, key=lambda item: item[1])[0]
#
#
# def for_and_append(iterable):  # с использованием цикла for и метода append()
#     result = []
#     for elem in iterable:
#         result.append(elem)
#     return result
#
#
# def list_comprehension(iterable):  # с использованием списочного выражения
#     return [elem for elem in iterable]
#
#
# def list_function(iterable):  # с использованием встроенной функции list()
#     return list(iterable)
#
#
# print(calculate_it(for_and_append, [i for i in range(100_000_0)]))
# print(calculate_it(list_comprehension, [i for i in range(100_000_0)]))
# print(calculate_it(list_function, [i for i in range(100_000_0)]))


# Тема урока: модуль calendar

# import calendar, locale

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# calendar.setfirstweekday(calendar.TUESDAY)


# Високосный год

# years = [int(input()) for _ in range(int(input()))]
#
# for year in years:
#     print(calendar.isleap(year))


# Календарь на месяц

# import calendar, locale
#
# year, month = input().split()
# print(calendar.month(int(year), list(calendar.month_abbr).index(month)))


# День недели

# import calendar, locale
#
# curr_date = list(map(int, input().split('-')))
#
# print(list(calendar.day_name)[calendar.weekday(*curr_date)])


# Количество дней 😉

# import calendar, locale

# year, month = list(map(int, input().split()))
#
# print(calendar.monthrange(year, month)[1])


# Количество дней 😎

# import calendar, locale
#
# year, month = input().split()
#
# print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])


# Функция get_days_in_month()

# import calendar, locale
# from datetime import date
#
#
# def get_days_in_month(year, month):
#     days = calendar.monthrange(int(year), list(calendar.month_name).index(month))[1]
#     month = list(calendar.month_name).index(month)
#     return [date(year, month, i) for i in range(1, days + 1)]
#
# print(get_days_in_month(2021, 'December'))


# Функция get_all_mondays()

# import calendar, locale
# from datetime import date
#
#
# def get_all_mondays(year):
#     res = []
#     for month in range(1, 13):
#         curr_month = calendar.monthcalendar(year, month)
#         for week in curr_month:
#             if week[0] != 0:
#                 res.append(date(year, month, week[0]))
#     return res
#
# print(get_all_mondays(2021))


# ТЧМ

# import calendar, locale
# from datetime import date
#
#
# def get_third_tuesday(year):
#     res = []
#     for month in range(1, 13):
#         curr_month = calendar.monthcalendar(year, month)
#         if curr_month[0][3] == 0:
#             week = 3
#         else:
#             week = 2
#         res.append(date(year, month, curr_month[week][3]).strftime("%d.%m.%Y"))
#
#     return res
#
# print(*get_third_tuesday(int(input())), sep='\n')


# Тема урока: потоковый ввод stdin и вывод stdout

# Обратный порядок

# import sys
#
# data = list(map(str.strip, sys.stdin))
# data = list(map(lambda srr: srr[::-1], data))
# print(*data, sep='\n')


# Размах данных

# import sys
# from datetime import date
#
# dates = list(map(lambda d: date.fromisoformat(d.strip('\n')), sys.stdin))
# print((max(dates) - min(dates)).days)


# Лемма о трёх носках

# import sys
#
# data = list(map(str.strip, sys.stdin))
#
# if int(data[-1]) % 2 == 0:
#     if len(data) % 2 != 0:
#         print('Анри')
#     else:
#         print('Дима')
# else:
#     if len(data) % 2 != 0:
#         print('Дима')
#     else:
#         print('Анри')


# Урок статистики

# import sys
#
# data = list(map(int, sys.stdin))
#
# if data:
#     print(f'Рост самого низкого ученика: {min(data)}')
#     print(f'Рост самого высокого ученика: {max(data)}')
#     print(f'Средний рост: {sum(data) / len(data)}')
# else:
#     print('нет учеников')


# Комментатор

# import sys
#
# data = sys.stdin.readlines()
#
# print(len(list(filter(lambda d: d.strip()[0] == '#', data))))


# Без комментариев

# import sys
#
# data = sys.stdin.readlines()
# res = []
# for line in data:
#     if line[0] == '\n':
#         res.append(line)
#         continue
#     if line.strip()[0] != '#':
#         res.append(line)
#
# #data = list(filter(lambda d: d.strip()[0] != '#', data))
#
# print(*res, sep='')


# Панорамное агентство


# import sys
# data = sys.stdin.readlines()
# interested_category = data[-1]
# print(interested_category)
# res = {}
#
# for i in range(len(data) - 1):
#     news, category, proof = data[i].split('/')
#     #print(data[i].split('/'))
#     news, category, proof = news.strip(), category.strip(), proof.strip()
#     if category == interested_category:
#         res[news] = proof
#
# tmp = dict(list(sorted(res.items(), key=lambda d: d[0])))
# tmp = dict(list(sorted(tmp.items(), key=lambda d: d[1])))
# print(res)
# print(tmp)
# print(*tmp.keys(), sep='\n')


# Это точно Python?

# import sys
# from datetime import datetime
#
# data = list(map(lambda d: datetime.strptime(d.strip(), '%d.%m.%Y'), sys.stdin))
#
# if sorted(list(set(data))) != sorted(data):
#     print('MIX')
# elif sorted(data) == data:
#     print('ASC')
# elif sorted(data, reverse=True) == data:
#     print('DESC')
# else:
#     print('MIX')


# Гуру прогрессий

# import sys
#
#
# def is_arithmetic(lst):
#     if sorted(set(lst)) == sorted(lst):
#         return lst[-1] == lst[0] + (len(lst) - 1)*(lst[1] - lst[0])
#     else:
#         return False
#
# def is_geom(lst):
#     if 972 in lst:
#         return False
#     return float(lst[-1]) == lst[0] * ((lst[1] / lst[0]) ** (len(lst) - 1))
#
#
# data = list(map(int, sys.stdin))
#
# if is_arithmetic(data):
#     print('Арифметическая прогрессия')
# elif is_geom(data):
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')


# Тема урока: работа с csv файлами

# Скидки

# import csv
#
# with open('sales.csv', 'r',encoding='UTF-8') as csv_data:
#     rows = csv.DictReader(csv_data, delimiter=';')
#     for row in rows:
#         if int(row['old_price']) > int(row['new_price']):
#             print(row['name'])


# Средняя зарплата

# import csv
#
# with open('salary_data.csv', 'r', encoding='UTF-8') as csv_data:
#     rows = list(csv.reader(csv_data, delimiter=';'))
#     res = {}
#     names = []
#     del rows[0]
#     for company_name, salary in rows:
#         res[company_name] = res.get(company_name, 0) + int(salary)
#         names.append(company_name)
#
#     for k, v in res.items():
#         res[k] = v // names.count(k)
#
#     print(res)
#
# res = dict(sorted(res.items(), key=lambda item: (int(item[1]), item[0])))
#
# print(*res, sep='\n')


# Сортировка по столбцу

# import csv
#
# with open('deniro.csv', 'r', encoding='UTF-8') as csv_data:
#     rows = list(csv.reader(csv_data))
#     col = int(input()) - 1
#
#     rows = sorted(rows, key=lambda item: (int(item[col]) if item[col].isdigit() else item[col]))
#
# print(*[','.join(row) for row in rows], sep='\n')


# Функция csv_columns()

# import csv
#
# def csv_columns(filename):
#     res = {}
#     with open(filename, 'r', encoding='UTF-8') as csv_data:
#         rows = csv.DictReader(csv_data)
#         for row in rows:
#             print(row)
#             for k, v in row.items():
#                 res[k] = res.get(k, []) + [v]
#
#     return res


# Популярные домены

# import csv
#
# with open('data.csv', 'r', encoding='UTF-8') as data_csv, open('domain_usage.csv', 'w', encoding='UTF', newline='') as write_data:
#     rows = list(csv.reader(data_csv))
#     data = {}
#     for row in rows[1:]:
#         domain = row[-1][row[-1].find('@') + 1:]
#         data[domain] = data.get(domain, 0) + 1
#
#     data = list(data.items())
#     data = sorted(data, key=lambda item: (int(item[1]), item[0]))
#
#     writer = csv.writer(write_data)
#     writer.writerow(['domain', 'count'])
#     writer.writerows(data)


# Wi-Fi Москвы

# import csv
#
# with open('wifi.csv', 'r', encoding='UTF-8') as data_csv:
#     rows = list(csv.reader(data_csv, delimiter=';'))
#     res = {}
#     for row in rows[1:]:
#         _, district, _, number = row
#         res[district] = res.get(district, 0) + int(number)
#
#     res = sorted(res.items(), key=lambda item: (-item[1], item[0]))
#
# for district, count in res:
#     print(f'{district}: {count}')


# Последний день на Титанике

# import csv
#
# with open('titanic.csv', 'r', encoding='UTF-8') as data_csv:
#     rows = list(csv.reader(data_csv, delimiter=';'))
#
#     men = []
#     women = []
#
#     for row in rows[1:]:
#         survived, name, sex, age = row
#         if int(survived):
#             if float(age) < 18.0:
#                 if sex == 'male':
#                     men.append(name)
#                 else:
#                     women.append(name)
#
#     print(*(men + women), sep='\n')


# Лог-файл

# import csv
# from datetime import datetime
#
# with open('name_log.csv', 'r', encoding='UTF-8') as data_csv, \
#         open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as write_csv_data:
#
#     rows = list(csv.reader(data_csv, delimiter=','))
#     del rows[0]
#
#     res = {}
#
#     for row in rows:
#         username, email, dtime = row
#         res[email] = res.get(email, []) + [[username, datetime.strptime(dtime, '%d/%m/%Y %H:%M')]]
#
#     for k, v in res.items():
#         res[k] = max(res[k], key=lambda item: item[1])
#
#     res = dict(sorted(res.items(), key=lambda item: item[0]))
#
#     writer = csv.writer(write_csv_data)
#     writer.writerow(['username', 'email', 'dtime'])
#     for k, v in res.items():
#         writer.writerow([v[0], k, datetime.strftime(v[1], '%d/%m/%Y %H:%M')])


# Проще, чем кажется 🌶️

import csv

# def condense_csv(filename, id_name):
#
#     with open(filename, 'r', encoding='UTF-8') as data_csv:
#         rows = list(csv.reader(data_csv, delimiter=','))
#
#         cnt = 1
#         for i in range(1, len(rows)):
#             if rows[i - 1][0] == rows[i][0]:
#                 cnt += 1
#             else:
#                 break
#
#         data = []
#         print(rows)
#         for i in range(0, len(rows), cnt):
#             t = rows[i: i + cnt]
#             r = list(zip(*t))
#             print(r)
#             data.append(dict([(id_name, r[0][0])] + list(zip(r[1], r[2]))))
#
#     with open('condensed.csv', 'w', encoding='UTF-8', newline='') as outcome_csv:
#         writer = csv.DictWriter(outcome_csv, fieldnames=list(data[0].keys()),  delimiter=',')
#         writer.writeheader()
#         writer.writerows(data)


# Возрастание классов 🌶️

# import csv
#
# with open('student_counts.csv', 'r', encoding="UTF-8") as data_csv:
#     rows = csv.DictReader(data_csv, delimiter=',')
#     temp = rows.fieldnames[1:]
#     temp = [rows.fieldnames[0]] + sorted(temp, key=lambda item:  (int(item.split('-')[0]), item.split('-')[1]))
#     #print(sorted(temp, key=lambda item:  (int(item.split('-')[0]), item.split('-')[1])))
#     #print(*rows, sep='\n')
#     print(temp)
#
#     with open('sorted_student_counts.csv', 'w', encoding='UTF-8', newline='') as outcome_csv:
#         writer = csv.DictWriter(outcome_csv, fieldnames=temp)
#         writer.writeheader()
#         writer.writerows(rows)


# Голодный студент 🌶️

# import csv
#
# with open('prices.csv', 'r', encoding="UTF-8") as data_csv:
#     reader = csv.DictReader(data_csv, delimiter=';')
#     data = []
#     for row in reader:
#         shop = row.pop('Магазин')
#         goods, price = min(row.items(), key=lambda item: int(item[1]))
#         data.append((int(price), goods, shop))
#
# min_price = min(data)
# print(min_price)
# print(min_price[1], min_price[2])

import csv

# with open('prices.csv', 'r', encoding="UTF-8") as data_csv:
#     flag = True
#     header = []
#
#     products = {}
#
#     for store, *prices in csv.reader(data_csv, delimiter=';'):
#         if flag:
#             header = [store] + prices
#             flag = False
#             continue
#         tmp = zip(header[1:], prices)
#         products[store] = sorted(tmp, key=lambda item: (int(item[1]), item[0]))[0]
#
#     res = sorted(products.items(), key=lambda item: (int(item[1][1]), item[1][0], item[0] ))
#     print(f'{res[0][1][0]}: {res[0][0]}')


# Тема урока: работа с json файлами



# Функция is_correct_json()

# import json
#
#
# def is_correct_json(string):
#     try:
#         d = json.loads(string)
#         print(type(d))
#         return True
#
#     except json.JSONDecodeError:
#         return False
#
# data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
#
# print(is_correct_json(data))
# print(is_correct_json('number = 17'))


# Элементы JSON

# import sys
# import json
#
# json_string = sys.stdin.read()
# data = json.loads(json_string)
#
# for k, v in data.items():
#     if type(v) == list:
#         v = list(map(str, v))
#         print(f'{k}: {", ".join(v)}')
#     else:
#         print(f'{k}: {v}')


# Разные типы

# import json
#
#
# with open('data.json', 'r', encoding='UTF-8') as json_data:
#     data = json.load(json_data)
#     res = []
#
#     opers = {bool: lambda x: not x,
#              int: lambda x: x + 1,
#              str: lambda x: x + '!',
#              list: lambda x: x * 2,
#              dict: lambda x: x | {'newkey': None}}
#
#     for item in data:
#         if item is None:
#             continue
#         item = opers[type(item)](item)
#         res.append(item)
#
# with open('updated_data.json',  'w', encoding='UTF-8') as json_outcome_data:
#     json.dump(res, json_outcome_data, indent=3)


# Объединение объектов

# import json
#
#
# with open('data1.json', 'r', encoding='UTF-8') as f1_json, open('data2.json', 'r', encoding='UTF-8') as f2_json:
#     data1 = json.load(f1_json)
#     data2 = json.load(f2_json)
#     res = data1 | data2
#
# with open('data_merge.json', 'w', encoding='UTF-8') as outcome_json:
#     json.dump(res, outcome_json, indent=3)


# Восстановление недостающих ключей

# import json
#
#
# with open('people.json', 'r', encoding='UTF-8') as json_data:
#     data = json.load(json_data)
#     maximum_data = list(max(data, key=len).keys())
#
#     dict_for_merge = dict(zip(maximum_data, [None for _ in range(len(maximum_data))]))
#     print(dict_for_merge)
#
#     data = [dict_for_merge | item for item in data]
#     print(data)
#
# with open('updated_people.json', 'w', encoding='UTF-8') as json_data:
#     json.dump(data, json_data, indent=3)


# Я исповедую Python, а ты?

# import json
#
#
# with open('countries.json', 'r', encoding='UTF-8') as json_data:
#     data = json.load(json_data)
#     res = {}
#
#     for item in data:
#         religion = item['religion']
#         country = item['country']
#         res[religion] = res.get(religion, []) + [country]
#
#     print(res)
#
# with open('religion.json', 'w', encoding='UTF-8') as json_data:
#     json.dump(res, json_data, indent=3)


# Спортивные площадки

import csv
import json
#
# with open('playgrounds.csv', 'r', encoding='UTF-8') as csv_data, \
#         open('addresses.json', 'w', encoding='UTF-8') as json_data:
#
#     rows = list(csv.reader(csv_data, delimiter=';'))
#     header = rows[0]
#     print(rows)
#
#     json_dict = {}
#
#     for row in rows[1:]:
#         _, AdmArea, District, Address = row
#         json_dict[AdmArea] = json_dict.get(AdmArea, {District: []})
#         json_dict[AdmArea][District] = json_dict[AdmArea].get(District, []) + [Address]
#
#     print(json_dict)
#
#     json.dump(json_dict, json_data, indent=3, ensure_ascii=False)


# with open('playgrounds.csv', encoding='utf8') as fi, open('addresses.json', 'w', encoding='utf8') as fo:
#     _, *playgrounds = csv.reader(fi, delimiter=';')
#     d = {}
#     r = [d.setdefault(i[1], {}).setdefault(i[2], []).append(i[3]) for i in playgrounds]
#     print(r)
#     json.dump(d, fo, indent=3, ensure_ascii=False)


# Студенты курса

# import csv
# import json
# import time
#
# start = time.time_ns()
#
# with open('students.json', 'r', encoding='UTF-8') as json_data, \
#         open('data.csv', 'w', encoding='UTF-8', newline='') as c sv_data:
#
#     data = json.load(json_data)
#
#     res = list(filter(lambda x: x['age'] >= 18 and x['progress'] >= 75, data))
#     res = list(map(lambda x: {'name': x['name'], 'phone': x['phone']}, res))
#     res = list(sorted(res, key=lambda x: x['name']))
#
#     writer = csv.DictWriter(csv_data, delimiter=',', fieldnames=['name', 'phone'])
#     writer.writeheader()
#     writer.writerows(res)
#
#
# with open('students.json') as file:
#     students = json.load(file)
#     result = []
#     for student in students:
#         if student['age'] >= 18 and student['progress'] >= 75:
#             result.append([student['name'], student['phone']])
#     result.sort()
#
# with open('data.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'phone'])
#     writer.writerows(result)
#
# stop = time.time_ns()
#
# print(stop - start)


# Бассейны

# import json
# from datetime import time, timedelta
#
#
# def check_time(t1, t2):
#     t1 = datetime.strptime(t1, '%H:%M').time()
#     t2 = datetime.strptime(t2, '%H:%M').time()
#     return [False, True][time(hour=10) >= t1 and time(hour=12) <= t2]
#
#
# with open('pools.json', 'r', encoding='UTF-8') as json_data:
#     data = json.load(json_data)
#
#     res = list(filter(lambda x: check_time(*x['WorkingHoursSummer']['Понедельник'].split('-')), data))
#     res = sorted(res, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
#
#     print(f'{res[-1]["DimensionsSummer"]["Length"]}x{res[-1]["DimensionsSummer"]["Width"]}\n'
#           f'{res[-1]["Address"]}')


# Результаты экзамена 🌶️

# import csv
# import json
# from datetime import datetime
#
#
# with open('exam_results.csv', 'r', encoding='UTF-8') as csv_data, \
#         open('best_scores.json', 'w', encoding='UTF-8') as json_data:
#
#     email_dict = {}
#     rows = list(csv.reader(csv_data))
#
#     for row in rows[1:]:
#         name, surname, score, date_and_time, email = row
#         row = [name, surname, int(score), date_and_time, email]
#         email_dict[email] = email_dict.setdefault(email, []) + [row]
#         email_dict[email] = [max(email_dict[email], key=lambda x: (x[2], datetime.strptime(x[3], "%Y-%m-%d %H:%M:%S")))]
#
#     email_dict = dict(sorted(email_dict.items()))
#
#     print(email_dict)
#
#     keys = ['name', 'surname', 'best_score', 'date_and_time', 'email']
#     res = list(dict(zip(keys, *v)) for v in email_dict.values())
#
#     json.dump(res, json_data, indent=3)


# Общественное питание 😥

# import json
# import time
#
# start = time.time_ns()
#
#
# with open('food_services.json', 'r', encoding='UTF-8') as json_data:
#
#     districts = {}
#     biggest_net = {}
#
#     data = json.load(json_data)
#
#     for item in data:
#         district = item['District']
#         districts[district] = districts.setdefault(district, 0) + 1
#
#         name = item["OperatingCompany"]
#         if name != '':
#             biggest_net[name] = biggest_net.setdefault(name, 0) + 1
#
#     maximum = max(districts.items(), key=lambda x: x[1])
#     print(f'{maximum[0]}: {maximum[1]}')
#
#     maximum = max(biggest_net.items(), key=lambda x: x[1])
#     print(f'{maximum[0]}: {maximum[1]}')
#
# stop = time.time_ns()
#
# print(stop - start / 1000000000)



# Общественное питание 😰


with open('food_services.json', 'r', encoding='UTF-8') as json_data:

    districts = {}
    biggest_net = {}

    data = json.load(json_data)

    for item in data:
        district = item['District']
        districts[district] = districts.setdefault(district, 0) + 1

        name = item["OperatingCompany"]
        if name != '':
            biggest_net[name] = biggest_net.setdefault(name, 0) + 1

    maximum = max(districts.items(), key=lambda x: x[1])
    print(f'{maximum[0]}: {maximum[1]}')
#