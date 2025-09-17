import asyncio

from parallel.asyncio.compute import io_bound_task
from parallel.asyncio.run import run_async


async def main():
    await run_async(io_bound_task, num_tasks=10, use_lock=False)


if __name__ == "__main__":
    asyncio.run(main())
