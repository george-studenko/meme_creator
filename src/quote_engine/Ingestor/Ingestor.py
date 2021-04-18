"""Strategy pattern to be able to parse any supported file type."""
from .IngestorInterface import IngestorInterface
from .DOCXIngestor import DOCXIngestor
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor

from typing import List
from ..QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Implements the Ingestor interface and groups all concrete classes."""

    ingestors = [DOCXIngestor, TXTIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file if there is an ingestor that supports it."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
