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

    files = [file_1, file_2, file_3]
    async for content in multi_read_rile(files):
        print(content)


async def exercise_1():
    # Step 1: Basic coroutine with `await asyncio.sleep()`
    print("Starting the CLI Log Analyzer...")
    await asyncio.sleep(1)  # Simulate some startup delay
    print("Initialization complete.")


async def read_file(file_path):
    # Step 2: `asyncio.gather()` reading multiple files concurrently
    with open(file_path, "r") as f:
        data = f.read()
    return data


async def multi_read_file(file_paths):
    # Step 3: `async for` with an async generator
    for file_path in file_paths:
        yield await read_file(file_path)


if __name__ == "__main__":
    asyncio.run(main())
