def test_function():
    def inner_function():
        print(" Я области видимости функции test_function")

#        inner_function()#Приводит к ошибке   [Previous line repeated 995 more times]
    # RecursionError: maximum recursion depth exceeded
#inner_function()# Ошибка вызова вложенной функции
    inner_function()# Вызывает вложенную функцию"Я в области видимости функции test_function"
test_function()# Выводит результат вызова на экран


def outer_function():
    def inner_function():
        print("Это вложенная функция")

    inner_function()  # Вызов вложенной функции


outer_function()

def my_function():
    def little_function():
        print("Hello, World!")
    little_function()
my_function()

