"""
ThreadPool Executor
Threads provide a way to execute something on the side, without blocking the loop
"""
import time,datetime
from concurrent.futures import ThreadPoolExecutor


#def fn_take_time(n):
#    print("Wake",n)
#    time.sleep(n)
#    print("Sleep",n)
#
#startTime = datetime.datetime.now()
#with ThreadPoolExecutor(max_workers=1) as Executor:
#    timer = [2,3,4]
#    result = Executor.map(fn_take_time, [ time for time in timer])
#    print("For Loop")
#endTime  = datetime.datetime.now()
#print(endTime - startTime)


def fn_take_time(n):
    print("wake",n)
    time.sleep(n)
    print("sleep",n)
    return "DONE @" + str(n)

with ThreadPoolExecutor(max_workers = 3) as ex:
    timer = [2,3,4]
    results = ex.map(fn_take_time, [time for time in timer ])
    for result in results:
        print(result)




