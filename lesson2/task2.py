# Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

# Решение сделано через функцию чтобы компактнее показать несколько примеров вывода с разными значениями
# Раньше питон не изучал, как делать функции нагуглил

def getNamedDate(date):
  parsedDate = date.split('.')

  months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
  }

  days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одинадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадатое',
    '2*': 'двадцать ',
    '30': 'тридцатое',
    '3*': 'тридцать',
  }

  # Получаем день
  day = parsedDate[0]
  if (int(day) > 31 or len(day) < 2):
    return 'Некорректный формат даты'

  if(day in days):
    day = days[day]
  elif(day[0] == '2'):
    day = days['2*'] + days['0' + day[1]]
  elif(day[0] == '3'):
    day = days['3*'] + days['0' + day[1]]
  else:
    return 'Некорректный формат даты'

  # Получаем месяц
  month = parsedDate[1]
  if (int(month) > 12 or len(month) < 2):
    return 'Некорректный формат даты'

  if (month in months):
    month = months[month]
  else:
    return 'Некорректный формат даты'

  return "{} {} {} года".format(day, month, parsedDate[2])


# Проверяем работу

print(getNamedDate('02.11.2013'))
print(getNamedDate('21.01.2018'))
print(getNamedDate('32.11.2013'))
print(getNamedDate('32.1.2013'))
print(getNamedDate('3.10.2013'))
print(getNamedDate('30.08.2000'))