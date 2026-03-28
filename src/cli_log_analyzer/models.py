"""
Different datamodels used in the CLI Log Analyzer project.
"""

from dateutil import parser


class LogEntry:
    """
    Normalizes a log entry into standardized fields so that they are easier
    to filter and search through

    Parameters:
    -----------
      timestamp: the date/time that the log occured
      level:     the level of severity of the log entry
      source:    file and line number that the log originated from
      message:   text that was received with the log
      metadata:  additional information to be saved along each entry
    """

    def __init__(self, timestamp, level, source, message, metadata):
        self.timestamp = parser.parse(timestamp)
        self.level = level
        self.source = source
        self.message = message
        self.metadata = metadata


class LogFilter:
    """
    Takes a collection of logs and returns logs that match the desired filters
    of the user

    Parameters:
    -----------
      logs:     a collection of LogEntry entries
      filter:   an object that will be used to filter out the logs
    """

    def __init__(self, logs, filter):
        self.logs = logs
        self.filter = filter


class AggregationResult:
    def __init__(self, logs):
        self.logs = logs
        self.report = {}
