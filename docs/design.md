# Design

## Async/Await

This project utilizes async/await in order to perform at scale both for the size of the file as well as any lag during the network requests for remotely deployed applications.

### Performance

```
Reading all files concurrently took 0.0930 seconds.
Reading all files took 0.0459 seconds.
Reading all files synchronously took 0.0532 seconds.
```

When initially planning this application out, one thing that was apparent was trying to find the best way to handle three separate issues:
1. What happens when an application has a large amount of logs to parse?
2. How will the application handle large files (> 5mb)
3. What happens when there is lag in a network?

In order to handle all three of these, a spike was done to compare the performance of three options: async gather, async for, and synchronous calls. The perfomance of these three in a test run can be seen above. Of the three, the async for pulls out ahead as the most performant when controlling for network lag by pulling local files.

As the asyncio package continues to improve along with the Python versions, this will be tested to ensure that the application uses the most performant option when considering all three of the constraints above. Additionally, the main advantage of async for the log reader is not raw throughput on local files, but non-blocking behavior: the event loop can process already-parsed log entries while new files are still being read. This becomes material at scale — parsing a million SQS-backed log records while concurrently downloading more is not possible with the synchronous approach.