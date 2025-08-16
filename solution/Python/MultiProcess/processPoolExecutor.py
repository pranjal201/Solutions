import datetime
from concurrent.futures import ProcessPoolExecutor
def cpu_intensiveTask():
    print("Before while Loop")
    counter = 0
    while counter < 900000000:
        counter += 1
    print("After while loop")


def mains():
    starttime = datetime.datetime.now()
    #cpu_intensiveTask()  #time take = 12 sec
    with ProcessPoolExecutor(max_workers = 3) as px:
        f1 = px.submit(cpu_intensiveTask)
        f2 = px.submit(cpu_intensiveTask)
        f1.result()
        f2.result()
    endtime = datetime.datetime.now()
    print("TotalTime=",endtime-starttime)

if __name__ == "__main__":
    mains()
