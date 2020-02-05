# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
# # 2. Сравнить время создания генератора и списка с элементами:
# # натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).

import time

def estimatedtime (f):
    def wrapper(*args, **kwargs):
        startime=time.time()
        f(*args, **kwargs)
        print(type(f))
        deltatime=(time.time() - startime)
        return print ('Время выполнения создания списка', format(deltatime, '11') )
    return wrapper

@estimatedtime
def makelist(n):
    list=[]
    for i in range(1, n+1):
        list.append(i)
    print(type(list))
makelist(1000000)

@estimatedtime
def makelistgen(n):
    list=(i for i in range(1,n+1))
    print(type(list))
makelistgen(1000000000000000000000000000000000000)
# print(deltatime)