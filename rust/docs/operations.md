# Crawlora VLR.gg Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `23`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vlr | `vlr.event` | `vlr-event` | `GET /vlr/event` | `id` (query String required) | `ApiKeyAuth` | `VlrEventResponse` |  |
| vlr | `vlr.event_agents` | `vlr-event-agents` | `GET /vlr/event-agents` | `id` (query String required) | `ApiKeyAuth` | `VlrEventAgentsResponse` |  |
| vlr | `vlr.event_matches` | `vlr-event-matches` | `GET /vlr/event-matches` | `id` (query String required)<br>`series_id` (query String)<br>`group` (query String enum{completed, upcoming}) | `ApiKeyAuth` | `VlrEventMatchesResponse` |  |
| vlr | `vlr.event_stats` | `vlr-event-stats` | `GET /vlr/event-stats` | `id` (query String required)<br>`side` (query String enum{all, t, ct})<br>`role` (query String)<br>`agent` (query String)<br>`map` (query String)<br>`stage` (query String)<br>`min_rounds` (query i64)<br>`sort` (query String)<br>`dir` (query String enum{desc, asc}) | `ApiKeyAuth` | `VlrEventStatsResponse` |  |
| vlr | `vlr.events` | `vlr-events` | `GET /vlr/events` | `tier` (query String enum{all, vct, vcl, t3, gc, cg, off})<br>`region` (query String enum{all, americas, emea, pacific, china})<br>`page` (query i64) | `ApiKeyAuth` | `VlrEventsResponse` |  |
| vlr | `vlr.forum_categories` | `vlr-forum-categories` | `GET /vlr/forum-categories` | none | `ApiKeyAuth` | `VlrForumCategoriesResponse` |  |
| vlr | `vlr.forum_threads` | `vlr-forum-threads` | `GET /vlr/forum-threads` | `category` (query String enum{valorant-discussion, off-topic, site-feedback})<br>`page` (query i64)<br>`sort` (query String enum{hot, new, top}) | `ApiKeyAuth` | `VlrForumThreadsResponse` |  |
| vlr | `vlr.match_` | `vlr-match` | `GET /vlr/match` | `id` (query String required) | `ApiKeyAuth` | `VlrMatchResponse` |  |
| vlr | `vlr.match_economy` | `vlr-match-economy` | `GET /vlr/match-economy` | `id` (query String required) | `ApiKeyAuth` | `VlrMatchEconomyResponse` |  |
| vlr | `vlr.match_performance` | `vlr-match-performance` | `GET /vlr/match-performance` | `id` (query String required) | `ApiKeyAuth` | `VlrMatchPerformanceResponse` |  |
| vlr | `vlr.match_rounds` | `vlr-match-rounds` | `GET /vlr/match-rounds` | `id` (query String required) | `ApiKeyAuth` | `VlrMatchRoundsResponse` |  |
| vlr | `vlr.matches` | `vlr-matches` | `GET /vlr/matches` | `page` (query i64) | `ApiKeyAuth` | `VlrMatchesResponse` |  |
| vlr | `vlr.news` | `vlr-news` | `GET /vlr/news` | `page` (query i64) | `ApiKeyAuth` | `VlrNewsResponse` |  |
| vlr | `vlr.news_article` | `vlr-news-article` | `GET /vlr/news-article` | `id` (query String required) | `ApiKeyAuth` | `VlrNewsArticleResponse` |  |
| vlr | `vlr.player` | `vlr-player` | `GET /vlr/player` | `id` (query String required)<br>`timespan` (query String enum{all, 30d, 60d, 90d}) | `ApiKeyAuth` | `VlrPlayerResponse` |  |
| vlr | `vlr.player_matches` | `vlr-player-matches` | `GET /vlr/player-matches` | `id` (query String required)<br>`page` (query i64) | `ApiKeyAuth` | `VlrPlayerMatchesResponse` |  |
| vlr | `vlr.rankings` | `vlr-rankings` | `GET /vlr/rankings` | `region` (query String enum{north-america, europe, brazil, asia-pacific, korea, china, japan, la-s, la-n, oceania, mena, gc, collegiate})<br>`limit` (query i64) | `ApiKeyAuth` | `VlrRankingsResponse` |  |
| vlr | `vlr.results` | `vlr-results` | `GET /vlr/results` | `page` (query i64) | `ApiKeyAuth` | `VlrResultsResponse` |  |
| vlr | `vlr.search` | `vlr-search` | `GET /vlr/search` | `q` (query String required)<br>`type` (query String enum{all, teams, events, players}) | `ApiKeyAuth` | `VlrSearchResponse` |  |
| vlr | `vlr.stats` | `vlr-stats` | `GET /vlr/stats` | `tier` (query String)<br>`region` (query String)<br>`timespan` (query String enum{all, 30d, 60d, 90d, 2026, 2025, 2024, 2023, 2022, 2021, 2020})<br>`side` (query String enum{all, t, ct})<br>`role` (query String)<br>`agent` (query String)<br>`map` (query String)<br>`min_rounds` (query i64)<br>`from` (query String)<br>`to` (query String)<br>`min_rating` (query String enum{0, 1300, 1400, 1500, 1550, 1650, 1750, 1850})<br>`sort` (query String enum{rating, maps, rnd, acs, kd, kast, adr, kpr, apr, fkfd, fkpr, fdpr, hsp, clp, cl, kmax, k, d, a, fk, fd})<br>`dir` (query String enum{asc, desc})<br>`page` (query i64) | `ApiKeyAuth` | `VlrStatsResponse` |  |
| vlr | `vlr.team` | `vlr-team` | `GET /vlr/team` | `id` (query String required) | `ApiKeyAuth` | `VlrTeamResponse` |  |
| vlr | `vlr.team_maps` | `vlr-team-maps` | `GET /vlr/team-maps` | `id` (query String required) | `ApiKeyAuth` | `VlrTeamMapsResponse` |  |
| vlr | `vlr.team_matches` | `vlr-team-matches` | `GET /vlr/team-matches` | `id` (query String required)<br>`page` (query i64)<br>`group` (query String enum{completed, upcoming}) | `ApiKeyAuth` | `VlrTeamMatchesResponse` |  |
