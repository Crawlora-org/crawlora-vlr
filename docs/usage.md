# VLR.gg API endpoint reference and client usage

This reference lists all 23 public VLR.gg API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/vlr`, `crawlora-vlr`, and `crawlora-vlr` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape VLR.gg locally; Crawlora is independent from and not endorsed by VLR.gg or its owners.

The package tracks the public API contract revision `sha256:370561612f103fbd9de6f1c5064c916796727ec38ffb4b5d041419ac0b175e30` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `vlr`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `event` | `event` | `vlr.event` | `GET /vlr/event` | `id` (query, required) | VLR.gg Valorant event detail and participating teams |
| `eventAgents` | `event_agents` | `vlr.event_agents` | `GET /vlr/event-agents` | `id` (query, required) | VLR.gg Valorant event agent pick rates by map |
| `eventMatches` | `event_matches` | `vlr.event_matches` | `GET /vlr/event-matches` | `id` (query, required), `series_id` (query, optional), `group` (query, optional; values: `completed`, `upcoming`) | VLR.gg Valorant event match list |
| `events` | `events` | `vlr.events` | `GET /vlr/events` | `tier` (query, optional; values: `all`, `vct`, `vcl`, `t3`, `gc`, `cg`, `off`), `region` (query, optional; values: `all`, `americas`, `emea`, `pacific`, `china`), `page` (query, optional) | VLR.gg Valorant events |
| `eventStats` | `event_stats` | `vlr.event_stats` | `GET /vlr/event-stats` | `id` (query, required), `side` (query, optional; values: `all`, `t`, `ct`), `role` (query, optional), `agent` (query, optional), `map` (query, optional), `stage` (query, optional), `min_rounds` (query, optional), `sort` (query, optional), `dir` (query, optional; values: `desc`, `asc`) | VLR.gg Valorant event player statistics |
| `forumCategories` | `forum_categories` | `vlr.forum_categories` | `GET /vlr/forum-categories` | — | VLR.gg forum categories |
| `forumThreads` | `forum_threads` | `vlr.forum_threads` | `GET /vlr/forum-threads` | `category` (query, optional; values: `valorant-discussion`, `off-topic`, `site-feedback`), `page` (query, optional), `sort` (query, optional; values: `hot`, `new`, `top`) | VLR.gg forum thread list |
| `match` | `match` | `vlr.match_` | `GET /vlr/match` | `id` (query, required) | VLR.gg Valorant match detail and player statistics |
| `matchEconomy` | `match_economy` | `vlr.match_economy` | `GET /vlr/match-economy` | `id` (query, required) | VLR.gg Valorant match economy |
| `matches` | `matches` | `vlr.matches` | `GET /vlr/matches` | `page` (query, optional) | VLR.gg upcoming and live Valorant matches |
| `matchPerformance` | `match_performance` | `vlr.match_performance` | `GET /vlr/match-performance` | `id` (query, required) | VLR.gg Valorant match performance |
| `matchRounds` | `match_rounds` | `vlr.match_rounds` | `GET /vlr/match-rounds` | `id` (query, required) | VLR.gg Valorant match round-by-round log |
| `news` | `news` | `vlr.news` | `GET /vlr/news` | `page` (query, optional) | VLR.gg Valorant esports news |
| `newsArticle` | `news_article` | `vlr.news_article` | `GET /vlr/news-article` | `id` (query, required) | VLR.gg news article |
| `player` | `player` | `vlr.player` | `GET /vlr/player` | `id` (query, required), `timespan` (query, optional; values: `all`, `30d`, `60d`, `90d`) | VLR.gg Valorant player profile and agent statistics |
| `playerMatches` | `player_matches` | `vlr.player_matches` | `GET /vlr/player-matches` | `id` (query, required), `page` (query, optional) | VLR.gg Valorant player match history |
| `rankings` | `rankings` | `vlr.rankings` | `GET /vlr/rankings` | `region` (query, optional; values: `north-america`, `europe`, `brazil`, `asia-pacific`, `korea`, `china`, `japan`, `la-s`, `la-n`, `oceania`, `mena`, `gc`, `collegiate`), `limit` (query, optional) | VLR.gg Valorant team rankings by region |
| `results` | `results` | `vlr.results` | `GET /vlr/results` | `page` (query, optional) | VLR.gg completed Valorant match results |
| `search` | `search` | `vlr.search` | `GET /vlr/search` | `q` (query, required), `type` (query, optional; values: `all`, `teams`, `events`, `players`) | VLR.gg search for teams, events and players |
| `stats` | `stats` | `vlr.stats` | `GET /vlr/stats` | `tier` (query, optional), `region` (query, optional), `timespan` (query, optional; values: `all`, `30d`, `60d`, `90d`, `2026`, `2025`, `2024`, `2023`, `2022`, `2021`, `2020`), `side` (query, optional; values: `all`, `t`, `ct`), `role` (query, optional), `agent` (query, optional), `map` (query, optional), `min_rounds` (query, optional), `from` (query, optional), `to` (query, optional), `min_rating` (query, optional; values: `0`, `1300`, `1400`, `1500`, `1550`, `1650`, `1750`, `1850`), `sort` (query, optional; values: `rating`, `maps`, `rnd`, `acs`, `kd`, `kast`, `adr`, `kpr`, `apr`, `fkfd`, `fkpr`, `fdpr`, `hsp`, `clp`, `cl`, `kmax`, `k`, `d`, `a`, `fk`, `fd`), `dir` (query, optional; values: `asc`, `desc`), `page` (query, optional) | VLR.gg Valorant player statistics with filters |
| `team` | `team` | `vlr.team` | `GET /vlr/team` | `id` (query, required) | VLR.gg Valorant team profile and roster |
| `teamMaps` | `team_maps` | `vlr.team_maps` | `GET /vlr/team-maps` | `id` (query, required) | VLR.gg Valorant team map win rates |
| `teamMatches` | `team_matches` | `vlr.team_matches` | `GET /vlr/team-matches` | `id` (query, required), `page` (query, optional), `group` (query, optional; values: `completed`, `upcoming`) | VLR.gg Valorant team match history |

## Client forms

- JavaScript: import `VLRClient` (also exported as `Client`) from `@crawlora-org/vlr`; use `new VLRClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `VLRClient` (also exported as `Client`) from `crawlora_vlr`; use `with VLRClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncVLRClient`, used with `async with` and `await`.
- Rust: add `crawlora-vlr` with Cargo; import `Client` and the generated operation parameter struct, then call `client.vlr.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-vlr/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
