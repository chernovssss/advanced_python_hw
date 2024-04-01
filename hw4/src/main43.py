import datetime
import sys
import time
from codecs import encode
from multiprocessing import Process, Queue


def is_time_passed(start_time):
    return time.time() - start_time > 5


def process_a(qa: Queue, qb: Queue):
    start_time = time.time()
    while True:
        if is_time_passed(start_time):
            item = qa.get()
            item = str(item).lower()
            qb.put(item)
            start_time = time.time()


def process_b(qb: Queue):
    while True:
        item = qb.get()
        sys.stdout.write(f'{datetime.datetime.now()} | roflaninfo | {item} -> {encode(item, "rot_13")}\n')


if __name__ == "__main__":
    qA = Queue()
    qB = Queue()
    A = Process(target=process_a, args=(qA, qB,), daemon=True)
    B = Process(target=process_b, args=(qB,), daemon=True)
    A.start()
    B.start()
    message = ''
    while True:
        message = input()
        if message == 'exit':
            # я не знаю насколько это безопасно
            # наверное стоило добавить условия остановки в циклы методов
            # qA.put(message)
            # qB.put(message)
            # в таком случае мы еще и дождемся пока очередь закончится
            # и все строки обработаются, но так не очень весело
            A.terminate()
            B.terminate()
            break
        qA.put(message)
