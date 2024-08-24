from logging import getLogger

logger = getLogger(__name__)


def calc_add(a: int, b: int, **options) -> int:
    result_dir = options.get('result_dir', 'result')
    logger.info(f"result_dir: {result_dir}")
    logger.info(f"result: {a + b}")
    return a + b
