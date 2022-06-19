import os
from datetime import datetime

# Глобальные переменные программы

LOG_FILE = 'fclogger.log'
LOG_PATH = 'log'

# Функции и классы используемые в программе

# функция-декоратор для логгирования работы функций
def func_log(func):

    # проверяем, существует ли каталог для лога
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)
    
    filename = os.path.join(LOG_PATH, LOG_FILE)
    
    # функция декоратора
    def logger(*args, **kwargs):
        # фиксируем время начала работы функции
        start = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        res = func(*args, **kwargs)
        # фиксируем время завершения работы функции
        end = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        # записываем данные в файл
        with open(filename, 'a', encoding='utf-8') as f:
            f.write('[' + func.__name__ + ']' + '\n')
            f.write('Started at: ' + start + '\n')
            f.write('Funtions arguments:' + '\n')
            f.write(str(args) + '\n')
            f.write(str(kwargs) + '\n')
            f.write('Results:' + '\n')
            f.write(str(res) + '\n')
            f.write('Stopped at: ' + end + '\n')
        return res

    return logger
# end func_log()

# функция-декоратор параметрами пути для логгирования работы функций
def func_log_path(path = LOG_PATH):

    # проверяем, существует ли каталог для лога
    if not os.path.isdir(path):
        os.mkdir(path)
    
    filename = os.path.join(path, LOG_FILE)
    
    def fc_log(func):
        # функция декоратора
        def logger(*args, **kwargs):
            # фиксируем время начала работы функции
            start = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            res = func(*args, **kwargs)
            # фиксируем время завершения работы функции
            end = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            # записываем данные в файл
            with open(filename, 'a', encoding='utf-8') as f:
                f.write('[' + func.__name__ + ']' + '\n')
                f.write('Started at: ' + start + '\n')
                f.write('Funtions arguments:' + '\n')
                f.write(str(args) + '\n')
                f.write(str(kwargs) + '\n')
                f.write('Results:' + '\n')
                f.write(str(res) + '\n')
                f.write('Stopped at: ' + end + '\n')
            return res
        return logger
    return fc_log
# end func_log_path()

# Главная функция программы

# Основная программа

if __name__ == '__main__':

    @func_log
    def get_time(*args, **kwargs):
        return 'Now time is: ', datetime.now()

    @func_log_path(LOG_PATH)
    def get_path(*args, **kwargs):
        return os.getcwd()

    print(get_time('day', 1, [123, 124, None], False, {'a' : 1}, x = 123, y = [1, 2, 'Yes']))
    print(get_time())
    print(get_path('Give me a path'))
