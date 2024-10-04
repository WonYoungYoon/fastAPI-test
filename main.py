import logging
from elasticapm.handlers.logging import Formatter
from loguru import logger
from fastapi import FastAPI
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

apm = make_apm_client({
	'SERVICE_NAME': 'sec-test',
    'SERVER_URL': 'http://wny.iptime.org:48200',
})

app = FastAPI()
app.add_middleware(ElasticAPM, client=apm)

sh = logging.StremHandler()
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh.setFormatter(formatter)

logger.add(sh, format="{message}")

@app.get("/")
def printHello():
    logger.info("get hello message")
    return "Hello World"

@app.get("/test")
@elasticapm.capture_span()
def printTest():
    logger.info("info test")
    print("info")
    logger.warning("warning test")
    print("warning")
    logger.error("error test")
    print("error")
    return "test"
    
    
    
    