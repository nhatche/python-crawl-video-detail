from multiprocessing import Process, Queue
import time
from classes.YoutubeDetailClass import youtubeDetail
from classes.CsvHandleClass import csvHandle

# def f(q):
#   q.put([42, None, 'hello'])

def f(q):
  print('hello')


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


def getData(queue, id):
  y = youtubeDetail()
  data = y.getVideoDetail(base_url+id)
  queue.put(data)
 

if __name__ == '__main__':



  start=time.time()


 
  queue = Queue()
  processes = []
  for i in range(20):
    
    p = Process(target=getData, args=[queue, listId[i],])
    print(queue.get())
    p.start()
    processes.append(p)

  for process in processes:
    process.join()


  # process0 = Process(target=f, args=(queue,))
  # process1 = Process(target=f, args=(queue,))
  # process2 = Process(target=f, args=(queue,))
  # process3 = Process(target=f, args=(queue,))
  # process4 = Process(target=f, args=(queue,))
  # process5 = Process(target=f, args=(queue,))
  # process6 = Process(target=f, args=(queue,))
  # process7 = Process(target=f, args=(queue,))
  # process8 = Process(target=f, args=(queue,))
  # process9 = Process(target=f, args=(queue,))
  # process10 = Process(target=f, args=(queue,))
  # process11 = Process(target=f, args=(queue,))
  # process12 = Process(target=f, args=(queue,))
  # process13 = Process(target=f, args=(queue,))
  # process14 = Process(target=f, args=(queue,))
  # process15 = Process(target=f, args=(queue,))
  # process16 = Process(target=f, args=(queue,))
  # process17 = Process(target=f, args=(queue,))
  # process18 = Process(target=f, args=(queue,))
  # process19 = Process(target=f, args=(queue,))

  # process0.start()
  # process1.start()
  # process2.start()
  # process3.start()
  # process4.start()
  # process5.start()
  # process6.start()
  # process7.start()
  # process8.start()
  # process9.start()
  # process10.start()
  # process11.start()
  # process12.start()
  # process13.start()
  # process14.start()
  # process15.start()
  # process16.start()
  # process17.start()
  # process18.start()
  # process19.start()

  # process0.join()
  # process1.join()
  # process2.join()
  # process3.join()
  # process4.join()
  # process5.join()
  # process6.join()
  # process7.join()
  # process8.join()
  # process9.join()
  # process10.join()
  # process11.join()
  # process12.join()
  # process13.join()
  # process14.join()
  # process15.join()
  # process16.join()
  # process17.join()
  # process18.join()
  # process19.join()

  end=time.time()
  print("time", end-start)