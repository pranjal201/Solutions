from threading import Thread
import time


def thrFunc():
    print("Thread Start")
    time.sleep(14)
    print("Thread End") 


time.sleep(15)
thread1 = Thread(target=thrFunc)
# print("Thread is ALive", thread1.is_alive()) # is_alive gives where thread is running or not
print(thread1.ident)
thread1.start()
print(thread1.ident)
# print(thread1.name)
# thread1.join()
print("Thread is ALive", thread1.is_alive())
print("MainTread End")

# threadU = Thread(target=thrFunc,name="UserThread")
# threadU.start()
# print(threadU.name)

# how to check if a thread is alive or not
# thread.ident != None and thread.is_alive() == True then the thread is alive else not


class MyThread(Thread):
    def __init__(self,param):
        super().__init__()
        self.param = param

    def run(self):
        print("Thread Start ---<",self.param)
        time.sleep(4)
        print("Thread End")
# thread2 = MyThread("Thread2")
# thread2.start()
