from parallel.compute import cpu_bound_task
from parallel.threading.run import run_in_threads


def main():
    run_in_threads(cpu_bound_task, num_threads=10, use_lock=False)


if __name__ == "__main__":
    main()
