from logging import getLogger

logger = getLogger(__name__)


def calc_add(a: int, b: int, **options) -> int:
    result_dir = options.get('result_dir', 'result')
    with open(f"{result_dir}/calc_add_result.txt", "w") as f:
        f.write(f"{a} + {b} = {a + b}")
    logger.info(f"result: {a + b}")
    return a + b
