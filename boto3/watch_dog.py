import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from sendto import send_file
from find_host_url import get_url
class ChangeHandler(PatternMatchingEventHandler):
    patterns = ["*/config.txt"]

    def __init__(self):
        super(ChangeHandler, self).__init__()

    def process(self, event):
        print("file has been modified")
        url=get_url()
        send_file(url)
    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)



if __name__ == '__main__':
    observer = Observer()
    observer.schedule(ChangeHandler(), path='.',
                      recursive=True)
    observer.start()
    while True:
        time.sleep(1)