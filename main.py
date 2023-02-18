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

#calendar.setfirstweekday(calendar.TUESDAY)


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
