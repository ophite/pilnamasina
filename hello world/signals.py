import threading
import signal

threads = []

running = True

def f():
    while running:
        pass

for i in range(1):
    th = threading.Thread(target=f)
    threads.append(th)
    th.start()

def sig_handler(sig_num, frame):
    print('SIGNAL')
    global running
    running = False

signal.signal(signal.SIGINT, sig_handler)

for th in threads:
    th.join()