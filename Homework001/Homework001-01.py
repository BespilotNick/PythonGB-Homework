
def IsAWeekend(N):

    ''' программа принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. '''

    if N == 6 or N == 7:
        print ('Да, это выходной день')
    else:
        print ('Нет, это не выходной день')

N = int(input('Введите номер дня недели: '))

if N in range (1, 8):
    IsAWeekend(N)
else:
    print ('Введено некорректное значение! Пожалуйста, введите номер дня недели от 1 до 7, начиная с понедельника')