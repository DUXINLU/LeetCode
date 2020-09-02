import threading, time

threads = []


def run(num):
    if num == 0:
        for i in range(10):
            print(num)
            time.sleep(0.1)
    else:
        for i in range(10):
            print(num)
            time.sleep(0.2)


for i in range(3):
    t = threading.Thread(target=run, args=(i,))
    threads.append(t)

for t in threads:
    t.setDaemon(True)
    t.start()

threads[0].join()

print('main thread end.%s' % threading.current_thread().name)