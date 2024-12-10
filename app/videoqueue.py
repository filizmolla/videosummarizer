import uuid
import threading
import time
import signal
from typing import List
from models import Video
from videosummarize import summarize
from videodb import get_empty_videos, Session

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  
            cls._instance = super(Singleton, cls).__new__(cls) 
        return cls._instance


class VideoQueue(Singleton):    

    def __init__(self):
        self.id = uuid.uuid4()
        self.queue = []

    def enqueue(self, item):
        print(f"Video {item[0].id} kuyruğa eklendi.")
        self.queue.append(item)

    def dequeue(self, head):
        self.queue.remove(head)

    def run(self, operation):
        
        def process():
            while not self._stop_event.is_set():
                if len(self.queue) > 0:
                    head = self.queue[0]
                    operation(head)
                    self.dequeue(head)
                else:
                    time.sleep(1)
                

        self._stop_event = threading.Event()
        self.t1 = threading.Thread(target=process, args=())
        self.t1.start()
        
    def stop(self):
        self._stop_event.set()

class Video:
    id: int
    url: str
    processed: bool

    def __init__(self, id, url):
        self.id = id
        self.url = url
        self.processed = False


def operation(item):
    video: Video = item[0]
    second = item[1]
    print(video.id, video.url, second)


signal.signal(signal.SIGINT, signal.SIG_DFL)


videoQueue = VideoQueue()
videoQueue.run(operation=operation)


index = -1

def getWaitingURLs() -> List[Video]:
    global index
    index = index + 1
    print(index)
    if index == 0:
        return [
            Video(id=1, url="http://hello"),
            Video(id=2, url="http://hello"),
            Video(id=3, url="http://hello"),
        ]
    elif index == 1:
        return [
            Video(id=5, url="http://hello"),
            Video(id=6, url="http://hello"),
        ]
    elif index == 2:
        return []
    elif index == 3:
        return [
            Video(id=10, url="http://hello"),
            Video(id=11, url="http://hello"),
            Video(id=12, url="http://hello"),
            Video(id=13, url="http://hello"),
        ]
    else:
        return []

def enqueueWaitingURLs():
    while True:
        videos = getWaitingURLs()
        if len(videos) == 0:
            break
        for video in videos:
            videoQueue.enqueue((video, "123"))


class VideoProcessor(Singleton):
    _instance = None

    def __init__(self, enqueueWaitingURLs):
        self.enqueueWaitingURLs = enqueueWaitingURLs
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.checkdb_thread = None

    def run(self):
        if self.checkdb_thread == None or not self.checkdb_thread.is_alive():
            self.checkdb_thread = threading.Thread(target=self.enqueueWaitingURLs, args=())
            self.checkdb_thread.start()

    def is_thread_running(self):
        return self.checkdb_thread.is_alive()

videoprocessor = VideoProcessor(enqueueWaitingURLs=enqueueWaitingURLs)

videoprocessor.run()
videoprocessor.run()

time.sleep(4)

videoprocessor.run()

time.sleep(4)


print(videoprocessor.is_thread_running())

