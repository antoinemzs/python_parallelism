from parallel.compute import cpu_bound_task
from parallel.multiprocessing.run import run_in_processes


def main():
    run_in_processes(cpu_bound_task, num_processes=10, use_lock=True)


if __name__ == "__main__":
    main()
