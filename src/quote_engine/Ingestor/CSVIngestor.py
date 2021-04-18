"""This module is in charge of loading quotes from csv files."""
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """This class is in charge of loading quotes from csv files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv and return list of quotes."""
        quotes = []
        try:
            rows = pd.read_csv(path, header=0)

            for _, row in rows.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)

            return quotes
        except Exception as exception:
            raise exception(
                'An error occurred when trying to parse a csv file')
