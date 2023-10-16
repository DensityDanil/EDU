from multiprocessing import Process
import time

def do_something():
    print("I'm going to sleep")
    time.sleep(1)
    print("I'm awake") 
# Create new child process

process_1 = Process(target=do_something)
process_2 = Process(target=do_something)

# Starts both processes
process_1.start()
process_2.start()
