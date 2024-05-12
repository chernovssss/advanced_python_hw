import math
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from multiprocessing import Process
from threading import Thread

from loguru import logger


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result

    return wrapper


# @timeit
def fibonacci(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


@timeit
def one_hundred_times(n):
    for _ in range(100):
        fibonacci(n)


@timeit
def ten_threads_ten_times(n):
    for _ in range(10):
        threads = [Thread(target=fibonacci, args=(n,)) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


@timeit
def ten_processes_ten_times(n):
    for _ in range(10):
        processes = [Process(target=fibonacci, args=(n,)) for _ in range(10)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()


def fibonacci_main():
    one_hundred_times(1000000)
    ten_threads_ten_times(1000000)
    ten_processes_ten_times(1000000)


@timeit
def integrate(f, a, b, *, n_jobs=1, n_iter=1_000_000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


@logger.catch
@timeit
def integrate_concurrent(f, a, b, *, n_jobs=1, n_iter=1_000_000,
                         concurrent_func=ProcessPoolExecutor):
    acc = 0
    step_size = (b - a) / n_iter
    n_steps = n_iter // n_jobs
    with concurrent_func(max_workers=n_jobs) as executor:
        futures = (executor.submit(integrate_chunk, f,
                                   a + i * step_size,
                                   a + (i + 1) * step_size, step_size) for i in
                   range(n_steps))
        for future in as_completed(futures):
            acc += future.result()
    return acc


def integrate_chunk(f, a, b, step):
    acc = 0
    for i in range(int((b - a) / step)):
        acc += f(a + i * step) * step
    return acc


def integrate_main():
    logger.add('../artifacts/42.log', format='{time} {level} {message}',
               level='INFO', colorize=True)
    logger.info('Start base')
    for n_jobs in [2 ** i for i in range(2, 5)]:
        logger.info(f'Start base with {n_jobs} jobs')
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        logger.info(f'Start base with {n_jobs} jobs')
    logger.info('End base')
    logger.info('Start concurrent')
    for concurrent_func in [ProcessPoolExecutor, ThreadPoolExecutor]:
        for n_jobs in [2 ** i for i in range(2, 5)]:
            logger.info(f'Start {concurrent_func.__name__} with {n_jobs} jobs')
            integrate_concurrent(math.cos, 0, math.pi / 2,
                                 n_jobs=n_jobs, concurrent_func=concurrent_func)


if __name__ == '__main__':
    # fibonacci_main()
    integrate_main()
