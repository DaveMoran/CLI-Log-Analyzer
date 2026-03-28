# Core Data Model

## LogEntry class
The LogEntry class will be used to create a normalized log entry regardless of how your source application is saving them. This class will take in the following parameters:
- timestamp: The string used to store the date/time of the log event. The timestamp may include a timezone in it, if it does not then we will default to UTC-0
- level: An enum used to determine the type of log we're storing (debug, info, warning, error, critical). These will be referenced from the default Pytrhon logging module
- source: Location of the log, usually a filename.
- message: The string that will display the message that was returned in the log.
- metadata: An object that stores custom data for the logger to maintain, like a correlation-id or trace-id

## LogFilter class
The LogFilter class will be used to take a custom filter and only return a list of log entries based on the existing params. For example, if you wanted to filter all of the Error logs from the multiple sources you've imported, then you could call 
```python
error_logs = LogFilter(logs=custom_log_collection, level=ERROR)
```

If you wanted to filter by a custom metadata item like trace_id you could do the following:
```python
user_logs = LogFilter(logs=custom_log_collection, metadata={trace_id: 'abc123'})
```

## AggregationResults class
The Aggregation Results class creates a summary of the logs that remained after filtering and reports back the following:
- total number of log entries
- last 5 logs
- Time of first and last log entry
- list of sources

This will be extendable as user cases are developed