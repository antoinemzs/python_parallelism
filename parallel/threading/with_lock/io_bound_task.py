from parallel.compute import io_bound_task
from parallel.threading.run import run_in_threads


def main():
    run_in_threads(io_bound_task, num_threads=2, use_lock=True)


if __name__ == "__main__":
    main()
