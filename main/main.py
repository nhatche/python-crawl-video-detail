'''
yObj = youtubeDetail()

yObj.getVideoDetail('JGwWNGJdvx8')

'''
from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import time

from classes.youtubeDetailClass import youtubeDetail
from classes.csvHandleClass import csvHandle

listId = [
'JGwWNGJdvx8',
'HCjNJDNzw8Y',
'k2qgadSvNyU',
'lp-EO5I60KA',
'OPf0YbXqDm0',
'RgKAFK5djSk',
'3tmd-ClpJxA',
'09R8_2nJtjg',
'60ItHLz5WEA',
'rtOvBOTyX00',
'NGLxoKOvzu4',
'papuvlVeZg8',
'3AtDnEC4zak',
'Io0fBr1XBUA',
'pRpeEdMmmQ0',
'hT_nvWreIhg',
'ALZHF5UqnU4',
'wIft-t-MQuE',
'LjhCEhWiKXk',
'fLexgOxsZu0',
]

base_url = 'https://www.youtube.com/watch?v='

dataQueue = Queue()
csvQueue = Queue()

listData = []

def getData(id):
  y = youtubeDetail()
  data = y.getVideoDetail(base_url+id)
  dataQueue.put(data)
  listData.append(data)
 
t0 = Thread(target=getData, args=(listId[0],))
t1 = Thread(target=getData, args=(listId[1],))
t2 = Thread(target=getData, args=(listId[2],))
t3 = Thread(target=getData, args=(listId[3],))
t4 = Thread(target=getData, args=(listId[4],))
t5 = Thread(target=getData, args=(listId[5],))
t6 = Thread(target=getData, args=(listId[6],))
t7 = Thread(target=getData, args=(listId[7],))
t8 = Thread(target=getData, args=(listId[8],))
t9 = Thread(target=getData, args=(listId[9],))
t10 = Thread(target=getData, args=(listId[10],))
t11 = Thread(target=getData, args=(listId[11],))
t12 = Thread(target=getData, args=(listId[12],))
t13 = Thread(target=getData, args=(listId[13],))
t14 = Thread(target=getData, args=(listId[14],))
t15 = Thread(target=getData, args=(listId[15],))
t16 = Thread(target=getData, args=(listId[16],))
t17 = Thread(target=getData, args=(listId[17],))
t18 = Thread(target=getData, args=(listId[18],))
t19 = Thread(target=getData, args=(listId[19],))

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()

t0.join()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()
t19.join()

# csv = csvHandle()
# csv.HandleInfomation(listData)
# csv.showInfo()


#----------------------------------------------------------------------------------




# CSV writer setup goes here

# listData = []

# queue = Queue()


# def consume():
#     while True:
#         if not queue.empty():
#             data = queue.get(block=False)
            
#             # Row comes out of queue; CSV writing goes here
#             listData.append(data)
            
#             print(data)
#         else:
#           return


# consumer = Thread(target=consume)
# # consumer.setDaemon(True)
# consumer.start()


# def produce(i):
#     # Data processing goes here; row goes into queue
#     y = youtubeDetail()
#     data = y.getVideoDetail(listLinks[i])
#     queue.put(data)


# with ThreadPoolExecutor(max_workers=20) as executor:
#     for i in range(20):
#         executor.submit(produce, i)

# consumer.join()

# print(listData)