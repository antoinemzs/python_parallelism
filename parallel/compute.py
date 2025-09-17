import logging
import multiprocessing
import threading
import time


def io_bound_task():
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "start",
        )
    )
    for i in range(1, 10):
        time.sleep(1)  # wait for io q｡-ᆺ-｡p <(Zzz)
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "done",
        )
    )


def cpu_bound_task():
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "start",
        )
    )
    for i in range(1, 1_000_000):
        float(str(i + i / 24.0))  # compute very hard (૭｡•̀ᵕ•́｡)૭
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "done",
        )
    )


def lock_before_running(lock, target):
    with lock:
        target()
