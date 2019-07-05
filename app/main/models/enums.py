"""
All enums used in the schema are described here.
"""
import enum

class PostType(enum.Enum):
    research
    startup
    technology

class CommentType(enum.Enum):
    comment
    report
    highlight

class PriorityType(enum.Enum):
    less_of_these
    follow
    more_of_these
