from config.settings import settings
from core.logger import get_logger
from services.llm.factory import LLMFactory

logger = get_logger(__name__)
def test_settings():
    print("\n===== SETTINGS =====")
    print(settings.llm_provider)
    print(settings.llm_model)

def test_logger():
    print("\n===== LOGGER =====")
    logger.info("Logger is working.")

def test_factory():
    print("\n===== FACTORY =====")
    try:
        llm = LLMFactory.create()
    except NotImplementedError as e:
        print(e)

if __name__ == "__main__":
    test_settings()
    test_logger()
    test_factory()