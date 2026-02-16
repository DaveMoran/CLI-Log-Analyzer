"""
This is the main entry point for the CLI Log Analyzer project.

- Write experimental script: basic coroutine with `await asyncio.sleep()`
- Write experimental script: `asyncio.gather()` reading multiple files concurrently
- Write experimental script: `async for` with an async generator
"""

from time import time
import asyncio


async def main():
    await exercise_1()

    start_time = time()
    file_1 = "./sample_logs/access.log"
    file_2 = "./sample_logs/error.log"
    file_3 = "./sample_logs/app.log"

    await asyncio.gather(read_file(file_1), read_file(file_2), read_file(file_3))

    end_time = time()
    print(f"Reading all files concurrently took {end_time - start_time:.4f} seconds.")

    files = [file_1, file_2, file_3]

    start_time = time()
    async for content in multi_read_file(files):
        print("Done!")
    end_time = time()
    print(f"Reading all files took {end_time - start_time:.4f} seconds.")

    start_time = time()
    for file in files:
        read_file_sync(file)
    end_time = time()
    print(f"Reading all files synchronously took {end_time - start_time:.4f} seconds.")


async def exercise_1():
    # Step 1: Basic coroutine with `await asyncio.sleep()`
    start_time = time()
    print("Starting the CLI Log Analyzer...")
    await asyncio.sleep(1)  # Simulate some startup delay
    print("Initialization complete.")
    end_time = time()
    print(f"Initialization took {end_time - start_time:.2f} seconds.")


async def read_file(file_path):
    # Step 2: `asyncio.gather()` reading multiple files concurrently
    with open(file_path, "r") as f:
        data = f.read()
    return data


async def multi_read_file(file_paths):
    # Step 3: `async for` with an async generator
    for file_path in file_paths:
        yield await read_file(file_path)


def read_file_sync(file_path):
    with open(file_path, "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    asyncio.run(main())
