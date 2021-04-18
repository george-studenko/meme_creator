"""This module is in charge of loading quotes from txt files."""
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """This class is in charge of loading quotes from txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt and return list of quotes."""
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
            raise exception('An error occurred when trying to parse a txt file')
