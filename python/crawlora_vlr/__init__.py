"""Typed VLR.gg client for the Crawlora hosted API."""

from .platform import VLRClient, AsyncVLRClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = VLRClient
AsyncClient = AsyncVLRClient
__version__ = '0.2.0'
DISPLAY_NAME = 'VLR.gg'
PLATFORM = 'vlr'
CONTRACT_REVISION = 'sha256:179a192268cbea90f4a433fae9fe047636b968ea7c92632fd296c8931519f7b5'

__all__ = [
    "VLRClient", "AsyncVLRClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
