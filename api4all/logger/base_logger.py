from typing import Optional
import logging
import textwrap
import uuid
from ..utils.models import TextResponse

def setup_logger():
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    logger.propagate = False

    handler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter(f'\n\nRequest ID - {uuid.uuid4()}\n\tcreate at: %(asctime)s\n\t%(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def log_response(logger, result: str, response: Optional[TextResponse] = None):
    if result == "SUCCESS" and response is not None:
        indented_content = textwrap.indent(response.content, '\t\t')

        execution_time = round(response.execution_time, 3) if response.execution_time else "Execution time not provided by the provider"
        cost = formatted_cost(response.cost) if response.cost is not None else "Cost cannot be calculated"
        if not response.input_tokens: response.input_tokens = "Input tokens not provided by the provider"
        if not response.output_tokens: response.output_tokens = "Output tokens not provided by the provider"

        logger.info(f'{result}\n\tResponse:\n{indented_content}\n\tCost: ${cost}\n\tProvider: {response.provider}\n\tExecution-time: {execution_time}\n\tActual-time: {response.actual_time}\n\tInput-token: {response.input_tokens}\n\tOutput-token: {response.output_tokens}\n\n')
    else:
        logger.error(f'{result}\n\t')

def formatted_cost(cost: float) -> str:
    formatted_num = "{:.10f}".format(cost).rstrip('0')
    if formatted_num[-1] == '.':
        formatted_num = formatted_num[:-1]
    return formatted_num