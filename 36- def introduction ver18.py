def import_os():
    import os
    os.system('cls')
import_os()

def addition_of_numbers(*args, **kwargs):
    dict_args = []
    for s in args:
        dict_args.append(s)
    print(dict_args) #return list
    print(args) #return tuple
    print(kwargs) #return dictionary 
    print(kwargs.items()) #return list in tuple
    list_kwargs = []
    for s in kwargs.items():
        list_kwargs.append(s)
    print(list_kwargs) #return list of dictiomary ex
    for name_,value_ in list_kwargs:
        print(name_, value_, end='|') #return tuple unpaking
        

addition_of_numbers(1,2,3,4,a='sina',b=10,c='mahsa',d=20)


# # output
# [1, 2, 3, 4]
# (1, 2, 3, 4)
# {'a': 'sina', 'b': 10, 'c': 'mahsa', 'd': 20}
# dict_items([('a', 'sina'), ('b', 10), ('c', 'mahsa'), ('d', 20)])
# [('a', 'sina'), ('b', 10), ('c', 'mahsa'), ('d', 20)]
# a sina|b 10|c mahsa|d 20|
