import time

while True:
    with open("/tmp/current_time.txt", "w") as f:
        f.write("The time is now " + time.ctime())
    time.sleep(5)
