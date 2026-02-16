"""
This is the main entry point for the CLI Log Analyzer project.

- Write experimental script: basic coroutine with `await asyncio.sleep()`
- Write experimental script: `asyncio.gather()` reading multiple files concurrently
- Write experimental script: `async for` with an async generator
"""

import asyncio


async def main():
    await exercise_1()
    results = await asyncio.gather(exercise_2_file1(), exercise_2_file2(), exercise_2_file3())
    print(results)


async def exercise_1():
    # Step 1: Basic coroutine with `await asyncio.sleep()`
    print("Starting the CLI Log Analyzer...")
    await asyncio.sleep(1)  # Simulate some startup delay
    print("Initialization complete.")


async def exercise_2_file1():
    # Step 2: `asyncio.gather()` reading multiple files concurrently
    with open("./sample_logs/access.log", "r") as f:
        data = f.read()
    return data


async def exercise_2_file2():
    # Step 2: `asyncio.gather()` reading multiple files concurrently
    with open("./sample_logs/error.log", "r") as f:
        data = f.read()
    return data


async def exercise_2_file3():
    # Step 2: `asyncio.gather()` reading multiple files concurrently
    with open("./sample_logs/app.log", "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    asyncio.run(main())
