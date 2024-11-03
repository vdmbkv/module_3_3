# Распаковка

def print_params(a = 89, b = 'CocaCola', c = True):
    print(a, b, c)

print_params()
print_params(b = 'Pepsi', c = False)
print_params(a = 15.15, b = False)
print_params(c = 'True')

print_params(b = 25)
print_params(c = [1,2,3])
# эти вызовы функций будут работать, но отмечены желтым, тк Пайтон ожидает на их месте оригинальные типы данных.

values_list = [18, '18', True]
values_dict = {'a': 98, 'b': 'Pepsi', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [18.18, '18']
print_params(*values_list_2, 42)
