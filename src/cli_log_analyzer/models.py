"""
Different datamodels used in the CLI Log Analyzer project.
"""

from dateutil import parser


class LogEntry:
    def __init__(self, timestamp, level, source, message, metadata):
        self.timestamp = parser.parse(timestamp)
        self.level = level
        self.source = source
        self.message = message
        self.metadata = metadata


class LogFilter:
    def __init__(self, logs, filter):
        self.logs = logs
        self.filter = filter
