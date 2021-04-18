"""Abstract interface to generalize Ingestors."""
from abc import ABC, abstractmethod
from typing import List
from ..QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestorInterface abstract interface."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        """To check if the file can be ingested by the concrete ingestor implementation."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To parse the current file format."""
        pass
