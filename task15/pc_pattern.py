from collections import deque
from threading import Thread, Lock
from time import sleep, time

import numpy as np
from numpy.linalg import matrix_power

task_queue = deque()
queue_lock = Lock()
THREAD_COUNT = 5


def producer():
    size = 1
    for _ in range(0, 100, 1):
        task = (size, 2, 2)
        with queue_lock:
            task_queue.append(task)
        size += 1
        sleep(0.1)

    for _ in range(THREAD_COUNT):
        with queue_lock:
            task_queue.append(None)


def process(size: int, value: int, times: int) -> int:
    matrix = np.array([[value ** (i + j) for i in range(size)] for j in range(size)])
    matrix_power(matrix, times)

    return np.sum(matrix)


def consumer():
    while True:
        task = None
        with queue_lock:
            if task_queue:
                task = task_queue.popleft()
                if task is None:
                    break
        if task: print(f'Task: {task}, result: {process(*task)}')

begin = time()
producer = Thread(target=producer, args=[])
producer.start()

thread_pool = list()
for i in range(THREAD_COUNT):
    thread_pool.append(Thread(target=consumer, args=[]))
    thread_pool[-1].start()

producer.join()
for thr in thread_pool:
    thr.join()
print(time() - begin)
