import multiprocessing
import time


def run_in_processes(target, num_threads: int = 1):
    threads = [multiprocessing.Process(target=target) for _i in range(1, num_threads)]
    start = time.time()
    for t in threads:
        t.start()

    # also run in main thread
    target()

    for t in threads:
        t.join()
    end = time.time()

    print("Time taken in seconds:", end - start)
