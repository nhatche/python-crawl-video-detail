from threading import Thread
import threading
import time
from queue import Queue
q1 = Queue()


def cal_cube(numbers):
    print("calculate cube number \n")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)
        q1.put(n*n)


def cal_square(numbers):

    print("calculate square number \n")
    for n in numbers:
        time.sleep(0.2)
        print ('cube:', n*n*n)
        q1.put(n*n*n)


value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


try:
    t = threading.Thread(target=cal_cube, args=(value,))
    t1 = threading.Thread(target=cal_square, args=(value,))
    t.start()
    t1.start()
    t.join()
    t1.join()
except:
    print("error")

print(q1.queue)
