from pathlib import Path
from services.loaders.base import BaseLoader
from core.logger import get_logger
from services.loaders.providers.pdf_loader import PDFLoader

LOADERS = {
    ".pdf": PDFLoader,
}

logger = get_logger(__name__)
class LoaderFactory:
    @staticmethod
    def create(file_path: str) -> BaseLoader:
        extension = Path(file_path).suffix.lower()
        loader_class = LOADERS.get(extension)
        if loader_class is None:
            raise NotImplementedError(f"Loader {extension} not implemented yet.")
        logger.info(f"Creating Loader for: {file_path}")
        return loader_class(file_path)

