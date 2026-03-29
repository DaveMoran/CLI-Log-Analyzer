"""
Different datamodels used in the CLI Log Analyzer project.
"""

from datetime import datetime
from dateutil import parser

from dataclasses import dataclass


class LogEntry:
    """
    Normalizes a log entry into standardized fields so that they are easier
    to filter and search through

    Parameters:
    -----------
      timestamp: the date/time that the log occurred
      level:     the level of severity of the log entry
      source:    file and line number that the log originated from
      message:   text that was received with the log
      metadata:  additional information to be saved along each entry
    """

    def __init__(self, timestamp: str, level: str, source: str, message: str, metadata: object):
        self.timestamp: datetime = parser.parse(timestamp)
        self.level: str = level
        self.source: str = source
        self.message: str = message
        self.metadata: object = metadata

    def __eq__(self, value: object) -> bool:
        """Checks to see if a LogEntry is the same as another"""
        return True

    def __repr__(self) -> str:
        """Prints out a representation of the variable"""
        return ""


class LogFilter:
    """
    Takes a collection of logs and returns logs that match the desired filters
    of the user

    Parameters:
    -----------
      logs:     a collection of LogEntry entries
      filter:   an object that will be used to filter out the logs
    """

    def __init__(self, logs: list[LogEntry], filter: object):
        self.logs: list[LogEntry] = logs
        self.filter: object = filter

    def __repr__(self) -> str:
        """Prints out a reporesentation of the variable"""
        return ""

    def __iter__(self):
        """Allows for the LogFilter entries to be looped over"""
        pass

    def __getitem__(self, key):
        """Allows retrieval of a specific filtered log"""
        pass

    def __len__(self):
        """Returns the number of items that were filtered out"""
        pass

    def __contains__(self, item):
        """Checks to see if a specific LogEntry item is in the filtered results"""
        pass


class AggregationResult:
    """
    Creates a report based on the collection of logs passed through

    Parameters:
    -----------
      logs:     a collection of LogEntry entries
    """

    def __init__(self, logs: list[LogEntry]):
        self.logs: list[LogEntry] = logs
        self.report: object = {}

    def __repr__(self) -> str:
        """Prints out a representation of the variable"""
        return ""


@dataclass
class PipelineConfig:
    """
    Creates a report based on the collection of logs passed through

    Parameters:
    -----------
      spacer:     check if we use a new line or spaced line for separation
      file_type:  type of file to parse (JSON, XML, CLF)
      filter:     filter to be passed through to LogFilter
    """

    spacer: bool
    file_type: str
    filter: object
