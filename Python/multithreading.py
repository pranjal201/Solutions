import threading
from threading import Thread
import time

def printAfterSec(n):
    while True:
        pass
        #print(f"Thread with {n} start")
        #time.sleep(n)
        #print(f"Thread with {n} finish")

def ExecuteThread():
    thrd1 = Thread(target=printAfterSec, args=(4,))  # Correct: pass function reference and argument as a tuple
    thrd2 = Thread(target=printAfterSec, args=(8,))  # Correct: pass function reference and argument as a tuple
    thrd1.start()
    thrd2.start()

# if you don't join the thread, the main thread will not wait for the child thread to finish
    thrd1.join()
    thrd2.join()

if __name__ == "__main__":
    print("Main Flow Start")
    ExecuteThread()
    print("Main Flow Ends")
