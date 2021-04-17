from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []
        try:
            with open(path, 'r') as txt:
                rows = txt.readlines()
                for row in rows:
                    if len(row) > 1:
                        body, author = row.split(' - ')
                        quotes.append(QuoteModel(body, author))
            return quotes
        except Exception as exception:
            raise exception
