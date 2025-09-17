import unittest

from parallel.asyncio.compute import cpu_bound_task, io_bound_task
from parallel.asyncio.run import run_async


class AsyncioTest(unittest.IsolatedAsyncioTestCase):
    async def test_cpu_bound_with_lock(self):
        await run_async(cpu_bound_task, num_tasks=10, use_lock=True)

    async def test_cpu_bound_no_lock(self):
        await run_async(cpu_bound_task, num_tasks=10, use_lock=False)

    async def test_io_bound_with_lock(self):
        await run_async(io_bound_task, num_tasks=2, use_lock=True)

    async def test_io_bound_no_lock(self):
        await run_async(io_bound_task, num_tasks=10, use_lock=False)
