from core.enums import SplitterStrategy
from core.logger import get_logger
from services.splitters.base import BaseSplitter
from services.splitters.strategies.recursive_splitter import RecursiveSplitter
from config.settings import settings

SPLITTER_REGISTRY = {
    SplitterStrategy.RECURSIVE: RecursiveSplitter,
}
logger = get_logger(__name__)
class SplitterFactory:
    @staticmethod
    def create() -> BaseSplitter:
        logger.info(f"Creating splitter strategy: {settings.text_splitter}")
        splitter_class = SPLITTER_REGISTRY.get(settings.text_splitter)
        if splitter_class is None:
            raise NotImplementedError(f"No strategy registered for {settings.text_splitter}")
        return splitter_class()
