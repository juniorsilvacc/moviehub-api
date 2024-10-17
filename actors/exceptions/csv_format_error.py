class CSVFormatError(Exception):
    """Exceção levantada para erros no formato do CSV."""
    def __init__(self, message="O formato do arquivo CSV está incorreto."):
        self.message = message
        super().__init__(self.message)
