from .IngestorInterface import IngestorInterface
from .DOCXIngestor import DOCXIngestor
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor

from typing import List
from ..QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    ingestors = [DOCXIngestor, TXTIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
