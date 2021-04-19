import time


def what_time_is_it_now():
    print(time.strftime('%H:%M'))


def simple_decore():
    def wrapper():
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        return wrapper


simple_decore()
what_time_is_it_now()
