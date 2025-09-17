import logging
import threading
import time

from parallel.compute import lock_before_running


def run_in_threads(target, use_lock: bool = False, num_threads: int = 1):
    lock = threading.Lock()
    if use_lock:
        threads = [
            threading.Thread(
                target=lock_before_running,
                args=(
                    lock,
                    target,
                ),
            )
            for _i in range(1, num_threads)
        ]
    else:
        threads = [threading.Thread(target=target) for _i in range(1, num_threads)]

    start = time.time()
    for t in threads:
        t.start()

    # also run in main thread
    if use_lock:
        lock_before_running(lock, target)
    else:
        target()

    for t in threads:
        t.join()
    end = time.time()

    logging.info("Time taken in seconds: {}".format(end - start))
