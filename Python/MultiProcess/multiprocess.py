from multiprocessing import Process

def working_process():
    while True:
        pass

if __name__ == "__main__":

    proc = Process(target = working_process)
    proc1 = Process(target = working_process)
    
    proc1.start()
    proc.start()


# For this in you execute the following command:
# ps -eaf | grep multiprocess
# you will see 4 python processes except the grep command itself.
# the reason is that multiprocess spawns up an extra process called as resource tracker. to keep track of the resources used by the child processes.
# This is the reason why we see 4 processes instead of 2.