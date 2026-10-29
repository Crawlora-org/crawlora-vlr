import os

from crawlora_vlr import VLRClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with VLRClient(api_key=api_key) as client:
    matches = client.matches()
    print('matches', matches)
    events = client.events()
    print('events', events)
