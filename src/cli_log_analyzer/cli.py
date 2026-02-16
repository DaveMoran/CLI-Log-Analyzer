"""
This is the main entry point for the CLI Log Analyzer project.

- Write experimental script: basic coroutine with `await asyncio.sleep()`
- Write experimental script: `asyncio.gather()` reading multiple files concurrently
- Write experimental script: `async for` with an async generator
"""

import asyncio


async def main():
    await exercise_1()


async def exercise_1():
    # Step 1: Basic coroutine with `await asyncio.sleep()`
    print("Starting the CLI Log Analyzer...")
    await asyncio.sleep(1)  # Simulate some startup delay
    print("Initialization complete.")


if __name__ == "__main__":
    asyncio.run(main())
