"""
Thread Synchronization or Mutual Exclusion and Locks

Why we need thread synchronication or Mutual Exclusion ( if one person has it, another can't)?
>> When multiple threads are running in a program, they may access the same resource at the same time. This may lead to data inconsistency.
>> To avoid this, we need to synchronize the threads. This is called thread synchronization.
this can be understood via below code in this folder
given a meeting room , where only one person can sit at a time. if Mutual Exlucsion is not applied, then in the first snippet we can see what issue arise.
"""
from threading import Thread,Lock
import time


#First Snippet
def first_person():
    print("First Person Enters Meeting Room")
    time.sleep(0.5)
    print("First Person Exits  Meeting Room")

def Second_person():
    print("Second Person Enters Meeting Room")
    time.sleep(0.5)
    print("Second Person Exits  Meeting Room")

t1 = Thread(target=first_person)
t2 = Thread(target=Second_person)
t1.start()
t2.start()
t1.join()
t2.join()
""" The out of the above snippet is incorrect as both the person occupy the meeting room one after another , which violates the condition. To solve this issue we use Lock(), which inturn work as mutex or semaphore?(this I don't remember)"""

#Second Snippet
lock = Lock()
def third_person(lock):
    lock.acquire()
    print("Third Person Enters Meeting Room")
    time.sleep(5)
    print("Third Person Exits  Meeting Room")
    lock.release()

def fourth_word(lock):
    while True:
        if lock.acquire(timeout=0.1) is True:
            break
        else:
            print("Lock Not Free")
    print("fourth_word Person Enters Meeting Room")
    time.sleep(0.5)
    print("fourth_word Person Exits  Meeting Room")
    lock.release()

t3 = Thread(target=third_person,args=(lock,))
t4 = Thread(target=fourth_word,args=(lock,))
t3.start()
t4.start()
t3.join()
t4.join()


