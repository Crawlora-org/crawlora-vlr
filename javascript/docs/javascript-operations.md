# Crawlora VLR.gg JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `23`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vlr | `vlr.event` | `vlr-event` | `GET /vlr/event` | `id` (query string required) | `ApiKeyAuth` | `VlrEventResponse` |  |
| vlr | `vlr.eventAgents` | `vlr-event-agents` | `GET /vlr/event-agents` | `id` (query string required) | `ApiKeyAuth` | `VlrEventAgentsResponse` |  |
| vlr | `vlr.eventMatches` | `vlr-event-matches` | `GET /vlr/event-matches` | `id` (query string required)<br>`series_id` (query string)<br>`group` (query "completed" \| "upcoming") | `ApiKeyAuth` | `VlrEventMatchesResponse` |  |
| vlr | `vlr.eventStats` | `vlr-event-stats` | `GET /vlr/event-stats` | `id` (query string required)<br>`side` (query "all" \| "t" \| "ct")<br>`role` (query string)<br>`agent` (query string)<br>`map` (query string)<br>`stage` (query string)<br>`min_rounds` (query number)<br>`sort` (query string)<br>`dir` (query "desc" \| "asc") | `ApiKeyAuth` | `VlrEventStatsResponse` |  |
| vlr | `vlr.events` | `vlr-events` | `GET /vlr/events` | `tier` (query "all" \| "vct" \| "vcl" \| "t3" \| "gc" \| "cg" \| "off")<br>`region` (query "all" \| "americas" \| "emea" \| "pacific" \| "china")<br>`page` (query number) | `ApiKeyAuth` | `VlrEventsResponse` |  |
| vlr | `vlr.forumCategories` | `vlr-forum-categories` | `GET /vlr/forum-categories` | none | `ApiKeyAuth` | `VlrForumCategoriesResponse` |  |
| vlr | `vlr.forumThreads` | `vlr-forum-threads` | `GET /vlr/forum-threads` | `category` (query "valorant-discussion" \| "off-topic" \| "site-feedback")<br>`page` (query number)<br>`sort` (query "hot" \| "new" \| "top") | `ApiKeyAuth` | `VlrForumThreadsResponse` |  |
| vlr | `vlr.match` | `vlr-match` | `GET /vlr/match` | `id` (query string required) | `ApiKeyAuth` | `VlrMatchResponse` |  |
| vlr | `vlr.matchEconomy` | `vlr-match-economy` | `GET /vlr/match-economy` | `id` (query string required) | `ApiKeyAuth` | `VlrMatchEconomyResponse` |  |
| vlr | `vlr.matchPerformance` | `vlr-match-performance` | `GET /vlr/match-performance` | `id` (query string required) | `ApiKeyAuth` | `VlrMatchPerformanceResponse` |  |
| vlr | `vlr.matchRounds` | `vlr-match-rounds` | `GET /vlr/match-rounds` | `id` (query string required) | `ApiKeyAuth` | `VlrMatchRoundsResponse` |  |
| vlr | `vlr.matches` | `vlr-matches` | `GET /vlr/matches` | `page` (query number) | `ApiKeyAuth` | `VlrMatchesResponse` |  |
| vlr | `vlr.news` | `vlr-news` | `GET /vlr/news` | `page` (query number) | `ApiKeyAuth` | `VlrNewsResponse` |  |
| vlr | `vlr.newsArticle` | `vlr-news-article` | `GET /vlr/news-article` | `id` (query string required) | `ApiKeyAuth` | `VlrNewsArticleResponse` |  |
| vlr | `vlr.player` | `vlr-player` | `GET /vlr/player` | `id` (query string required)<br>`timespan` (query "all" \| "30d" \| "60d" \| "90d") | `ApiKeyAuth` | `VlrPlayerResponse` |  |
| vlr | `vlr.playerMatches` | `vlr-player-matches` | `GET /vlr/player-matches` | `id` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `VlrPlayerMatchesResponse` |  |
| vlr | `vlr.rankings` | `vlr-rankings` | `GET /vlr/rankings` | `region` (query "north-america" \| "europe" \| "brazil" \| "asia-pacific" \| "korea" \| "china" \| "japan" \| "la-s" \| "la-n" \| "oceania" \| "mena" \| "gc" \| "collegiate")<br>`limit` (query number) | `ApiKeyAuth` | `VlrRankingsResponse` |  |
| vlr | `vlr.results` | `vlr-results` | `GET /vlr/results` | `page` (query number) | `ApiKeyAuth` | `VlrResultsResponse` |  |
| vlr | `vlr.search` | `vlr-search` | `GET /vlr/search` | `q` (query string required)<br>`type` (query "all" \| "teams" \| "events" \| "players") | `ApiKeyAuth` | `VlrSearchResponse` |  |
| vlr | `vlr.stats` | `vlr-stats` | `GET /vlr/stats` | `tier` (query string)<br>`region` (query string)<br>`timespan` (query "all" \| "30d" \| "60d" \| "90d" \| "2026" \| "2025" \| "2024" \| "2023" \| "2022" \| "2021" \| "2020")<br>`side` (query "all" \| "t" \| "ct")<br>`role` (query string)<br>`agent` (query string)<br>`map` (query string)<br>`min_rounds` (query number)<br>`from` (query string)<br>`to` (query string)<br>`min_rating` (query 0 \| 1300 \| 1400 \| 1500 \| 1550 \| 1650 \| 1750 \| 1850)<br>`sort` (query "rating" \| "maps" \| "rnd" \| "acs" \| "kd" \| "kast" \| "adr" \| "kpr" \| "apr" \| "fkfd" \| "fkpr" \| "fdpr" \| "hsp" \| "clp" \| "cl" \| "kmax" \| "k" \| "d" \| "a" \| "fk" \| "fd")<br>`dir` (query "asc" \| "desc")<br>`page` (query number) | `ApiKeyAuth` | `VlrStatsResponse` |  |
| vlr | `vlr.team` | `vlr-team` | `GET /vlr/team` | `id` (query string required) | `ApiKeyAuth` | `VlrTeamResponse` |  |
| vlr | `vlr.teamMaps` | `vlr-team-maps` | `GET /vlr/team-maps` | `id` (query string required) | `ApiKeyAuth` | `VlrTeamMapsResponse` |  |
| vlr | `vlr.teamMatches` | `vlr-team-matches` | `GET /vlr/team-matches` | `id` (query string required)<br>`page` (query number)<br>`group` (query "completed" \| "upcoming") | `ApiKeyAuth` | `VlrTeamMatchesResponse` |  |
