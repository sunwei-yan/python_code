# import time
# import multiprocessing
 
 
# def eat(num,name):
#     for i in range(num):
#         print(name+"吃一口……")
#         time.sleep(1)
 
 
# def drink(num,name):
#     for i in range(num):
#         print(name+"喝一口……")
#         time.sleep(1)
 
 
# if __name__ == '__main__':
#     # target：指定执行的函数名
#     # args:使用元组方式给指定任务传参
#     # kwargs:使用字典方式给指定任务传参
#     eat_process = multiprocessing.Process(target=eat,args=(3,"giao"))
#     drink_process = multiprocessing.Process(target=drink,kwargs={"num": 4,"name":"giao"})
 
#     eat_process.start()
#     drink_process.start()
import multiprocessing
from unicodedata import name
def fun1():
    for i in range(5):
        print("1")
def fun2():
    for i in range(5):
        print("2")
if __name__ == '__main__':
    fun1por=multiprocessing.Process(target=fun1)
    fun2pro=multiprocessing.Process(target=fun2)
    fun1por.start()
    fun2pro.start()
        
    
    
    
    