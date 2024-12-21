import queue
from random import randint
from threading import Thread

import numpy as np
from scipy.sparse.linalg import matrix_power

task_queue = queue.Queue()
THREAD_COUNT = 5


def producer():
    size = 1
    while True:
        task = (size, randint(1, 3), randint(1, 5))
        task_queue.put(task)
        size += 1


def process(size: int, value: int, times: int) -> int:
    matrix = np.array([[value ** (i + j) for i in range(size)] for j in range(size)])
    matrix_power(matrix, times)

    return np.sum(matrix)


def consumer():
    while True:
        task = task_queue.get()
        print(f'Task: {task}, result: {process(*task)}')


producer = Thread(target=producer, args=[])
producer.start()

thread_pool = list()
for i in range(THREAD_COUNT):
    consumer = Thread(target=consumer, args=[])
    thread_pool.append(consumer)
    consumer.start()

producer.join()
for thr in thread_pool:
    thr.join()
