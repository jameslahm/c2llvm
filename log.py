import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.addHandler(console)