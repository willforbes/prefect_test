from prefect import flow, get_run_logger

@flow(name="log-example-flow")
def logger_flow():
    logger = get_run_logger()
    logger.info("INFO level log message.")