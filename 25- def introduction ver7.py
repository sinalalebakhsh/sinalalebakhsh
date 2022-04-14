
def import_os():
    import os
    os.system('cls')
import_os()

input_name = input('What\'s your name? ')
input_symbol = input('What\'s your symbol? ')

def side_symbol_center_name(center, side):
    return f'{side} {center} {side}'

print(side_symbol_center_name(input_name, input_symbol))
