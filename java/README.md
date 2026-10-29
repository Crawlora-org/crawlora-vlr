# Crawlora VLR.gg API client for Java

The official Java client for Crawlora's hosted VLR.gg API. It exposes 23 endpoints covering Valorant matches, events, results, rankings, statistics, news, and forum data. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-vlr</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-java-console) to get an API key.

```java
import net.crawlora.vlr.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.matches(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported VLR.gg API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-vlr/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-vlr)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-java-api-docs)
