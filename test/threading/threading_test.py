import unittest

from parallel.compute import cpu_bound_task, io_bound_task
from parallel.threading.run import run_in_threads


class ThreadingTest(unittest.TestCase):
    def test_cpu_bound_with_lock(self):
        run_in_threads(cpu_bound_task, num_threads=10, use_lock=True)

    def test_cpu_bound_no_lock(self):
        run_in_threads(cpu_bound_task, num_threads=10, use_lock=False)

    def test_io_bound_with_lock(self):
        run_in_threads(io_bound_task, num_threads=2, use_lock=True)

    def test_io_bound_no_lock(self):
        run_in_threads(io_bound_task, num_threads=10, use_lock=False)
