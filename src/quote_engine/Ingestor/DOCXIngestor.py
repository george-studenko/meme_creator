"""This module is in charge of loading quotes from DOCX files."""
from typing import List

from .IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel
import docx


class DOCXIngestor(IngestorInterface):
    """This module is in charge of loading quotes from docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx and return list of quotes."""
        quotes = []
        try:
            doc = docx.Document(path)

            for paragraph in doc.paragraphs:
                if len(paragraph.text) > 1:
                    body, author = paragraph.text.split(' - ')
                    quotes.append(QuoteModel(body, author))
            return quotes
        except Exception as exception:
            raise exception(
                'An error occurred when trying to parse a docx file')
