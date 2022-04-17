def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()


sina = 10

def name_function(num):
    global sina
    sina = sina + num
    print(sina)


print(sina)
name_function(10)
print(sina)



