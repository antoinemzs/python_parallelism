import asyncio

from parallel.asyncio.compute import io_bound_task
from parallel.asyncio.run import run_async


async def main():
    await run_async(io_bound_task, num_tasks=2, use_lock=True)


if __name__ == "__main__":
    asyncio.run(main())
