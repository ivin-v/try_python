# выводит время суток
# код взят здесь https://geekbrains.ru/topics/3016
# Доработан Ivin

import time

#print(time.ctime())           # выводим текущую дату и время

time_list = time.localtime()   # назначаем переменой time_list содержание строки с датой\временем
hours = time_list[3]           # назначаем переменной hours значение 3-го слова (часы) из строки с датой\временем
minuts = time_list[4]
day = time_list[0]

#morning = "утро"               # назначаем переменные по времени суток
#day = "день"
#evening = "вечер"
#night = "ночь"

                               # назначаем переменные по часам
                               



if 5 < int(hours) <= 11:       # задаем начало и окончание утра
  time_sutok = "утро"         

elif 11 < int(hours) <= 16:    # задаем начало и окончание дня 
  time_sutok = "день"

elif 16 < int(hours) <= 23:    # задаем начало и окончание вечера
  time_sutok = "вечер"

else:                          # все остальное время-ночь 
  time_sutok = "ночь"

#print(time_sutok)             # выводим текущее время суток,
                               # ремарка для использования в других модулях
print (hours)
#print (minuts)
#print (hours,":",minuts,time_sutok)
