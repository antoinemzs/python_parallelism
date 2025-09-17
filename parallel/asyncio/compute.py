import asyncio
import logging
import multiprocessing
import threading


async def io_bound_task():
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "start",
        )
    )
    for i in range(1, 10):
        # async I/O
        await asyncio.sleep(1)  # wait for io q｡-ᆺ-｡p <(Zzz)
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "done",
        )
    )


async def cpu_bound_task():
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "start",
        )
    )
    # No await !!
    for i in range(1, 1_000_000):
        float(str(i + i / 24.0))  # compute very hard (૭｡•̀ᵕ•́｡)૭
    logging.info(
        "In process {}, thread {}: {}".format(
            multiprocessing.current_process().name,
            threading.current_thread().name,
            "done",
        )
    )


async def lock_before_running(lock, target):
    await lock.acquire()
    try:
        await target()
    finally:
        lock.release()
