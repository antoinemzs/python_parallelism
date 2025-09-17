import asyncio
import logging
import time

from parallel.asyncio.compute import lock_before_running


async def run_async(target, use_lock: bool = False, num_tasks: int = 10):
    lock = asyncio.Lock()
    if use_lock:
        tasks = [
            asyncio.create_task(lock_before_running(lock, target))
            for _i in range(0, num_tasks)
        ]
    else:
        tasks = [asyncio.create_task(target()) for _i in range(0, num_tasks)]

    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()

    logging.info("Time taken in seconds: {}".format(end - start))
