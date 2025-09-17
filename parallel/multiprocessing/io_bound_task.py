from parallel.compute import io_bound_task
from parallel.multiprocessing.run import run_in_processes


def main():
    run_in_processes(io_bound_task, 10)


if __name__ == "__main__":
    main()
