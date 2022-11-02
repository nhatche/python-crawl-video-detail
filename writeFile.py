'''

import threading
from time import sleep
from datetime import datetime

global_lock = threading.Lock()

def write_to_file():
    while global_lock.locked():
        sleep(0.01)
        continue

    global_lock.acquire()

    with open("thread_writes", "a+") as file:
        file.write(str(threading.get_ident()))
        file.write("\n")
        file.close()

    global_lock.release()

# Create a 200 threads, invoke write_to_file() through each of them,
# and 
threads = []
st = datetime.now()

for i in range(1, 20):
    print (i)
    t = threading.Thread(target=write_to_file)
    threads.append(t)
    t.start()
[thread.join() for thread in threads]

nd = datetime.now()
print ("Ex time: ", (nd - st).total_seconds())
print('threads', threads)
'''

import queue
import threading
import time

# Class
class MultiThread(threading.Thread):
  def __init__(self, name):
    threading.Thread.__init__(self)
    self.name = name

  def run(self):
    print(f"Output ** Starting the thread - {self.name}")
    process_queue()
    print(f" ** Completed the thread - {self.name}")

# Process thr queue
def process_queue():
  while True:
    try:
      value = my_queue.get(block=False)
      print('in try', value)
    except queue.Empty:
      print('queue empty')
      return
    else:
      print_multiply(value)
      time.sleep(2)

# function to multiply
def print_multiply(x):
  output_value = []
  for i in range(1, x + 1):
    output_value.append(i * x)
  print(f" *** The multiplication result for the {x} is - {output_value}")

# Input variables
input_values = [2, 4, 6, 5,10,3]

# fill the queue
my_queue = queue.Queue()
for x in input_values:
  my_queue.put(x)
# initializing and starting 3 threads
thread1 = MultiThread('First')
thread2 = MultiThread('Second')
thread3 = MultiThread('Third')
thread4 = MultiThread('Fourth')

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Join the threads
thread1.join()
thread2.join()
thread3.join()
thread4.join()