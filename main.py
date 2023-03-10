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



