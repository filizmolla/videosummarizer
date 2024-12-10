from videodb import get_empty_videos, add_videos_to_db
import threading
import time 
from threading import Thread

def timer():
    while True:
        listen()
        time.sleep(10)

def process(video):
    if video.is_transcribed == False:
        video.is_transcribed = True
        add_videos_to_db([video])

def listen():
    while True:
        vl = get_empty_videos()
        if vl.__len__() > 0:
            for v in vl: 
                print(v)
                process(v)
                #thread = threading.Thread(target = process, args=v)
                #thread.start()
        else:
            print("no v")
            break


timer()

#print(threading.enumerate())

""""
post_new_video:
	if check_if_thread_not_running:
        start_thread -> listen
    return triggerd

start_thread -> timer

def timer -> 1dk
    while true:
        if check_if_thread_not_running:
            start_thread -> listen
        sleep 10000
        
"""



#def thread_function():
#  for i in range(5):
#    print("Thread ile Çağrıldı: " + str(i))
#    time.sleep(1)
#def function():
#  for i in range(5):
#    print(i)
#    time.sleep(3)
#
#thread_fun = Thread(target = thread_function)
#thread_fun.start()
#function()
#exit()
#