from multiprocessing import Process, Queue
from classes.YoutubeDetailClass import youtubeDetail
from classes.CsvHandleClass import csvHandle
import subprocess
import webbrowser
import time
import os


def f(queue, i):
  print('hello: ', i)

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

csv = csvHandle()
def getData(queue, id, index):
  y = youtubeDetail()
  data = y.getVideoDetail(base_url+id)
  linkVideo = base_url+id
  timeVideo = data[2]
  print('time video:',timeVideo, ",linkVideo:",linkVideo)
  queue.put(data)

  #thao browser process
  # browser = subprocess.Popen(rf'"C:\Program Files\Google\Chrome\Application\chrome.exe" --kiosk {linkVideo}')
  # time.sleep(10)
  # browser.kill()

  # webbrowser.open(url)
  #   time.sleep(20)
  #   pyautogui.hotkey('ctrl', 'w')
  #   print("tab closed")


def checkQueue(queue):
  time.sleep(1)
  while True:
    if queue.empty():
      break
    data = queue.get()
    print('in checkqueue: ', data)
    csv.HandleOneInfomation(data)


if __name__ == '__main__':
  processes = []
  queue1 = Queue()
  for i in range(20):
    p = Process(target=getData, args=(queue1, listId[i], i,))
    p.start()
    processes.append(p)

  for process in processes:
    process.join()

  queueThread = Process(target=checkQueue, args=(queue1,))
  queueThread.start()
  queueThread.join()
  