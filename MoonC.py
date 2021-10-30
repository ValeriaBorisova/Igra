
class MyError(Exception):
    def __init__(self, text):
        self.txt = text

a = input("Присланный объект список списков: ")

try:
    a = int(a)
    if a < 0:
        raise MyError("Присланный объект не список списков")
except ValueError:
    print("Error type of value!")
except MyError as mr:
    print(mr)
else:
    print(a)



class RectangleError(Exception):
    def __init__(self, text):
        self.txt = text
b = input("Двумерный список прямоугольный: ")

try:
    b = int(b)
    if b > 0:
        raise RectangleError("Присланный двумерный список - не прямоугольный")
except ValueError:
    print("Error type of value!")
except RectangleError as rr:
    print(rr)
else:
    print(b)


class NumberError(Exception):
    def __init__(self, text):
        self.txt = text

c = input("В присланном списке присутствуют элементы который являются только нулем либо единицей : ")

try:
    c = int(c)
    if c == 0 or 1:
        raise NumberError("В присланном двумерном списке присутствуют элементы которые НЕ являются нулем либо единицей")
except ValueError:
    print("Error type of value!")
except NumberError as nr:
    print(nr)

else:
    print(c)


class ListValidationError(Exception):
    def __init__(self, text):
        self.txt = text

d = input("Присланный список пуст: ")

try:
    d = int(d)
    if d <= -1:
        raise ListValidationError("Присланный список пуст")
except ValueError:
    print("Error type of value!")
except ListValidationError as lr:
    print(lr)
else:
    print(d)


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Какие данные поступили по присланным объектам:")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
        return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
class ListValidationError:
    def function_with_no_argument () -> None:
        print('Присланный список пуст')


@a_decorator_passing_arbitrary_arguments
class NumberError:
    def function_with_correct_argument ()-> None:
        print('В присланном двумерном списке присутствуют элементы которые НЕ являются нулем либо единицей')

@a_decorator_passing_arbitrary_arguments
class RectangleError:
    def function_with_geometry_argument ()-> None:

        print('Присланный двумерный список - не прямоугольный')

@a_decorator_passing_arbitrary_arguments
class MyError:
    def function_with_list_argument () -> None:
        print('Присланный объект не список списков')





