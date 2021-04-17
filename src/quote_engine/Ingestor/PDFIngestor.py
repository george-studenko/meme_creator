from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel
import subprocess
import os


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quotes = []

        text_file_path = 'text.txt'
        try:
            call = subprocess.call(['pdftotext', path, text_file_path])
            with open(text_file_path, 'r') as txt:
                rows = txt.readlines()
                for row in rows:
                    if len(row) > 1:
                        body, author = row.split(' - ')
                        quotes.append(QuoteModel(body, author))
            os.remove(text_file_path)
            return quotes
        except Exception as exception:
            raise exception
