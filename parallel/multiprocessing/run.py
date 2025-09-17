import multiprocessing
import time

from parallel.compute import lock_before_running


def run_in_processes(target, use_lock: bool = False, num_processes: int = 1):
    lock = multiprocessing.Lock()
    if use_lock:
        processes = [
            multiprocessing.Process(
                target=lock_before_running,
                args=(
                    lock,
                    target,
                ),
            )
            for _i in range(1, num_processes)
        ]
    else:
        processes = [
            multiprocessing.Process(target=target) for _i in range(1, num_processes)
        ]
    start = time.time()
    for p in processes:
        p.start()

    # also run in main thread
    if use_lock:
        lock_before_running(lock, target)
    else:
        target()

    for p in processes:
        p.join()
    end = time.time()

    print("Time taken in seconds:", end - start)
