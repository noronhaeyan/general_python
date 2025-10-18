import asyncio

from random import randint

class AsyncIterable:
    def __init__(self, stop):
        self._stop = stop
        self._index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index >= self._stop:
            raise StopAsyncIteration
        await asyncio.sleep(value := randint(1, 3))
        self._index += 1
        return value

async def main():
    async for number in AsyncIterable(4):
        print(number)

if __name__ == "__main__":
    asyncio.run(main())
    # Output:
    # 3
    # 3
    # 2
    # 1
