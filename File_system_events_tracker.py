import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/240125/Downloads/Project102"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey,{event.scr_path} has been created!")
    def on_deleted(self,event):
        print(f"Oops! Someone deleted{event.scr_path}!")    


event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir,recursive=True)
observer.start()    
try:
 while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
 print("stopped!")
observer.stop()

            
