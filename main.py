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

# import csv
# import json
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

# import json
#
#
# with open('food_services.json', 'r', encoding='UTF-8') as json_data:
#     type_object_dict = {}
#     data = json.load(json_data)
#
#     for item in data:
#         type = item['TypeObject']
#         name = item['Name']
#         seats = int(item['SeatsCount'])
#
#         if type_object_dict.get(type, 0) == 0:
#             type_object_dict.setdefault(type, [name, int(seats)])
#         else:
#             if type_object_dict[type][1] < seats:
#                 type_object_dict[type] = [name, seats]
#
#     type_object_dict = dict(sorted(type_object_dict.items()))
#
#
# for k, v in type_object_dict.items():
#     print(f'{k}: {v[0]}, {v[1]}')


# Тема урока: работа с zip файлами


# Количество файлов


# from zipfile import ZipFile
#
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     count = 0
#     for item in info:
#         if not item.is_dir():
#             count += 1
#
#     print(count)


# Объем файлов

# from zipfile import ZipFile
#
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     size_before_zip = sum(item.file_size for item in info)
#     size_after_zip = sum(item.compress_size for item in info)
#
#     print(f'Объем исходных файлов: {size_before_zip} байт(а)')
#     print(f'Объем сжатых файлов: {size_after_zip} байт(а)')


# Наилучший показатель
# fontlist-v330.json

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#
#     k = 100
#     res = ''
#     for item in info:
#         if item.compress_size and item.file_size and ((item.compress_size / item.file_size) * 100 < k):
#             k = (item.compress_size / item.file_size) * 100
#             res = item.filename
#     print(res[res.find('/') + 1:])


# Избранные


# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     t = datetime(year=2021, month=11, day=30, hour=14, minute=22)
#     files = [file.filename.split('/')[-1] for file in zip_file.infolist() if not file.is_dir() and datetime(*file.date_time) > t]
#
#     print(*sorted(files), sep='\n')


# Форматированный вывод

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     f = lambda item: (item.filename.split('/')[-1], item.file_size, item.compress_size, datetime(*item.date_time))
#     files_info = [f(file) for file in zip_file.infolist() if not file.is_dir()]
#
#     files_info = sorted(files_info)
#
#     for file in files_info:
#         print(file[0])
#         print(f'  Дата модификации файла: {file[-1]}')
#         print(f'  Объем исходного файла: {file[1]} байт(а)')
#         print(f'  Объем сжатого файла: {file[2]} байт(а)\n')


# Функция extract_this()

# from zipfile import ZipFile
#
#
# def extract_this(zip_name, *args):
#
#     with ZipFile(zip_name) as zip_file:
#         if args:
#             list(map(lambda x: zip_file.extract(x), args))
#         else:
#             zip_file.extractall()


# Шахматы были лучше 🌶️

# import json
# from zipfile import ZipFile
#
#
# def open_json(json_name):
#     try:
#         data = json.loads(json_name)
#         return True
#     except json.JSONDecodeError:
#         return False
#
#
# with ZipFile('data.zip') as zip_file:
#     files_info = [file.filename for file in zip_file.infolist() if not file.is_dir() and file.filename[-5:] == '.json']
#
#     res = []
#
#     for file_path in files_info:
#         try:
#             with zip_file.open(file_path) as file:
#                 content = file.read().decode('utf-8')
#         except:
#             continue
#
#         data = open_json(content)
#         if data:
#             data = json.loads(content)
#             if data['team'] == 'Arsenal':
#                 res.append(data['first_name'] + ' ' + data['last_name'])
#
#     res.sort()
#
#     print(*res, sep='\n')



# Структура архива 🌶️🌶️

# from zipfile import ZipFile
#
#
# def convert_bytes(size):
#     """Конвертер байт в большие единицы"""
#     if size < 1000:
#         return f'{size} B'
#     elif 1000 <= size < 1000000:
#         return f'{round(size / 1024)} KB'
#     elif 1000000 <= size < 1000000000:
#         return f'{round(size / 1048576)} MB'
#     else:
#         return f'{round(size / 1073741824)} GB'
#
#
# with ZipFile('desktop.zip') as zip_file:
#     indent = 0
#     print(zip_file.infolist()[0].filename[:-1])
#     for d in zip_file.infolist()[1:]:
#         name = d.filename
#         size = int(d.file_size)
#
#         indent = name.count("/") - 1
#         if not name.endswith('/'):
#             indent += 1
#         if name.endswith('/'):
#             name = name.split('/')[-2]
#         else:
#             name = name.split('/')[-1]
#
#         print(f'{"  " * indent}{name} {convert_bytes(size) if size != 0 else ""}')



# Тема урока: работа с модулем pickle


# import pickle

# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
#
# print(binary_obj)
# print(type(binary_obj))


# Одинокая функция

# import pickle
# import sys
#
# pickle_name, *params = [srr.strip() for srr in sys.stdin]
#
#
# with open(pickle_name, 'rb') as file:
#     func = pickle.load(file)
#     print(func(*params))


# Ты не пройдешь

# import pickle
#
#
# def filter_dump(filename, objects, typename):
#     with open(filename, 'wb') as file:
#         pickle.dump([item for item in objects if type(item) == typename], file)
#
# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)


# Контрольная сумма

# import pickle
#
#
# def check_control_sum(filename, con_sum):
#     with open(filename, 'rb') as file:
#         data = pickle.load(file)
#
#     if isinstance(data, dict):
#         keys = data.keys()
#         keys = list(filter(lambda x: isinstance(x, int), keys))
#         if len(keys) == 0:
#             return 0 == con_sum
#         return sum(keys) == con_sum
#
#     elif isinstance(data, list):
#         data = list(filter(lambda x: isinstance(x, int), data))
#         if len(data) == 0:
#             return 0 == con_sum
#         return max(data) * min(data) == con_sum
#
#
# name = input()
# control_sum = int(input())
#
# if check_control_sum(name, control_sum):
#     print('Контрольные суммы совпадают')
# else:
#     print('Контрольные суммы не совпадают')



# Я и сам своего рода переводчик

# import string
#
# alphabet = list(map(lambda x: x, input()))
# #print(dict(zip(alphabet, [i for i in range(26)])))
# alphabet = dict(zip([i for i in range(26)], alphabet))
#
# tbl = str.maketrans(alphabet)
#
# srr = input().upper()
# letters = string.ascii_uppercase
#
# tbl2 = str.maketrans(dict(zip(letters, [i for i in range(26)])))
# srr = srr.translate(tbl2)
#
# print(srr.translate(tbl))


# from collections import namedtuple
# import pickle
#
# Animal = namedtuple('animal', 'name, family, sex, color')
#
# with open('data.pkl', 'rb') as file:
#     data = pickle.load(file)
#
#     for item in data:
#         r = [f'{d[0]}: {d[1]}\n' for d in list((zip(Animal._fields, item)))]
#         print(*r, sep='')


# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
#
#
# def subscribe(sub):
#     plans = ['Gold', 'Silver', 'Bronze', 'Basic']
#     return plans.index(sub)
#
#
# res = sorted(users, key=lambda item: (subscribe(item.plan), item.email))
#
# for item in res:
#     print(item.name, item.surname)
#     print(f'  Email:{item.email}')
#     print(f'  Plan:{item.plan}\n')


# Вы кто такие? Я вас не звал

# import csv
# from collections import namedtuple
# from datetime import time, date
#
# Friend = namedtuple('Friend', ['surname', 'name', 'meeting_date', 'meeting_time'])
#
# date_pattern, time_pattern = '%d.%m.%Y', '%H:%M'
#
#
# def date_sort(d):
#     return datetime.strptime(d, date_pattern)
#
#
# def time_sort(t):
#     return datetime.strptime(t, time_pattern)
#
#
# with open('meetings.csv', 'r', encoding='utf-8') as csv_data:
#     rows = csv.DictReader(csv_data, delimiter=',')
#     friends = [Friend(*row.values()) for row in rows]
#
#     friends = sorted(friends, key=lambda item: (date_sort(item.meeting_date), time_sort(item.meeting_time)))
#
#
# [print(friend.surname, friend.name) for friend in friends]



# Тема урока: тип данных defaultdict


# from collections import defaultdict
# info = defaultdict(int)  # создаем словарь со значением по умолчанию 0
#
# info['name'] = 'Timur'
# info['age'] = 29
# info['job'] = 'Teacher'
# info['hi'] = 566666
#
# print(info['salary'])
#
# print(info['ebs'])
# print(info)


# from collections import defaultdict
#
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966),
#         ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964),
#         ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
#         ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951),
#         ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
#
#
# data_new = defaultdict(int)
#
# for item, price in data:
#     data_new[item] += price
#
# print(*sorted([f'{k}: ${data_new[k]}' for k in data_new]), sep='\n')



# from collections import defaultdict
#
# data = defaultdict(int)
#
# for item in staff:
#     data[item[0]] += 1
#
# for k, v in sorted(data.items()):
#     print(f'{k}: {v}')


# from collections import defaultdict
#
# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]
#
# data = defaultdict(set)
#
# for item in staff_broken:
#     data[item[0]].add(item[1])
#
# for k, v in sorted(data.items()):
#     print(f'{k}: ', end='')
#     print(*sorted(list(v)), sep=', ')


# Функция wins()

# from collections import defaultdict
#
#
# def wins(pairs):
#     data = defaultdict(set)
#     for pair in pairs:
#         data[pair[0]].add(pair[1])
#     return data
#
# result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))


# Функция flip_dict()

# from collections import defaultdict
#
#
# def flip_dict(dict_of_lists: dict):
#     data = defaultdict(list)
#     for k, v in dict_of_lists.items():
#         [data[key].append(k) for key in v]
#
#     return data


# Функция best_sender()

# from collections import defaultdict
#
#
# def best_sender(messages: list, senders: list):
#     data = defaultdict(int)
#
#     for msg, snd in zip(messages, senders):
#         data[snd] += msg.count(' ')
#
#     print(data['Bob'])
#     return max(data, key=lambda x: (data[x], x))
#
#
# messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
# senders = ['Bob', 'Charlie']
#
# print(best_sender(messages, senders))


# Тема урока: тип данных OrderedDict



# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
#
# for key in list(data):
#     data.move_to_end(key)
#
# print(data)


# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
#
# new_data = OrderedDict()
#
# rule = False
# for _ in range(len(data)):
#     name, grade = data.popitem(last=rule)
#     new_data[name] = grade
#     rule = not rule
#
# print(new_data)


# from collections import OrderedDict
#
# data = OrderedDict({'Law & Order': 1990, 'The Practice': 1997, 'Six Feet Under': 2001, 'Joan of Arcadia': 2003, 'The West Wing': 1999, 'Deadwood': 2004, 'The Sopranos': 1999, 'Boston Legal': 2004, 'ER': 1994, 'Friday Night Lights': 2006, '24': 2001, 'Heroes': 2006, 'Lost': 2004, 'Dexter': 2006, 'Damages': 2007, 'Big Love': 2006, 'House': 2004, 'Downton Abbey': 2010, "Grey's Anatomy": 2005, 'Homeland': 2011, 'Breaking Bad': 2008, 'Game of Thrones': 2011, 'CSI: Crime Scene Investigations': 2000, 'Boardwalk Empire': 2010, 'True Blood': 2008, 'House of Cards': 2013, 'True Detective': 2014})
#
# data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
# data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)
#
# print(data.sorted_values(reverse=True))


# Функция custom_sort() 🌶️

# from collections import OrderedDict
#
#
# def custom_sort(ordered_dict, by_values=False):
#     if by_values:
#         for k, v in sorted(ordered_dict.items(), key=lambda item: item[1]):
#             ordered_dict.move_to_end(k)
#     else:
#         for k in sorted(ordered_dict):
#             ordered_dict.move_to_end(k)
#
# data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
# custom_sort(data, by_values=True)
#
# print(*data.items())



# Тема урока: тип данных Counter

# from collections import Counter
#
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
#
# res = Counter([f[f.rfind('.')+1:] for f in files])
#
# for k, v in sorted(res.items()):
#     print(f'{k}: {v}')


# Функция count_occurences()

# from collections import Counter
#
#
# def count_occurences(word, words):
#     res = Counter(words.lower().split())
#     return res[word.lower()]
#
# word = 'Se'
# words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'
#
# print(count_occurences(word, words))


# Не поленимся и запишем

# from collections import Counter
#
# srr = input().split(',')
# res = Counter(srr)
#
# for k in sorted(res):
#     print(f'{k}: {res[k]}')


# А сколько стоит курс?

# from collections import Counter
#
#
# srr = input().split(',')
# res = Counter(srr)
# max_len = len(max(res, key=len))
#
# for k in sorted(res):
#     price = sum(list(map(lambda x: ord(x) if x != ' ' else 0, k)))
#     print(f'{k}'.ljust(max_len) + f': {price} UC x {res[k]} = {price * res[k]} UC')


# The Zen of Python

# from collections import Counter
#
# with open('pythonzen.txt', 'r', encoding='utf-8') as file:
#     data = file.read().lower()
#     res = Counter(filter(str.isalpha, data))
#
# for k in sorted(res):
#     print(f'{k}: {res[k]}')


# В поисках слов 😇

# from collections import Counter
#
# res = Counter(list(map(str.lower, input().split())))
# print(res.most_common(1)[0][0])


# В поисках слов 😋


# from collections import Counter
#
# res = Counter(list(map(str.lower, input().split())))
# m = res.most_common()[-1][1]
# f = list(filter(lambda item: item[1] <= m, res.most_common()[::-1]))
# f = [r[0] for r in f]
#
# print(', '.join(sorted(f)))


# В поисках слов 🥳

# from collections import Counter
#
# res = Counter(list(map(str.lower, input().split())))
#
# min_common = res.most_common()[0][1]
# res = list(filter(lambda item: item[1] >= min_common, res.most_common()[::-1]))
# f = [item[0] for item in res]
# print(max(f))


# Статистика длин слов

# from collections import Counter, defaultdict
#
# data = Counter([len(word) for word in input().split()])
# print(data)
# res = sorted(data.items(), key=lambda item: item[1])
# [print(f'Слов длины {item[0]}: {item[1]}') for item in res]


# Все еще достоин

# import sys
# from collections import Counter
#
# res = Counter()
#
# for word in sys.stdin:
#     k, v = word.split()
#     res[k] = int(v)
#
# print(res.most_common()[-2][0])


# from collections import Counter
#
# data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
#
# data.max_values = lambda: [item for item in data.most_common() if item[1] == data.most_common()[0][1]]
# data.min_values = lambda: [item for item in data.most_common() if item[1] == data.most_common()[-1][1]]
#
# print(data)
# print(data.min_values())



# Here we go again

# import csv
# from collections import Counter, defaultdict
#
# res = Counter()
#
# with open('name_log.csv', 'r', encoding='utf-8') as csv_data:
#     rows = list(csv.reader(csv_data, delimiter=','))
#
#     for row in rows[1:]:
#         name, email, time = row
#         res.update((email, 0))
#
#     del res[0]
#
#
# res = sorted(res.most_common(), key=lambda item: (item[0], item[1]), reverse=False)
# for k, v in res:
#     print(f'{k}: {v}')


# Функция scrabble()

# from collections import Counter
#
#
# def scrabble(symbols, word):
#     c_symblos = Counter(symbols.lower())
#     c_word = Counter(word.lower())
#     return c_word <= c_symblos
#
#
# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))


# Функция print_bar_chart()

# from collections import Counter
#
#
# def print_bar_chart(data, mark):
#     res = Counter(data)
#     delim = len(max(res, key=len))
#
#     for k, v in res.most_common():
#         print(f'{k}'.ljust(delim) + f' |{mark * v}')
#
#
# print_bar_chart('beegeek', '+')
#
# languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
#
# print_bar_chart(languages, '#')


# Бесплатные курсы берут свое 😢

# import json
# import csv
# from collections import Counter
#
# files = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
#
# with open('prices.json', 'r', encoding='utf-8') as json_data:
#     json = json.load(json_data)
#     res = Counter()
#
#     for file in files:
#         with open(file, 'r', encoding='utf-8') as csv_data:
#             _, *rows = csv.reader(csv_data, delimiter=',')
#
#             res += Counter({item[0]: sum(map(int, item[1:])) for item in rows})
#
# total_sum = sum(json[k] * v for k, v in res.items())
# print(total_sum)
# 924593


# Бесплатные курсы берут свое 😭

# from collections import Counter
#
# available_books = Counter(input().split())
#
# res = 0
#
# for _ in range(int(input())):
#     clas, price = input().split()
#     if clas in available_books:
#         res += int(price)
#         available_books -= Counter((clas, 1))
#
#
# print(res)


#
# import json
#
#
# with open('test.json', 'w', encoding='utf-8') as json_data:
#     #'{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'
#     srr = {"names": {"name": "a", "name": "b"}}
#     json.dump(srr, json_data, indent=2)


# Тема урока: тип данных ChainMap


# Зоопарк

# from collections import ChainMap
# from collections import Counter
# import json
#
#
# with open('zoo.json', 'r', encoding='utf-8') as json_data:
#     data = json.load(json_data)
#     pets = ChainMap(*data)
#     res = Counter(pets)
#     print(res.total())


# Булочный магнат

# from collections import ChainMap
# from collections import Counter
#
# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
#
# ingredients = Counter(input().split(','))
# n = len(str(ingredients.most_common(1)[0][1]))
#
# ingredients = sorted(ingredients.items())
# print(ingredients)
#
# max_len = len(max(ingredients, key=lambda x: len(x[0]))[0]) + 1
# dopings = ChainMap(bread, meat, sauce, vegetables, toppings)
# print(max_len)
#
# total = 0
# for pos, val in ingredients:
#     print(f'{pos:{max_len}}x {val}')
#     total += dopings[pos] * val
#
# max_len += (n + 2)
#
# if len(f'ИТОГ: {total}р') > max_len:
#     print('-' * len(f'ИТОГ: {total}р'))
# else:
#     print('-'*(max_len))
# print(f'ИТОГ: {total}р')


#  Функция get_all_values()

# from collections import ChainMap
#
#
# def get_all_values(chainmap: ChainMap, key):
#     res = set()
#     for item in chainmap.maps:
#         if key in item:
#             res.add(item[key])
#     return res


# Функция deep_update()

# from collections import ChainMap
#
#
# def deep_update(chainmap: ChainMap, key, value):
#     if key not in chainmap:
#         chainmap[key] = value
#     else:
#         for item in chainmap.maps:
#             if key in item:
#                 item[key] = value



# Функция get_value()

# from collections import ChainMap
#
#
# def get_value(chainmap: ChainMap, key, from_left=True):
#     if key not in chainmap:
#         return None
#     if not from_left:
#         chainmap.maps.reverse()
#     for item in chainmap.maps:
#         if key in item:
#             return item[key]


# Тема урока: обработка исключений

# Only numbers

# import sys
#
# res = [srr.strip() for srr in sys.stdin]
# nums = 0
# strings = 0
#
# for item in res:
#     try:
#         if '.' in item:
#             nums += float(item)
#         else:
#             nums += int(item)
#     except ValueError:
#         strings += 1

# print(nums, strings, sep='\n')


# Январь, февраль, ...

# from calendar import month_name
#
# print(list(month_name ))
#
# m = dict(enumerate(month_name[1:], 1))
#
# try:
#     n = int(input())
# except:
#     print('Введено некорректное значение')
# else:
#     try:
#         print(m[n])
#     except KeyError:
#         print('Введено число из недопустимого диапазона')


# Функция add_to_list_in_dict()


# def add_to_list_in_dict(data:dict, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data.setdefault(key, [element])
#
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'c', 7)

#print(data)


# readme.txt

# name = input()
#
# try:
#     with open(name, 'r', encoding='utf-8') as file:
#         data = file.read()
# except FileNotFoundError:
#     print('Файл не найден')
# else:
#     print(data)


# Функция get_weekday()


# def get_weekday(number):
#     week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
#     if type(number) != int:
#         raise TypeError('Аргумент не является целым числом')
#     if not (1 <= number <= 7):
#         raise ValueError('Аргумент не принадлежит требуемому диапазону')
#     return week[number]
#
# try:
#     print(get_weekday('4'))
# except Exception as err:
#     print(err)
#     print(type(err))


# Функция get_id()


# def get_id(names, name):
#     if type(name) != str:
#         raise TypeError('Имя не является строкой')
#     else:
#         if not (name[0].isupper() and all([ (c.islower() and c.isalpha()) for c in name[1:]])):
#             raise ValueError('Имя не является корректным')
#     return len(names) + 1
#
#
# names = ['Timur', 'Anri', 'Dima']
# name = 'Arthur'
#
# print(get_id(names, name))


# Tanya prog

# import csv
# import os
#
#
# path = "C:/Users/Root/PycharmProjects/stepik_pokoleni_for_pro/Deaths_5x1/"
# dir_list = os.listdir(path)
#
# print(dir_list)
# print(f'Value of files: {len(dir_list)}')
#
#
# with open('res.csv', 'w', encoding='utf-8', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     columns = ['Year', 'Age', 'Female', 'Male', 'Total']
#     writer.writerow(columns)
#
#     for i in range(len(dir_list)):
#
#         with open(path + dir_list[i], 'r', encoding='utf-8', newline='') as txt_file:
#             data = txt_file.readlines()
#             #print(*data[0:10])
#             #print(data[1])
#
#         new_data = []
#         for d in data[3:]:
#             #print(d.strip().split())
#             new_data.append(d.strip().split())
#
#         years = [d[0] for d in new_data]
#         years.append('2020')
#         try:
#             min_index = years.index("2000")
#         except ValueError:
#             print(f' no min year in {dir_list[i]}')
#
#         try:
#            # max_index = years[::-1].index("2019")
#             max_index = years.index("2020")
#         except ValueError:
#             print(f' no max year in {dir_list[i]}')
#
#         if dir_list[i] == 'HRV.Deaths_5x1.txt':
#             min_index = 0
#         if dir_list[i] == 'KOR.Deaths_5x1.txt':
#             min_index = 0
#
#         new_data = new_data[min_index:max_index]
#
#         for row in new_data:
#             writer.writerow(row)


    # years = [d[0] for d in new_data]
    # #print(*years, sep='\n')
    # print(f'Value of lines: {len(years)}')
    # print(f'index of first year = {years.index("2019")}')


# Десериализация
#
# import json
#
# json_name = input()
#
# try:
#     with open(json_name, 'r', encoding='utf-8') as json_data:
#         try:
#             data = json.load(json_data)
#             print(data)
#         except:
#             print('Ошибка при десериализации')
# except:
#     print('Файл не найден')


# Функция is_good_password() 👀

# def is_good_password(string: str):
#     if len(string) < 9:
#         return False
#     if string.lower() == string or string.upper() == string:
#         return False
#     if not any(map(str.isdigit, string)):
#         return False
#     return True
#
# print(is_good_password('МойПарольСамыйЛучший111'))


# Функция is_good_password() 🐍

# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
#
# def is_good_password(string: str):
#     if len(string) < 9:
#         raise LengthError
#     if string.lower() == string or string.upper() == string:
#         raise LetterError
#     if not any(map(str.isdigit, string)):
#         raise DigitError
#     return True
#
# try:
#     print(is_good_password('41157081231232'))
# except Exception as err:
#     print(type(err))


# Уж лучше матрицы 😐

# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     #
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
#
# def is_good_password(string: str):
#     if len(string) < 9:
#         raise LengthError('LengthError')
#     if string.lower() == string or string.upper() == string:
#         raise LetterError('LetterError')
#     if not any(map(str.isdigit, string)):
#         raise DigitError('DigitError')
#
#     return True
#
#
# import sys
#
# for password in sys.stdin:
#     try:
#         if is_good_password(password.strip()):
#             print('Success!')
#             break
#     except Exception as err:
#         print(err)



# Функция to_binary()

# def to_binary(number):
#     res = ''
#     if number <= 0:
#         return str(number)
#     else:
#         res += str(number % 2)
#         return res + to_binary(number // 2)

def to_binary(number):
    res = ''
    if number == 0:
        return ''
    else:
        res += str(number % 2)
        return to_binary(number // 2) + res

print(to_binary(0))
print(to_binary(8))
# print(to_binary(1))
# print(to_binary(15))



# num = int(input())
# srr = ''
# while num > 0:
#     srr = str(num % 2) + srr
#     print(num, num // 2, num % 2)
#    # print(num % 2, end='')
#     num = num // 2
# print(srr)
# Рекурсия


# Подозрительно просто 🤫

# def traffic(n):
#     if n > 0:
#         traffic(n - 1)
#         print('Не парковаться')
# traffic(3)


# Подозрительно просто 🤐

# def print_nums(start, end):
#     def rec(num):
#         if num <= end:
#             print(num)
#             rec(num + 1)
#     rec(start)
#
# print_nums(1, 100)


# def print_nums(lst):
#     i = 0
#     def rec(i):
#         if i < len(lst):
#             print(f'Элемент {i}: {lst[i]}')
#             rec(i+1)
#     rec(i)
#
# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
#
# print_nums(numbers)


# Обратный порядок

import sys

#data = [int(line.strip()) for line in sys.stdin]
# data = [1, 2,3,4,0]
# print(data)
#
# def rev(lst):
#     def rec(index=0):
#         if index < len(lst):
#             rec(index + 1)
#             print(lst[index])
#     rec()
#
# rev(data)


# Функция triangle() 😥
#
# def triangle(h):
#     if h > 0:
#         print('*' * h)
#         triangle(h - 1)
#
# triangle(3)


# Функция triangle() 😰

# def triangle(h):
#     def rec(i=1):
#         if i <= h:
#             print('*' * i)
#             rec(i + 1)
#     rec()
#
# triangle(3)


# Песочные часы

# def print_clock(n, num):
#     if n > 4:
#         print((str(num) * n).center(16))
#         print_clock(n - 4, num + 1)
#     print((str(num) * n).center(16))
#
# print_clock(16, 1)


# Функция print_digits() 😉

# def print_digits(number):
#     def rec(index=0):
#         if index < len(str(number)):
#             rec(index + 1)
#             print(str(number)[index])
#     rec()


# Функция print_digits() 😎

# def print_digits(number):
#     if number:
#         print_digits(number // 10)
#         print(number % 10)
#
# print_digits(12345)


# Количество цифр

# def val_nums(num):
#     dct = {'val': 0}
#
#     def rec(n):
#         if n > 9:
#             rec(n // 10)
#         dct['val'] += 1
#         return dct['val']
#
#     return rec(num)
#
# num = 505
# print(num % 10)
# print(val_nums(50))



# Сумма цифр


# def rec(num):
#     if num <= 0:
#         return 0
#     else:
#         return (num % 10) + rec(num // 10)
#
#
# print(rec(int(input())))


# Функция number_of_frogs()

# def number_of_frogs(year):
#
#     def rec(year, frogs=77):
#         if year == 1:
#             return frogs
#         else:
#             frogs = 3 * (frogs - 30)
#             return rec(year - 1, frogs)
#     r = rec(year)
#     return r
#
# print(number_of_frogs(10))


# Функция range_sum()

# def range_sum(numbers, start, end):
#     if start > end:
#         return 0
#     else:
#         return numbers[start] + range_sum(numbers, start + 1, end)
#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))


# Обычное возведение в степень

# def get_pow(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * get_pow(a, n - 1)
#
# print(get_pow(5, 2))


# Быстрое возведение в степень

# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         return get_fast_pow(a * a, n/2)
#     else:
#         return a * get_fast_pow(a, n - 1)
#
# print(get_fast_pow(2, 10))


# Функция recursive_sum()

# def recursive_sum(a, b):
#     # if abs(a) > abs(b):
#     #     a, b = b, a
#
#     if a == 0:
#         return b
#     else:
#         #print(a)
#         return recursive_sum(a - 1, b + 1)
#
# print(recursive_sum(10, 22))
#
# print(recursive_sum(99, 0))


# Функция is_power()

# def is_power(num):
#     if num < 2:
#         if num == 1:
#             return True
#         else:
#             return False
#     else:
#         return is_power(num / 2)
#
#print(is_power(512))


# Функция tribonacci()

# def tribonacci(n):
#     cache = {1: 1, 2: 1, 3: 1}
#
#     def rec(n):
#         res = cache.get(n)
#         if res is None:
#             res = rec(n - 3) + rec(n - 2) + rec(n - 1)
#             cache[n] = res
#         return res
#     return rec(n)
#
#
# print(tribonacci(7))


# Функция is_palindrome()

# def is_palindrome(string):
#     if len(string) in [0, 1] or (string is None):
#         return True
#     elif string[0] == string[-1]:
#         return is_palindrome(string[1:-1])
#     else:
#         return False
#
# print(is_palindrome(''))
# print(is_palindrome('stepik'))
# print(is_palindrome('level'))
# print('level'[1:-1])


# Функция to_binary()

# def to_binary(num):
#     #res = {'v': ''}
#     res = []
#     def rec(num):
#         if num == 0:
#             #return res['v']
#             return res
#         else:
#             #res['v'] += str(num % 2)
#             res.append(num % 2)
#             return rec(num // 2)
#
#     rec(num)
#     if len(res) == 0:
#         return 0
#     res.reverse()
#     return ''.join(map(str, res))
#
# print(to_binary(15))


# Без циклов

# def rev(n):
#     if n > 0:
#         print(n)
#         rev(n - 5)
#     print(n)
#
# rev(16)


# Функция recursive_sum()

# def recursive_sum(nested_lists):
#     res = 0
#
#     for n in nested_lists:
#         if type(n) == list:
#             #for i in nested_lists:
#             res += recursive_sum(n)
#         if type(n) == int:
#             #return nested_lists
#             res += n
#
#     return res
#
#
# my_list = [1, [4, 4], 2, [1, [2, 10]]]
#
# print(recursive_sum(my_list))


# Функция linear()

# def linear(lst):
#     res = []
#     for n in lst:
#         if isinstance(n, list):
#             res.extend(linear(n))
#         else:
#             res.append(n)
#     return res
#
#
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
#
# print(linear(my_list))


# Функция get_value()

# def get_value(dicts, key):
#     if key in dicts:
#         return dicts[key]
#
#     for k, v in dicts.items():
#         if isinstance(v, dict):
#             value = get_value(v, key)
#             if value is not None:
#                 return value
#
#
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
#         'address': {'streetAddress': 'Часовая 25, кв. 127',
#                     'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'},
#                     'postalCode': '125315'}}
#
# print(get_value(data, 'cityName'))


# Функция get_all_values() 🌶️

# def get_all_values(dicts, key):
#     res = []
#
#     for k, v in dicts.items():
#         if key in dicts:
#             res.append(dicts[key])
#         if isinstance(v, dict):
#             value = get_all_values(v, key)
#             res.extend(value)
#
#     return set(res)
#
# my_dict = {
#            'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
#            'Timur': {'hobby': 'math'},
#            'Dima': {
#                    'hobby': 'CS',
#                    'sister':
#                        {
#                          'name': 'Anna',
#                          'hobby': 'TV',
#                          'age': 14
#                        }
#                    }
#            }
#
# result = get_all_values(my_dict, 'hobby')
# print(*sorted(result))


# Функция dict_travel() 🌶️🌶️


# def dict_travel(dicts, path=''):
#
#     for k, v in sorted(dicts.items()):
#         if isinstance(v, dict):
#             dict_travel(v, path + f'{k}.')
#         else:
#             print(f'{path}{k}: {v}')
#
#
# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
#
# dict_travel(data)




# Встроенные функции

# Строчный алфавит

# [print(chr(i), end='\n') for i in range(97, 122)]


# Функция convert()

# def convert(num):
#     return (bin(num).replace('0b', ''), oct(num).replace('0o', ''), hex(num).replace('0x', '').upper())
#
# print(convert(15))



# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
#
# print(max(films))
# films_new = {}
# for k, v in films.items():
#     films_new[k] = sum(v.values())
#
# min_sum = min(films_new.values())
# for k, v in films_new.items():
#     if v == min_sum:
#         print(k)
#         break


# Функция non_negative_even()

# def non_negative_even(numbers):
#     return all([True if ((num % 2 ==0) and (num >= 0)) else False for num in numbers])
#
# print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))


# Функция is_greater()

# def is_greater(lists, number):
#     return any([sum(d) > number for d in lists])
#
# data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
#
# print(is_greater(data, 2))


# Функция custom_isinstance()

# def custom_isinstance(objects, typeinfo):
#     return sum([any([isinstance(d, typeinfo)]) for d in objects])
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))



# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
#
# print(max(enumerate(numbers, 0), key=lambda x: x[1])[0])
# print(max(numbers))


# Функция my_pow()

# def my_pow(number):
#     return sum([pow(int(n[1]), n[0]) for n in enumerate(str(number), 1)])
#
# print(my_pow(139))


# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
# for n, b, d in sorted(zip(names, budgets, box_offices)):
#     print(f'{n}: {d-b}$')


# Функция zip_longest()

# def zip_longest(*args: list, fill=None):
#     maxest_len = len(max(args, key=len))
#     for lst in args:
#         lst.extend([fill for i in range(maxest_len - len(lst))])
#     return list(zip(*args))
#
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))


# Необычная сортировка 🌶️


# def sotr(str):
#     str = sorted(str)
#     lower = [c for c in str if c.islower()]
#     upper = [c for c in str if c.isupper()]
#     nums = [c for c in str if c.isdigit()]
#
#     lower.sort()
#     upper.sort()
#     nums.sort(key=lambda x: int(x) % 2 == 0)
#     return ''.join(lower + upper + nums)
#
# print(sotr('AnHTqir9brdQrgu5g71uhm1FaJ4fAZjbisIDnJVYekRPdGDc29'))


# Функция hash_as_key()

# def hash_as_key(objects):
#     res = {}
#     for item in objects:
#         k = hash(item)
#         if k in res:
#             if isinstance(res[k], list):
#                 res[k] = res[k] + [item]
#             else:
#                 res[k] = [res[k], item]
#         else:
#             res[k] = item
#     return res
#
# data = [5, 5, 5]
#
# print(hash_as_key(data))


# Коллекции

# def rer(data):
#     data = eval(data)
#     if isinstance(data, list):
#         print(data[-1])
#     elif isinstance(data, tuple):
#         print(data[0])
#     else:
#         print(len(data))
#
# rer('[[1, 2], [3, 4], [5, 6]]')


# Математические выражения

# import sys
# data = [eval(i) for i in sys.stdin]
#
# print(max(data))


# Минимум и максимум

# f = input()
# x1, x2 = list(map(int, input().split()))
# y = [eval(f) for x in range(x1, x2 + 1)]
#
# print(f'Минимальное значение функции {f} на отрезке [{x1}; {x2}] равно {min(y)}')
# print(f'Максимальное значение функции {f} на отрезке [{x1}; {x2}] равно {max(y)}')


# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
#
# print(*map(int, filter(lambda x: isinstance(x, int) or isinstance(x, float), data)), sep='\n')


# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
#
# print(sum(map(lambda x: x * x, filter(lambda x: (abs(x) in range(10, 100)) and (x % 9 == 0), numbers))))


# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
#
# print(*sorted(map(str.capitalize, filter(lambda x: x[0].lower() in 'ам' and len(x) > 4, names))))


# Функция fib()

# fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
#
# print(fib(5))


# Функция print_operation_table()

# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows +1):
#         for j in range(1, cols+1):
#             print(operation(i, j), end=' ')
#         print()
#
#
# print_operation_table(lambda a, b: a * b, 5, 5)
# print_operation_table(pow, 5, 4)


# Функция verification()

# import string
#
# def verification(login, paswword, succcess, failure):
#
#     lower = any(c in string.ascii_lowercase for c in paswword)
#     upper = any(c in string.ascii_uppercase for c in paswword)
#     digit = any(c in string.digits for c in paswword)
#
#     if all([lower, upper, digit]):
#         succcess(login)
#     else:
#         msg = ['в пароле нет ни одной буквы',
#                'в пароле нет ни одной заглавной буквы',
#                'в пароле нет ни одной строчной буквы',
#                'в пароле нет ни одной цифры']
#         err = [lower or upper, upper, lower, digit]
#
#         for i in range(4):
#             if not err[i]:
#                 failure(login, msg[i])
#
#
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
# verification('Arthur_Davletov', 'HELLO_WORLD', success, failure)


# Функция numbers_sum()

# def numbers_sum(elems):
#     """Принимает список и возвращает сумму его чисел (int, float),
# игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
#     return sum(filter(lambda x: isinstance(x, int) or isinstance(x, float), elems))
#
# print(numbers_sum([1, '2', 3, 4, 'five']))
# print(numbers_sum.__doc__)


# Новый print()

# old_print = print
# def print(*args, **kwargs):
#     sep, end = ' ', '\n'
#     if 'sep' in kwargs:
#         sep = kwargs['sep'].upper()
#     if 'end' in kwargs:
#         end = kwargs['end'].upper()
#
#     res = [s.upper() if isinstance(s, str) else s for s in args]
#     res = [s if isinstance(s, str) else repr(s) for s in res]
#
#     res = f'{sep}'.join(res) + end
#     old_print(res)



# Функция power()

# def power(degree):
#     def maker(num):
#         return num ** degree
#     return maker
#
# square = power(2)
# print(square(5))


# Функция generator_square_polynom()

# def generator_square_polynom(a, b, c):
#     return lambda x: a * (x ** 2) + b * x + c
#
# f = generator_square_polynom(1, 2, 1)
# print(f(5))


# Функция sourcetemplate()

# def sourcetemplate(url):
#     def maker_query(**kwargs):
#         if kwargs:
#             return f'{url}?' + '&'.join(f'{k}={v}' for k, v in sorted(kwargs.items()))
#         return url
#     return maker_query
#
# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load())


# Функция date_formatter()

from datetime import date
# def date_formatter(country_code):
#     def format(d):
#         d_dict = {'ru': '%d.%m.%Y',
#              'us': '%m-%d-%Y',
#              'ca': '%Y-%m-%d',
#              'br': '%d/%m/%Y',
#              'fr': '%d.%m.%Y',
#              'pt': '%d-%m-%Y', }
#         return d.strftime(d_dict[country_code])
#
#     return format
#
# date_ru = date_formatter('us')
# today = date(2025, 1, 5)
# print(date_ru(today))


# Функция sort_priority() 🌶️

# def sort_priority(values, group):
#     tmp = values.copy()
#     a = set(values)
#     b = set(group)
#     a = a - b
#     values.clear()
#     for n in sorted(list(b)):
#         if n in tmp:
#             values.append(n)
#     for n in sorted(list(a)):
#         values.append(n)
#
# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {5, 7, 2, 3}
# sort_priority(numbers, group)
#
# print(numbers)


# Тема урока: аннотации типов

# Функция get_digits()

# def get_digits(number: int | float) -> list[int]:
#     return [int(i) for i in str(number) if i.isdigit()]


# Функция top_grade()

# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     return dict(name=grades['name'], top_grade=max(grades['grades']))
#
# info = {'name': 'Timur', 'grades': [30, 57, 99]}
#
# print(top_grade(info))
#
# print(*top_grade.__annotations__.values())


# Функция cyclic_shift()

# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     for i in range(len(numbers) + step):
#         a = numbers.pop()
#         numbers.insert(0, a)
#
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, 1)
#
# print(numbers)


# Функция matrix_to_dict()

# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
#     #return dict([i+1=matrix[i] for i in range(len(matrix))])
#     return {key: val for (key, val) in enumerate(matrix, 1)}
#
# matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
#
# print(matrix_to_dict(matrix))
#
# print(*matrix_to_dict.__annotations__.values())




# Декораторы

#
# def uppercase_decorator(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
#
# def greet():
#     return 'Hello world!'
#
# greet2 = uppercase_decorator(greet)
#
# print(greet())
# print(greet2())



# Декоратор sandwich

# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         r = func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#         return r
#     return wrapper
#
# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
#
# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

# @sandwich
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())


# Новый print

# def new_print(func):
#     def wrapper(*args, **kwargs):
#         sep = kwargs.get('sep', ' ')
#         end = kwargs.get('end', '\n')
#         return func(f'{sep}'.join(map(str, args)).upper(), end=end.upper())
#     return wrapper
#
# print = new_print(print)
#
# # print('hi', 'there', end='!')
# print(111, 222, 333, sep='xxx', end='python')
# print(111, 222, 333, sep='--', end='\n')
# print(111, 222, 333, sep='qqq', end='!')


# Декоратор do_twice

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         m = func(*args, **kwargs)
#         m = func(*args, **kwargs)
#         return m
#     return wrapper
#
# @do_twice
# def beegeek():
#     print('beegeek')

# print(beegeek())


# Декоратор reverse_args

# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         args = args[::-1]
#         r = func(*args, **kwargs)
#         return r
#     return wrapper
#
# @reverse_args
# def power(a, n):
#     return a ** n

# @reverse_args
# def concat(a, b, c):
#     return a + b + c

# print(concat('apple', 'cherry', 'melon'))
# print(power(2, 3))


# Декоратор exception_decorator

# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return (func(*args, **kwargs), 'Функция выполнилась без ошибок')
#         except:
#             return (None, 'При вызове функции произошла ошибка')
#     return wrapper
#
# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))


# Декоратор takes_positive

# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         lst = list(args)
#         lst.extend(kwargs.values())
#         if not all([isinstance(n, int) for n in lst]):
#             raise TypeError
#         else:
#             if any([n <= 0 for n in lst]):
#                 raise ValueError
#             else:
#                 return func(*args, **kwargs)
#     return wrapper
#
#
# @takes_positive
# def positive_sum(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# try:
#     print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
# except Exception as err:
#     print(type(err))




# Декоратор square

# import functools
#
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) ** 2
#     return wrapper
#
# @square
# def add(*args, **kwargs):
#     return sum([*args, *kwargs.values()])

# print(add(3, 7, x=10, y=30))


# Декоратор returns_string

# import functools
#
# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if isinstance(func(*args, **kwargs), str):
#             return func(*args, **kwargs)
#         else:
#             raise TypeError
#     return wrapper
#
#
# @returns_string
# def add(a, b):
#     return a + b
#
# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))


# Декоратор trace

# import functools
#
# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
#         res = func(*args, **kwargs)
#         print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(res)}')
#         return res
#     return wrapper
#
# # TEST_3:
# @trace
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
# print(beegeek())
# print(beegeek.__name__)
# print(beegeek.__doc__)


# Декоратор prefix

# import functools
#
# def prefix(string, to_the_end=False):
#
#     def dectorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if to_the_end:
#                 return func(*args, **kwargs) + string
#             else:
#                 return string + func(*args, **kwargs)
#         return wrapper
#     return dectorator
#
#
# @prefix(' online-school', to_the_end=True)
# def beegeek():
#     '''beegeek docs'''
#     return 'beegeek'
#
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# print(beegeek())


# Декоратор make_html

# import functools
# def make_html(tag):
#
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>' + func(*args, **kwargs) + f'</{tag}>'
#         return wrapper
#     return decorator
#
#
# @make_html('i')
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text(text='decorators are so cool!'))


# Декоратор repeat

# import functools
#
# def repeat(times):
#
#     def dectorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 val = func(*args, **kwargs)
#             return val
#         return wrapper
#     return dectorator
#
#
# @repeat(4)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
#
# print(say_beegeek.__name__)
# print(say_beegeek.__doc__)


# Декоратор strip_range

# import functools
#
# def strip_range(start, end, char='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             str = func(*args, **kwargs)
#             nonlocal end
#             if end > len(str):
#                 end = len(str)
#             return str[:start] + f'{char}' * (end-start) + str[end:]
#         return wrapper
#     return decorator
#
#
# @strip_range(20, 30)
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())


# Декоратор returns

# import functools
#
#
# def returns(datatype):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             if datatype != type(res):
#                 raise TypeError
#             return res
#         return wrapper
#     return decorator
#
#
# @returns(list)
# def append_this(li, elem):
#     '''append_this docs'''
#     return li + [elem]
#
# print(append_this.__name__)
# print(append_this.__doc__)
# print(append_this([1, 2, 3], elem=4))


# Декоратор takes

# import functools
#
# def takes(*args_outer):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             if not all(type(a) in args_outer for a in args):
#                 raise TypeError
#             if not all(type(a) in args_outer for a in kwargs.values()):
#                 raise TypeError
#             return res
#
#         return wrapper
#     return decorator
#
#
# @takes(str)
# def beegeek(word, repeat):
#     return word * repeat
#
#
# try:
#     print(beegeek('beegeek', repeat=2))
# except TypeError as e:
#     print(type(e))


# Декоратор add_attrs

# import functools
#
# def add_attrs(**kwargs_outer):
#     def decorator(func):
#         for k, v in kwargs_outer.items():
#             func.__dict__[k] = v
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#
#     return decorator
#
#
# @add_attrs(attr2='geek')
# @add_attrs(attr1='bee')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)


# Декоратор ignore_exception

# import functools
#
# def ignore_exception(*args_outer):
#
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 res = func(*args, **kwargs)
#             except Exception as err:
#                 if type(err) in args_outer:
#                     print(f'Исключение {type(err).__name__} обработано')
#                 else:
#                     raise err
#             else:
#                 return res
#         return wrapper
#
#     return decorator
#
#
# @ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())



# Декоратор retry

# import functools
#
# class MaxRetriesException(Exception):
#     pass
#
#
# def retry(times):
#
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 try:
#                     res = func(*args, **kwargs)
#                     return res
#                 except Exception as err:
#                     pass
#
#             raise MaxRetriesException
#
#         return wrapper
#     return decorator
#
#
# @retry(8)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 5:
#         raise ValueError
#     print('beegeek')
#
# beegeek()