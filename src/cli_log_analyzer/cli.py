"""
This is the main entry point for the CLI Log Analyzer project.

- Write experimental script: basic coroutine with `await asyncio.sleep()`
- Write experimental script: `asyncio.gather()` reading multiple files concurrently
- Write experimental script: `async for` with an async generator
"""

import asyncio


async def main():
    print("Hello before sleep")
    await asyncio.sleep(5)
    print("Hello after sleep")


if __name__ == "__main__":
    asyncio.run(main())
