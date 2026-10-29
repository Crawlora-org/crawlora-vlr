# VLR.gg clients for Crawlora

Official Crawlora client packages for the hosted VLR.gg API. Access 23 API endpoints covering Valorant matches, events, results, rankings, statistics, news, and forum data from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape VLR.gg locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by VLR.gg or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/vlr`](javascript/README.md)
- Python: [`crawlora-vlr`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-vlr`](go.mod)
- Ruby: [`crawlora-vlr`](ruby/README.md)
- Java: [`net.crawlora:crawlora-vlr:0.1.0`](java/README.md)
- PHP: [`crawlora/vlr`](php/README.md)
- Rust: [`crawlora-vlr`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 23 selected public VLR.gg API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
