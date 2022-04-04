import time


def myname():
    a = input('Podaj imie: ')
    print('Mam na imie ', a)

def mytime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('Obecnie jest godzina: ', current_time)


myname()
mytime()