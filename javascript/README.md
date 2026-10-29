# @crawlora-org/vlr — VLR.gg API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted VLR.gg API.
It exposes 23 API endpoints for Valorant matches, events, results, rankings, statistics, news, and forum data through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-javascript-homepage). It does not run a browser or scrape VLR.gg locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by VLR.gg or its owners.

## Install

```sh
npm install @crawlora-org/vlr
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { VLRClient } from "@crawlora-org/vlr";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new VLRClient({ apiKey });
const result1 = await client.matches({});
console.log(result1);
const result2 = await client.events({});
console.log(result2);
```

The client also exports `Client` as an alias for `VLRClient`. Operation
methods are available directly in camelCase and through the `vlr`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-vlr/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-vlr/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported VLR.gg API endpoints

This package exposes each route below as a direct method and through the `vlr` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-vlr/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
