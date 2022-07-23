import datetime
import time
import sys
import os

# >>> Стандартная библиотека под лупой

print(sys.platform) # Определяем операционную систему
print(sys.version) # Определяем версию python

print(os.getcwd()) # Каталог, в котором выполняется код
print(os.environ) # Системные переменные окружения
print(os.getenv('HOME')) # Конкретная системная переменная окружения

print(datetime.date.today()) # Получает дату
print(datetime.date.today().day) # День
print(datetime.date.today().month) # Месяц
print(datetime.date.today().year) # Год

print(time.strftime('%I:%M')) #Время. %I - Часы %M - Минуты
print(time.strftime('%A %p')) #Время. %A - День недели %p - Текущая половина суток
