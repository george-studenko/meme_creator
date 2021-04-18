"""Quote model."""
class QuoteModel:
    """The model to contain quotes."""

    def __init__(self, body, author):
        """Each quote contains a body and an author."""
        self.body = body
        self.author = author
