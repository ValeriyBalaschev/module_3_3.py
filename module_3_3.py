# module_3_3.py Самостоятельная работа по уроку "Распаковка позиционных параметров".


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a = 2)
print_params(b = 25)
c = [1, 2, 3]
print_params(c)
print_params(c)
print_params(*c)
print_params(*c)

values_list = [25, True, 'String']
print_params(b = values_list)
print_params(*values_list)
values_dict = {'a': 5, 'b': True, 'c': 'banan'}
print_params(**values_dict)
print_params(c = values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print_params(values_list_2, 42)


