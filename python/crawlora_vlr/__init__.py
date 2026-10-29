"""Typed VLR.gg client for the Crawlora hosted API."""

from .platform import VLRClient, AsyncVLRClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = VLRClient
AsyncClient = AsyncVLRClient
__version__ = '0.1.0'
DISPLAY_NAME = 'VLR.gg'
PLATFORM = 'vlr'
CONTRACT_REVISION = 'sha256:370561612f103fbd9de6f1c5064c916796727ec38ffb4b5d041419ac0b175e30'

__all__ = [
    "VLRClient", "AsyncVLRClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
