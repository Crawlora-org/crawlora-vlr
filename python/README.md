# crawlora-vlr — VLR.gg API client for Python

Python client for Crawlora's hosted VLR.gg API. It exposes 23 API endpoints covering Valorant matches, events, results, rankings, statistics, news, and forum data. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-python-homepage); the package does not run a browser or scrape
VLR.gg locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
VLR.gg or its owners.

## Install

```sh
python -m pip install crawlora-vlr
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_vlr import VLRClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with VLRClient(api_key=api_key) as client:
    result_1 = client.matches()
    print(result_1)
    result_2 = client.events()
    print(result_2)
```

The package also exports `Client` as an alias for `VLRClient`. Operation
methods are available directly in snake_case and through the `vlr`
group. The async package client is `AsyncVLRClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-vlr/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-vlr/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_vlr import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.matches()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-vlr/blob/main/examples/python.py) for a complete usage example.

## Supported VLR.gg API endpoints

This package exposes every route below through direct snake_case methods and the `vlr` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-vlr/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/vlr/event` | `vlr-event` | VLR.gg Valorant event detail and participating teams |
| `GET` | `/vlr/event-agents` | `vlr-event-agents` | VLR.gg Valorant event agent pick rates by map |
| `GET` | `/vlr/event-matches` | `vlr-event-matches` | VLR.gg Valorant event match list |
| `GET` | `/vlr/event-stats` | `vlr-event-stats` | VLR.gg Valorant event player statistics |
| `GET` | `/vlr/events` | `vlr-events` | VLR.gg Valorant events |
| `GET` | `/vlr/forum-categories` | `vlr-forum-categories` | VLR.gg forum categories |
| `GET` | `/vlr/forum-threads` | `vlr-forum-threads` | VLR.gg forum thread list |
| `GET` | `/vlr/match` | `vlr-match` | VLR.gg Valorant match detail and player statistics |
| `GET` | `/vlr/match-economy` | `vlr-match-economy` | VLR.gg Valorant match economy |
| `GET` | `/vlr/match-performance` | `vlr-match-performance` | VLR.gg Valorant match performance |
| `GET` | `/vlr/match-rounds` | `vlr-match-rounds` | VLR.gg Valorant match round-by-round log |
| `GET` | `/vlr/matches` | `vlr-matches` | VLR.gg upcoming and live Valorant matches |
| `GET` | `/vlr/news` | `vlr-news` | VLR.gg Valorant esports news |
| `GET` | `/vlr/news-article` | `vlr-news-article` | VLR.gg news article |
| `GET` | `/vlr/player` | `vlr-player` | VLR.gg Valorant player profile and agent statistics |
| `GET` | `/vlr/player-matches` | `vlr-player-matches` | VLR.gg Valorant player match history |
| `GET` | `/vlr/rankings` | `vlr-rankings` | VLR.gg Valorant team rankings by region |
| `GET` | `/vlr/results` | `vlr-results` | VLR.gg completed Valorant match results |
| `GET` | `/vlr/search` | `vlr-search` | VLR.gg search for teams, events and players |
| `GET` | `/vlr/stats` | `vlr-stats` | VLR.gg Valorant player statistics with filters |
| `GET` | `/vlr/team` | `vlr-team` | VLR.gg Valorant team profile and roster |
| `GET` | `/vlr/team-maps` | `vlr-team-maps` | VLR.gg Valorant team map win rates |
| `GET` | `/vlr/team-matches` | `vlr-team-matches` | VLR.gg Valorant team match history |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
