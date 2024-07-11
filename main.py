import asyncio

from src.factory import BotFactory


if __name__ == "__main__":
    asyncio.run(BotFactory.start_bot())
