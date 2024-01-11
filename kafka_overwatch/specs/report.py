# generated by datamodel-codegen:
#   filename:  report.json

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union


@dataclass
class Metadata:
    timestamp: str
    """
    Time the report was generated at
    """


@dataclass
class ConsumerGroups:
    total: int
    """
    Total number of consumer groups
    """
    active: int | None = None
    """
    Number of active consumer groups (lag = 0) & members > 0
    """
    inactive: int | None = None
    """
    Number of inactive consumer groups (lag > 0) or groups without members
    """


@dataclass
class Statistics:
    topics: int
    """
    Total count of topics counted at the time of generating the report
    """
    partitions: int | None = None
    """
    Sum of partitions for the topics
    """
    most_active_topics: list[str] | dict[str, Any] | None = None
    """
    Topics in the 0.75 percentile of number of messages and new_messages which active consumer groups
    """
    consumer_groups: ConsumerGroups | None = None


@dataclass
class TopicWasteCategory:
    topics: dict[str, int]
    topic_partitions_sum: int
    description: str
    """
    The description of the category
    """
    topics_count: int | None = None
    cluster_percentage: float | None = None
    """
    The percentage of topics fit into that category within the cluster
    """


@dataclass
class EstimatedWaste:
    topics: int | None = None
    partitions: int | None = None
    """
    Sum of partitions for the topics
    """
    topic_categories: dict[str, TopicWasteCategory] | None = None


@dataclass
class ClusterReport:
    cluster_name: str
    metadata: Metadata
    statistics: Statistics | None = None
    estimated_waste: EstimatedWaste | None = None


@dataclass
class ClusterUsageReportStructure:
    """
    Defines the format of the cluster topics report
    """

    cluster: ClusterReport | None = None
