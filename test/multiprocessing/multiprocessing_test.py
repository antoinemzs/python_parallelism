import unittest

from parallel.compute import cpu_bound_task, io_bound_task
from parallel.multiprocessing.run import run_in_processes


class MultiprocessingTest(unittest.TestCase):
    def test_cpu_bound_with_lock(self):
        run_in_processes(cpu_bound_task, num_processes=10, use_lock=True)

    def test_cpu_bound_no_lock(self):
        run_in_processes(cpu_bound_task, num_processes=10, use_lock=False)

    def test_io_bound_with_lock(self):
        run_in_processes(io_bound_task, num_processes=2, use_lock=True)

    def test_io_bound_no_lock(self):
        run_in_processes(io_bound_task, num_processes=10, use_lock=False)
