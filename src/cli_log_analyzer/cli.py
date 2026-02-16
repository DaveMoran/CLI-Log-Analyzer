"""
This is the main entry point for the CLI Log Analyzer project.

- Write experimental script: basic coroutine with `await asyncio.sleep()`
- Write experimental script: `asyncio.gather()` reading multiple files concurrently
- Write experimental script: `async for` with an async generator
"""

import asyncio


async def main():
    await exercise_1()
    file_1 = "./sample_logs/access.log"
    file_2 = "./sample_logs/error.log"
    file_3 = "./sample_logs/app.log"
    results = await asyncio.gather(read_file(file_1), read_file(file_2), read_file(file_3))
    print(results)


async def exercise_1():
    # Step 1: Basic coroutine with `await asyncio.sleep()`
    print("Starting the CLI Log Analyzer...")
    await asyncio.sleep(1)  # Simulate some startup delay
    print("Initialization complete.")


async def read_file(file_path):
    with open(file_path, "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    asyncio.run(main())
