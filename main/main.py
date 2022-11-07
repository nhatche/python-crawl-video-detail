from multiprocessing import Process, Queue
from classes.YoutubeDetailClass import YoutubeDetail
from classes.CsvHandleClass import CsvHandle
import subprocess
import webbrowser
import time
import os

import time,webbrowser, pyautogui
import keyboard

list_id = [
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

def open_close(id, additional_time):
    webbrowser.open_new_tab(base_url+id)
    time.sleep(10+additional_time)
    try:
      # pyautogui.hotkey('ctrl', 'w')
      keyboard.press_and_release('ctrl+w')
    except:
      print("chrome already closed")
    finally:
      print("finish")

def getData(queue, id):
  y = YoutubeDetail()
  data = y.getVideoDetail(base_url+id)
  link_video = base_url+id
  time_video = data[2]
  print('time video:',time_video, ",linkVideo:",link_video)
  queue.put(data)

def check_queue(queue, csv):
  time.sleep(1)
  while True:
    if queue.empty():
      break
    data = queue.get()
    print('in checkqueue: ', data)
    csv.handle_one_informatio(data)

def run(queue1, csv):
  for i in range(20):
    p = Process(target=getData, args=(queue1, list_id[i],))
    p.start()
    processes.append(p)

  #join 20 threads
  for process in processes:
    process.join()

  #thread to checkQueue
  queue_thread = Process(target=check_queue, args=(queue1,csv,))
  queue_thread.start()
  queue_thread.join()


  processes_browser = []
  max_time = 20
  for i in range(20):
    # additional_time = i/50
    p1 = Process(target=open_close, args=(list_id[i], i ,))
    processes_browser.append(p1)
    p1.start()
    
  #join 20 threads
  for process in processes_browser:
    process.join()

if __name__ == '__main__':


  processes = []
  queue1 = Queue()
  csv = CsvHandle()

  while(True):
    run(queue1, csv)
    time.sleep(5)
  # #create and run 20 threads
  # for i in range(20):
  #   p = Process(target=getData, args=(queue1, list_id[i],))
  #   p.start()
  #   processes.append(p)

  # #join 20 threads
  # for process in processes:
  #   process.join()

  # #thread to checkQueue
  # queue_thread = Process(target=check_queue, args=(queue1,csv,))
  # queue_thread.start()
  # queue_thread.join()


  # processes_browser = []
  # max_time = 20
  # for i in range(20):
  #   # additional_time = i/50
  #   p1 = Process(target=open_close, args=(list_id[i], i ,))
  #   processes_browser.append(p1)
  #   p1.start()
    
  # #join 20 threads
  # for process in processes_browser:
  #   process.join()

  

