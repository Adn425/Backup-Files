import os
import shutil
import time

time = 30

path = input("Enter your path: ")

seconds = time.time() - (time * 24 * 60 * 60)

if os.path.exists(path):
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime

            if seconds >= ctime:
                os.remove(path)

        for name in dirs:
            path = os.path.join(root, name)
            ctime = os.stat(path).st_ctime

            if seconds >= ctime:
                shutil.rmtree(path)
else:
    print("Path not found")
