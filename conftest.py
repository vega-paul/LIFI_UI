import pytest
import logging

logger = logging.getLogger(__name__)

pytest_plugins = ["pytest_playwright"]

# Custom handler that flushes immediately after each log
class ImmediateFlushHandler(logging.Handler):
    def __init__(self, handler):
        super().__init__()
        self.handler = handler
        self.setLevel(handler.level)
        self.setFormatter(handler.formatter)

    def emit(self, record):
        self.handler.emit(record)
        self.handler.flush()

# Configure logging to capture all module logs with immediate flushing
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s'))

file_handler = logging.FileHandler('pytest.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s'))

# Wrap handlers with immediate flushing
immediate_stream_handler = ImmediateFlushHandler(stream_handler)
immediate_file_handler = ImmediateFlushHandler(file_handler)

# Configure root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(immediate_stream_handler)
root_logger.addHandler(immediate_file_handler)



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    logger.info("Setting up browser context arguments")
    args = {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
        "ignore_https_errors": True,
        "bypass_csp": True,
    }
    logger.info(f"Browser context args configured: {args}")
    return args

@pytest.fixture(scope="session")
def browser_args(browser_args):
    return [
        *browser_args,
        "--disable-web-security",
        "--disable-features=VizDisplayCompositor",
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-background-timer-throttling",
        "--disable-backgrounding-occluded-windows",
        "--disable-renderer-backgrounding",
    ]

@pytest.fixture(scope="session")
def browser_launch_args(browser_launch_args, request):
    # Get browser name from pytest command line or default to chromium
    browser_name = getattr(request.config.option, 'browser', ['chromium'])[0]

    # Base launch args
    launch_args = {
        **browser_launch_args,
        "headless": True,  # Run headless in CI for better performance
        "args": [
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-software-rasterizer",
            "--disable-background-timer-throttling",
            "--disable-backgrounding-occluded-windows",
            "--disable-renderer-backgrounding",
        ]
    }

    # Browser-specific configurations
    if browser_name == "chrome":
        launch_args.update({
            "executable_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "channel": "chrome",
        })
    elif browser_name == "edge":
        launch_args.update({
            "executable_path": "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "channel": "msedge",
        })


    return launch_args
