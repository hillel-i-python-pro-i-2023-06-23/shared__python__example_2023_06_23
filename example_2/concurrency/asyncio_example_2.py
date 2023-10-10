import asyncio

from example_2.concurrency.example_2_helpers.main import main
from example_2.logging.init_logging import init_logging

if __name__ == "__main__":
    init_logging()

    asyncio.run(main())
    # asyncio.get_event_loop().run_until_complete(main())
