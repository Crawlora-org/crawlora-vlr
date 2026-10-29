# Crawlora VLR.gg API client for Ruby (`crawlora-vlr`)

This Ruby gem calls Crawlora's hosted VLR.gg API at `https://api.crawlora.net/api/v1`. It exposes 23 endpoints covering Valorant matches, events, results, rankings, statistics, news, and forum data; it does not call or scrape VLR.gg directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-vlr"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/vlr"

client = Crawlora::Vlr::Client.new
result = client.request("vlr-search", JSON.parse("{\"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 23 API operations.

```ruby
client = Crawlora::Vlr::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported VLR.gg API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-vlr/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-vlr) for account setup, the API operation reference, and release history.
