'''Вопрос №1

На языке Python написать алгоритм (функцию) определения четности целого числа,
который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
Объяснить плюсы и минусы обеих реализаций.

Пример:

def isEven(value):

      return value % 2 == 0'''

#Вариант 1: Использование оператора % (остаток от деления)
def isEven(value):
    return value % 2 == 0
'''Оператор % возвращает остаток от деления числа на 2.
Если остаток равен 0, число четное, иначе — нечетное.'''

#Вариант 2: Использование побитовой операции &
def isEven(value):
    return (value & 1) == 0



