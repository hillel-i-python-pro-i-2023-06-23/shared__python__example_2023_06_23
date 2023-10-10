import asyncio
import random

from example_2.logging.init_logging import init_logging
from example_2.logging.loggers import get_core_logger


async def make_something():
    logger = get_core_logger()
    logger.info("Hello")
    await asyncio.sleep(1)
    logger.info("World")


async def make_something_with_arg(number: int) -> str:
    logger = get_core_logger()
    base_message = f"[{number}]"
    logger.info(f"{base_message} start")
    time_to_wait = random.randint(0, 5)
    logger.info(f"{base_message} wait for {time_to_wait}")
    await asyncio.sleep(time_to_wait)
    logger.info(f"{base_message} end")

    return f"{number} - done"


async def main():
    # await make_something()
    numbers = range(1, 11)

    tasks = [make_something_with_arg(number=number) for number in numbers]

    results = await asyncio.gather(
        *tasks,
    )

    print(results)

    # for number in numbers:
    #     await make_something_with_arg(number=number)


if __name__ == "__main__":
    init_logging()

    asyncio.run(main())
    # asyncio.get_event_loop().run_until_complete(main())
