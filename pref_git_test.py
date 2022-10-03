from prefect import flow, get_run_logger
import os

@flow(name="log-example-flow")
def logger_flow():
    logger = get_run_logger()
    logger.info("INFO level log message.")
    logger.info(os.path.realpath(__file__))
    logger.info('Another Log')