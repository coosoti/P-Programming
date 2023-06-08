# Asynchronous execution in Python using asyncio
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1")

async def task2():
    await asyncio.sleep(2)
    print("Task 2")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

