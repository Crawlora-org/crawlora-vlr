from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelVlrHistoryResponse = TypedDict('ModelVlrHistoryResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'group': NotRequired[Literal['completed', 'upcoming']],
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'matches': NotRequired[list[ModelVlrTeamMatch]],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrTeamMatch = TypedDict('ModelVlrTeamMatch', {
    'date': NotRequired[str],
    'eta': NotRequired[str],
    'event': NotRequired[str],
    'id': NotRequired[str],
    'opponent': NotRequired[str],
    'result': NotRequired[Literal['win', 'loss', 'upcoming']],
    'score': NotRequired[str],
    'stage': NotRequired[str],
    'team': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrTeamMapsResponse = TypedDict('ModelVlrTeamMapsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'maps': NotRequired[list[ModelVlrTeamMapRow]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

ModelVlrTeamMapRow = TypedDict('ModelVlrTeamMapRow', {
    'attack': NotRequired[ModelVlrMapSide],
    'defense': NotRequired[ModelVlrMapSide],
    'losses': NotRequired[int],
    'map': NotRequired[str],
    'played': NotRequired[int],
    'win_percent': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelVlrMapSide = TypedDict('ModelVlrMapSide', {
    'first_rounds': NotRequired[int],
    'round_win_percent': NotRequired[float],
    'rounds_lost': NotRequired[int],
    'rounds_won': NotRequired[int],
}, total=False)

ModelVlrTeamDetail = TypedDict('ModelVlrTeamDetail', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'links': NotRequired[list[str]],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'news': NotRequired[list[ModelVlrNewsItem]],
    'recent_matches': NotRequired[list[ModelVlrTeamMatch]],
    'roster': NotRequired[list[ModelVlrRosterMember]],
    'source_url': NotRequired[str],
    'tag': NotRequired[str],
}, total=False)

ModelVlrRosterMember = TypedDict('ModelVlrRosterMember', {
    'alias': NotRequired[str],
    'country_code': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'real_name': NotRequired[str],
    'role': NotRequired[Literal['player', 'captain', 'coach', 'manager', 'analyst', 'staff']],
}, total=False)

ModelVlrNewsItem = TypedDict('ModelVlrNewsItem', {
    'author': NotRequired[str],
    'country_code': NotRequired[str],
    'date': NotRequired[str],
    'description': NotRequired[str],
    'id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrStatsResponse = TypedDict('ModelVlrStatsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'players': NotRequired[list[ModelVlrStatsRow]],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrStatsRow = TypedDict('ModelVlrStatsRow', {
    'acs': NotRequired[float],
    'adr': NotRequired[float],
    'agent_usage': NotRequired[list[str]],
    'agents': NotRequired[list[str]],
    'assists': NotRequired[int],
    'assists_per_round': NotRequired[float],
    'clutch_percent': NotRequired[float],
    'clutches_total': NotRequired[int],
    'clutches_won': NotRequired[int],
    'deaths': NotRequired[int],
    'first_death_percent': NotRequired[float],
    'first_deaths': NotRequired[int],
    'first_kill_percent': NotRequired[float],
    'first_kills': NotRequired[int],
    'fk_fd_ratio': NotRequired[float],
    'headshot_percent': NotRequired[float],
    'kast_percent': NotRequired[float],
    'kd': NotRequired[float],
    'kills': NotRequired[int],
    'kills_per_round': NotRequired[float],
    'maps': NotRequired[int],
    'max_kills': NotRequired[int],
    'player': NotRequired[ModelVlrPlayerRef],
    'rating': NotRequired[float],
    'rounds': NotRequired[int],
}, total=False)

ModelVlrPlayerRef = TypedDict('ModelVlrPlayerRef', {
    'country_code': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'team': NotRequired[str],
}, total=False)

ModelVlrSearchResponse = TypedDict('ModelVlrSearchResponse', {
    'count': NotRequired[int],
    'counts': NotRequired[ModelVlrSearchCounts],
    'fetched_at': NotRequired[str],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelVlrSearchResult]],
    'source_url': NotRequired[str],
    'type': NotRequired[Literal['all', 'teams', 'events', 'players']],
}, total=False)

ModelVlrSearchResult = TypedDict('ModelVlrSearchResult', {
    'date_range': NotRequired[str],
    'description': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'inactive': NotRequired[bool],
    'kind': NotRequired[Literal['team', 'event', 'player']],
    'name': NotRequired[str],
    'prize_pool': NotRequired[str],
    'successor': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrSearchCounts = TypedDict('ModelVlrSearchCounts', {
    'events': NotRequired[int],
    'players': NotRequired[int],
    'teams': NotRequired[int],
}, total=False)

ModelVlrMatchListResponse = TypedDict('ModelVlrMatchListResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'matches': NotRequired[list[ModelVlrMatchSummary]],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrMatchSummary = TypedDict('ModelVlrMatchSummary', {
    'date': NotRequired[str],
    'eta': NotRequired[str],
    'event': NotRequired[str],
    'has_stats': NotRequired[bool],
    'has_vods': NotRequired[bool],
    'id': NotRequired[str],
    'note': NotRequired[str],
    'series': NotRequired[str],
    'status': NotRequired[Literal['upcoming', 'live', 'completed']],
    'teams': NotRequired[list[ModelVlrMatchTeam]],
    'time_label': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrMatchTeam = TypedDict('ModelVlrMatchTeam', {
    'country_code': NotRequired[str],
    'name': NotRequired[str],
    'score': NotRequired[int],
    'winner': NotRequired[bool],
}, total=False)

ModelVlrRankingsResponse = TypedDict('ModelVlrRankingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'region': NotRequired[str],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelVlrRankingRow]],
    'total': NotRequired[int],
}, total=False)

ModelVlrRankingRow = TypedDict('ModelVlrRankingRow', {
    'country': NotRequired[str],
    'earnings': NotRequired[str],
    'last_match_id': NotRequired[str],
    'rank': NotRequired[int],
    'rating': NotRequired[float],
    'record': NotRequired[str],
    'streak': NotRequired[str],
    'team': NotRequired[ModelVlrTeamRef],
}, total=False)

ModelVlrTeamRef = TypedDict('ModelVlrTeamRef', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'tag': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrPlayerDetail = TypedDict('ModelVlrPlayerDetail', {
    'agent_stats': NotRequired[list[ModelVlrAgentUsage]],
    'alias': NotRequired[str],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'current_teams': NotRequired[list[ModelVlrPlayerTeam]],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'links': NotRequired[list[str]],
    'past_teams': NotRequired[list[ModelVlrPlayerTeam]],
    'real_name': NotRequired[str],
    'recent_matches': NotRequired[list[ModelVlrTeamMatch]],
    'source_url': NotRequired[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d']],
}, total=False)

ModelVlrPlayerTeam = TypedDict('ModelVlrPlayerTeam', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'period': NotRequired[str],
    'tag': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrAgentUsage = TypedDict('ModelVlrAgentUsage', {
    'acs': NotRequired[float],
    'adr': NotRequired[float],
    'agent': NotRequired[str],
    'assists': NotRequired[int],
    'assists_per_round': NotRequired[float],
    'deaths': NotRequired[int],
    'first_deaths': NotRequired[int],
    'first_kills': NotRequired[int],
    'first_kills_per_round': NotRequired[float],
    'kast_percent': NotRequired[float],
    'kd': NotRequired[float],
    'kills': NotRequired[int],
    'kills_per_round': NotRequired[float],
    'rating': NotRequired[float],
    'rounds': NotRequired[int],
    'use': NotRequired[str],
}, total=False)

ModelVlrArticleDetail = TypedDict('ModelVlrArticleDetail', {
    'author': NotRequired[str],
    'external_links': NotRequired[list[str]],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'images': NotRequired[list[str]],
    'paragraphs': NotRequired[list[str]],
    'published_at': NotRequired[str],
    'references': NotRequired[list[ModelVlrArticleRef]],
    'source_url': NotRequired[str],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrArticleRef = TypedDict('ModelVlrArticleRef', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'type': NotRequired[Literal['team', 'player', 'event']],
    'url': NotRequired[str],
}, total=False)

ModelVlrNewsResponse = TypedDict('ModelVlrNewsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[ModelVlrNewsItem]],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrMatchRounds = TypedDict('ModelVlrMatchRounds', {
    'available': NotRequired[bool],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'maps': NotRequired[list[ModelVlrRoundsBlock]],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrRoundsBlock = TypedDict('ModelVlrRoundsBlock', {
    'game_id': NotRequired[str],
    'map': NotRequired[str],
    'map_number': NotRequired[int],
    'rounds': NotRequired[list[ModelVlrRoundLog]],
}, total=False)

ModelVlrRoundLog = TypedDict('ModelVlrRoundLog', {
    'attacking_team': NotRequired[str],
    'events': NotRequired[list[ModelVlrRoundEvent]],
    'loadouts': NotRequired[list[ModelVlrRoundLoadout]],
    'round': NotRequired[int],
    'score_after': NotRequired[ModelVlrRoundScore],
    'spike_detonated': NotRequired[bool],
    'winner_team': NotRequired[str],
}, total=False)

ModelVlrRoundScore = TypedDict('ModelVlrRoundScore', {
    'team1': NotRequired[int],
    'team2': NotRequired[int],
}, total=False)

ModelVlrRoundLoadout = TypedDict('ModelVlrRoundLoadout', {
    'agent': NotRequired[str],
    'armor': NotRequired[str],
    'credits_left': NotRequired[int],
    'player': NotRequired[str],
    'spent': NotRequired[int],
    'team': NotRequired[str],
    'weapon': NotRequired[str],
}, total=False)

ModelVlrRoundEvent = TypedDict('ModelVlrRoundEvent', {
    'player': NotRequired[str],
    'player_team': NotRequired[str],
    'time': NotRequired[str],
    'type': NotRequired[Literal['kill', 'plant', 'defuse']],
    'victim': NotRequired[str],
    'weapon': NotRequired[str],
}, total=False)

ModelVlrMatchPerformance = TypedDict('ModelVlrMatchPerformance', {
    'all_maps': NotRequired[ModelVlrPerformanceBlock],
    'available': NotRequired[bool],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'maps': NotRequired[list[ModelVlrPerformanceBlock]],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrPerformanceBlock = TypedDict('ModelVlrPerformanceBlock', {
    'advanced': NotRequired[list[ModelVlrAdvancedLine]],
    'game_id': NotRequired[str],
    'kill_matrices': NotRequired[list[ModelVlrKillMatrix]],
    'map': NotRequired[str],
    'map_number': NotRequired[int],
}, total=False)

ModelVlrKillMatrix = TypedDict('ModelVlrKillMatrix', {
    'mode': NotRequired[Literal['overall', 'first_kills', 'op_kills']],
    'rows': NotRequired[list[ModelVlrMatrixRow]],
}, total=False)

ModelVlrMatrixRow = TypedDict('ModelVlrMatrixRow', {
    'player': NotRequired[ModelVlrMatrixPlayer],
    'vs': NotRequired[list[ModelVlrMatrixCell]],
}, total=False)

ModelVlrMatrixCell = TypedDict('ModelVlrMatrixCell', {
    'deaths': NotRequired[int],
    'diff': NotRequired[int],
    'kills': NotRequired[int],
    'opponent': NotRequired[ModelVlrMatrixPlayer],
}, total=False)

ModelVlrMatrixPlayer = TypedDict('ModelVlrMatrixPlayer', {
    'name': NotRequired[str],
    'team': NotRequired[str],
}, total=False)

ModelVlrAdvancedLine = TypedDict('ModelVlrAdvancedLine', {
    'agent': NotRequired[str],
    'clutches_1v1': NotRequired[int],
    'clutches_1v2': NotRequired[int],
    'clutches_1v3': NotRequired[int],
    'clutches_1v4': NotRequired[int],
    'clutches_1v5': NotRequired[int],
    'defuses': NotRequired[int],
    'econ_rating': NotRequired[int],
    'multikills_2k': NotRequired[int],
    'multikills_3k': NotRequired[int],
    'multikills_4k': NotRequired[int],
    'multikills_5k': NotRequired[int],
    'plants': NotRequired[int],
    'player': NotRequired[ModelVlrMatrixPlayer],
}, total=False)

ModelVlrMatchEconomy = TypedDict('ModelVlrMatchEconomy', {
    'all_maps': NotRequired[ModelVlrEconomyBlock],
    'available': NotRequired[bool],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'maps': NotRequired[list[ModelVlrEconomyBlock]],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrEconomyBlock = TypedDict('ModelVlrEconomyBlock', {
    'buy_buckets': NotRequired[list[ModelVlrBuyBucket]],
    'game_id': NotRequired[str],
    'map': NotRequired[str],
    'map_number': NotRequired[int],
    'rounds': NotRequired[list[ModelVlrEconomyRound]],
    'teams': NotRequired[list[ModelVlrTeamEconomy]],
}, total=False)

ModelVlrTeamEconomy = TypedDict('ModelVlrTeamEconomy', {
    'bonus_rounds': NotRequired[ModelVlrRatio],
    'pistol_conversion': NotRequired[ModelVlrRatio],
    'pistol_rounds': NotRequired[ModelVlrRatio],
    'team': NotRequired[str],
}, total=False)

ModelVlrRatio = TypedDict('ModelVlrRatio', {
    'played': NotRequired[int],
    'won': NotRequired[int],
}, total=False)

ModelVlrEconomyRound = TypedDict('ModelVlrEconomyRound', {
    'pistol': NotRequired[bool],
    'round': NotRequired[int],
    'team1_bank_k': NotRequired[float],
    'team1_buy': NotRequired[Literal['eco', 'half', 'full']],
    'team1_loadout_k': NotRequired[float],
    'team2_bank_k': NotRequired[float],
    'team2_buy': NotRequired[Literal['eco', 'half', 'full']],
    'team2_loadout_k': NotRequired[float],
    'winner_side': NotRequired[Literal['attack', 'defense']],
    'winner_team': NotRequired[str],
}, total=False)

ModelVlrBuyBucket = TypedDict('ModelVlrBuyBucket', {
    'buy': NotRequired[Literal['eco', 'half', 'full']],
    'label': NotRequired[str],
    'teams': NotRequired[list[ModelVlrBuyOutcome]],
}, total=False)

ModelVlrBuyOutcome = TypedDict('ModelVlrBuyOutcome', {
    'team': NotRequired[str],
    'vs_eco': NotRequired[ModelVlrRatio],
    'vs_full': NotRequired[ModelVlrRatio],
    'vs_half': NotRequired[ModelVlrRatio],
}, total=False)

ModelVlrMatchDetail = TypedDict('ModelVlrMatchDetail', {
    'all_maps_players': NotRequired[list[ModelVlrPlayerLine]],
    'event': NotRequired[ModelVlrEventRef],
    'fetched_at': NotRequired[str],
    'format': NotRequired[str],
    'head_to_head': NotRequired[ModelVlrHeadToHead],
    'id': NotRequired[str],
    'maps': NotRequired[list[ModelVlrMapResult]],
    'note': NotRequired[str],
    'past_matches': NotRequired[list[ModelVlrPastMatches]],
    'source_url': NotRequired[str],
    'start_time_utc': NotRequired[str],
    'status': NotRequired[str],
    'teams': NotRequired[list[ModelVlrTeamScore]],
    'url': NotRequired[str],
}, total=False)

ModelVlrTeamScore = TypedDict('ModelVlrTeamScore', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'score': NotRequired[int],
    'tag': NotRequired[str],
    'url': NotRequired[str],
    'winner': NotRequired[bool],
}, total=False)

ModelVlrPastMatches = TypedDict('ModelVlrPastMatches', {
    'matches': NotRequired[list[ModelVlrPastMatch]],
    'team': NotRequired[str],
}, total=False)

ModelVlrPastMatch = TypedDict('ModelVlrPastMatch', {
    'date': NotRequired[str],
    'id': NotRequired[str],
    'opponent': NotRequired[str],
    'result': NotRequired[Literal['win', 'loss']],
    'score': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrMapResult = TypedDict('ModelVlrMapResult', {
    'duration': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'number': NotRequired[int],
    'picked_by': NotRequired[str],
    'players': NotRequired[list[ModelVlrPlayerLine]],
    'teams': NotRequired[list[ModelVlrMapTeamResult]],
}, total=False)

ModelVlrMapTeamResult = TypedDict('ModelVlrMapTeamResult', {
    'name': NotRequired[str],
    'rounds': NotRequired[ModelVlrRoundSplit],
    'score': NotRequired[int],
}, total=False)

ModelVlrRoundSplit = TypedDict('ModelVlrRoundSplit', {
    'attack': NotRequired[int],
    'defend': NotRequired[int],
    'overtime': NotRequired[int],
}, total=False)

ModelVlrPlayerLine = TypedDict('ModelVlrPlayerLine', {
    'acs': NotRequired[int],
    'adr': NotRequired[float],
    'agents': NotRequired[list[str]],
    'assists': NotRequired[int],
    'country_code': NotRequired[str],
    'deaths': NotRequired[int],
    'first_deaths': NotRequired[int],
    'first_kills': NotRequired[int],
    'fk_diff': NotRequired[int],
    'headshot_percent': NotRequired[float],
    'id': NotRequired[str],
    'kast_percent': NotRequired[float],
    'kd_diff': NotRequired[int],
    'kills': NotRequired[int],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'team': NotRequired[str],
}, total=False)

ModelVlrHeadToHead = TypedDict('ModelVlrHeadToHead', {
    'matches': NotRequired[list[ModelVlrH2Hmatch]],
    'team1': NotRequired[str],
    'team2': NotRequired[str],
}, total=False)

ModelVlrH2Hmatch = TypedDict('ModelVlrH2Hmatch', {
    'date': NotRequired[str],
    'event': NotRequired[str],
    'id': NotRequired[str],
    'stage': NotRequired[str],
    'team1_score': NotRequired[int],
    'team2_score': NotRequired[int],
    'url': NotRequired[str],
    'winner': NotRequired[Literal['team1', 'team2']],
}, total=False)

ModelVlrEventRef = TypedDict('ModelVlrEventRef', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'series': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrForumThreadsResponse = TypedDict('ModelVlrForumThreadsResponse', {
    'category': NotRequired[str],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['hot', 'new', 'top']],
    'source_url': NotRequired[str],
    'threads': NotRequired[list[ModelVlrForumThread]],
}, total=False)

ModelVlrForumThread = TypedDict('ModelVlrForumThread', {
    'author': NotRequired[str],
    'category': NotRequired[str],
    'category_name': NotRequired[str],
    'frags': NotRequired[int],
    'id': NotRequired[str],
    'last_active': NotRequired[str],
    'last_poster': NotRequired[str],
    'pinned': NotRequired[bool],
    'posted': NotRequired[str],
    'replies': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelVlrForumCategoriesResponse = TypedDict('ModelVlrForumCategoriesResponse', {
    'categories': NotRequired[list[ModelVlrForumCategory]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrForumCategory = TypedDict('ModelVlrForumCategory', {
    'description': NotRequired[str],
    'group': NotRequired[str],
    'last_post_time': NotRequired[str],
    'last_poster': NotRequired[str],
    'last_thread_id': NotRequired[str],
    'name': NotRequired[str],
    'posts': NotRequired[int],
    'slug': NotRequired[Literal['valorant-discussion', 'off-topic', 'site-feedback']],
    'threads': NotRequired[int],
}, total=False)

ModelVlrEventsResponse = TypedDict('ModelVlrEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelVlrEventSummary]],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'region': NotRequired[str],
    'source_url': NotRequired[str],
    'tier': NotRequired[str],
}, total=False)

ModelVlrEventSummary = TypedDict('ModelVlrEventSummary', {
    'country_code': NotRequired[str],
    'dates': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'prize': NotRequired[str],
    'status': NotRequired[Literal['upcoming', 'ongoing', 'completed']],
    'url': NotRequired[str],
}, total=False)

ModelVlrEventStatsResponse = TypedDict('ModelVlrEventStatsResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[str],
    'fetched_at': NotRequired[str],
    'players': NotRequired[list[ModelVlrStatsRow]],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrEventMatchesResponse = TypedDict('ModelVlrEventMatchesResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[str],
    'fetched_at': NotRequired[str],
    'group': NotRequired[Literal['completed', 'upcoming']],
    'matches': NotRequired[list[ModelVlrMatchSummary]],
    'series_id': NotRequired[str],
    'source_url': NotRequired[str],
    'stages': NotRequired[list[ModelVlrEventStage]],
}, total=False)

ModelVlrEventStage = TypedDict('ModelVlrEventStage', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelVlrEventAgentsResponse = TypedDict('ModelVlrEventAgentsResponse', {
    'agents': NotRequired[list[str]],
    'compositions': NotRequired[list[ModelVlrMapCompositions]],
    'event_id': NotRequired[str],
    'fetched_at': NotRequired[str],
    'maps': NotRequired[list[ModelVlrMapAgentRow]],
    'overall': NotRequired[ModelVlrMapAgentRow],
    'source_url': NotRequired[str],
}, total=False)

ModelVlrMapAgentRow = TypedDict('ModelVlrMapAgentRow', {
    'attack_win_percent': NotRequired[float],
    'defense_win_percent': NotRequired[float],
    'games': NotRequired[int],
    'map': NotRequired[str],
    'pick_rates': NotRequired[list[ModelVlrAgentPick]],
}, total=False)

ModelVlrAgentPick = TypedDict('ModelVlrAgentPick', {
    'agent': NotRequired[str],
    'percent': NotRequired[float],
}, total=False)

ModelVlrMapCompositions = TypedDict('ModelVlrMapCompositions', {
    'map': NotRequired[str],
    'teams': NotRequired[list[ModelVlrTeamComposition]],
}, total=False)

ModelVlrTeamComposition = TypedDict('ModelVlrTeamComposition', {
    'agents_used': NotRequired[list[str]],
    'matches': NotRequired[list[ModelVlrCompositionMatch]],
    'team': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

ModelVlrCompositionMatch = TypedDict('ModelVlrCompositionMatch', {
    'agents': NotRequired[list[str]],
    'match_id': NotRequired[str],
    'opponent': NotRequired[str],
    'result': NotRequired[Literal['win', 'loss']],
}, total=False)

ModelVlrEventDetail = TypedDict('ModelVlrEventDetail', {
    'dates': NotRequired[str],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'location': NotRequired[str],
    'name': NotRequired[str],
    'prize': NotRequired[str],
    'series': NotRequired[str],
    'source_url': NotRequired[str],
    'subtitle': NotRequired[str],
    'teams': NotRequired[list[ModelVlrTeamRef]],
}, total=False)

VlrEventResponse = Any
VlrEventParams = TypedDict('VlrEventParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrEventAgentsResponse = Any
VlrEventAgentsParams = TypedDict('VlrEventAgentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrEventMatchesResponse = Any
VlrEventMatchesParams = TypedDict('VlrEventMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'series_id': NotRequired[str],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

VlrEventStatsResponse = Any
VlrEventStatsParams = TypedDict('VlrEventStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'stage': NotRequired[str],
    'min_rounds': NotRequired[int],
    'sort': NotRequired[str],
    'dir': NotRequired[Literal['desc', 'asc']],
}, total=False)

VlrEventsResponse = Any
VlrEventsParams = TypedDict('VlrEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tier': NotRequired[Literal['all', 'vct', 'vcl', 't3', 'gc', 'cg', 'off']],
    'region': NotRequired[Literal['all', 'americas', 'emea', 'pacific', 'china']],
    'page': NotRequired[int],
}, total=False)

VlrForumCategoriesResponse = Any
VlrForumCategoriesParams = TypedDict('VlrForumCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

VlrForumThreadsResponse = Any
VlrForumThreadsParams = TypedDict('VlrForumThreadsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['valorant-discussion', 'off-topic', 'site-feedback']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['hot', 'new', 'top']],
}, total=False)

VlrMatchResponse = Any
VlrMatchParams = TypedDict('VlrMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrMatchEconomyResponse = Any
VlrMatchEconomyParams = TypedDict('VlrMatchEconomyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrMatchPerformanceResponse = Any
VlrMatchPerformanceParams = TypedDict('VlrMatchPerformanceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrMatchRoundsResponse = Any
VlrMatchRoundsParams = TypedDict('VlrMatchRoundsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrMatchesResponse = Any
VlrMatchesParams = TypedDict('VlrMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
}, total=False)

VlrNewsResponse = Any
VlrNewsParams = TypedDict('VlrNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
}, total=False)

VlrNewsArticleResponse = Any
VlrNewsArticleParams = TypedDict('VlrNewsArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrPlayerResponse = Any
VlrPlayerParams = TypedDict('VlrPlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d']],
}, total=False)

VlrPlayerMatchesResponse = Any
VlrPlayerMatchesParams = TypedDict('VlrPlayerMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

VlrRankingsResponse = Any
VlrRankingsParams = TypedDict('VlrRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'region': NotRequired[Literal['north-america', 'europe', 'brazil', 'asia-pacific', 'korea', 'china', 'japan', 'la-s', 'la-n', 'oceania', 'mena', 'gc', 'collegiate']],
    'limit': NotRequired[int],
}, total=False)

VlrResultsResponse = Any
VlrResultsParams = TypedDict('VlrResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
}, total=False)

VlrSearchResponse = Any
VlrSearchParams = TypedDict('VlrSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'teams', 'events', 'players']],
}, total=False)

VlrStatsResponse = Any
VlrStatsParams = TypedDict('VlrStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tier': NotRequired[str],
    'region': NotRequired[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d', '2026', '2025', '2024', '2023', '2022', '2021', '2020']],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'min_rounds': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'min_rating': NotRequired[Literal['0', '1300', '1400', '1500', '1550', '1650', '1750', '1850']],
    'sort': NotRequired[Literal['rating', 'maps', 'rnd', 'acs', 'kd', 'kast', 'adr', 'kpr', 'apr', 'fkfd', 'fkpr', 'fdpr', 'hsp', 'clp', 'cl', 'kmax', 'k', 'd', 'a', 'fk', 'fd']],
    'dir': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
}, total=False)

VlrTeamResponse = Any
VlrTeamParams = TypedDict('VlrTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrTeamMapsResponse = Any
VlrTeamMapsParams = TypedDict('VlrTeamMapsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

VlrTeamMatchesResponse = Any
VlrTeamMatchesParams = TypedDict('VlrTeamMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

class VlrGroup:
    @overload
    def event(self, **params: Unpack[VlrEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[VlrEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[VlrEventDefaultParams]) -> VlrEventResponse: ...
    @overload
    def event_agents(self, **params: Unpack[VlrEventAgentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_agents(self, **params: Unpack[VlrEventAgentsTextResponseParams]) -> str: ...
    @overload
    def event_agents(self, **params: Unpack[VlrEventAgentsDefaultParams]) -> VlrEventAgentsResponse: ...
    @overload
    def event_matches(self, **params: Unpack[VlrEventMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def event_matches(self, **params: Unpack[VlrEventMatchesTextResponseParams]) -> str: ...
    @overload
    def event_matches(self, **params: Unpack[VlrEventMatchesDefaultParams]) -> VlrEventMatchesResponse: ...
    @overload
    def event_stats(self, **params: Unpack[VlrEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    def event_stats(self, **params: Unpack[VlrEventStatsTextResponseParams]) -> str: ...
    @overload
    def event_stats(self, **params: Unpack[VlrEventStatsDefaultParams]) -> VlrEventStatsResponse: ...
    @overload
    def events(self, **params: Unpack[VlrEventsStreamParams]) -> BinaryIO: ...
    @overload
    def events(self, **params: Unpack[VlrEventsTextResponseParams]) -> str: ...
    @overload
    def events(self, **params: Unpack[VlrEventsDefaultParams]) -> VlrEventsResponse: ...
    @overload
    def forum_categories(self, **params: Unpack[VlrForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def forum_categories(self, **params: Unpack[VlrForumCategoriesTextResponseParams]) -> str: ...
    @overload
    def forum_categories(self, **params: Unpack[VlrForumCategoriesDefaultParams]) -> VlrForumCategoriesResponse: ...
    @overload
    def forum_threads(self, **params: Unpack[VlrForumThreadsStreamParams]) -> BinaryIO: ...
    @overload
    def forum_threads(self, **params: Unpack[VlrForumThreadsTextResponseParams]) -> str: ...
    @overload
    def forum_threads(self, **params: Unpack[VlrForumThreadsDefaultParams]) -> VlrForumThreadsResponse: ...
    @overload
    def match(self, **params: Unpack[VlrMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[VlrMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[VlrMatchDefaultParams]) -> VlrMatchResponse: ...
    @overload
    def match_economy(self, **params: Unpack[VlrMatchEconomyStreamParams]) -> BinaryIO: ...
    @overload
    def match_economy(self, **params: Unpack[VlrMatchEconomyTextResponseParams]) -> str: ...
    @overload
    def match_economy(self, **params: Unpack[VlrMatchEconomyDefaultParams]) -> VlrMatchEconomyResponse: ...
    @overload
    def match_performance(self, **params: Unpack[VlrMatchPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    def match_performance(self, **params: Unpack[VlrMatchPerformanceTextResponseParams]) -> str: ...
    @overload
    def match_performance(self, **params: Unpack[VlrMatchPerformanceDefaultParams]) -> VlrMatchPerformanceResponse: ...
    @overload
    def match_rounds(self, **params: Unpack[VlrMatchRoundsStreamParams]) -> BinaryIO: ...
    @overload
    def match_rounds(self, **params: Unpack[VlrMatchRoundsTextResponseParams]) -> str: ...
    @overload
    def match_rounds(self, **params: Unpack[VlrMatchRoundsDefaultParams]) -> VlrMatchRoundsResponse: ...
    @overload
    def matches(self, **params: Unpack[VlrMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[VlrMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[VlrMatchesDefaultParams]) -> VlrMatchesResponse: ...
    @overload
    def news(self, **params: Unpack[VlrNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[VlrNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[VlrNewsDefaultParams]) -> VlrNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[VlrNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[VlrNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[VlrNewsArticleDefaultParams]) -> VlrNewsArticleResponse: ...
    @overload
    def player(self, **params: Unpack[VlrPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[VlrPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[VlrPlayerDefaultParams]) -> VlrPlayerResponse: ...
    @overload
    def player_matches(self, **params: Unpack[VlrPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[VlrPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[VlrPlayerMatchesDefaultParams]) -> VlrPlayerMatchesResponse: ...
    @overload
    def rankings(self, **params: Unpack[VlrRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[VlrRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[VlrRankingsDefaultParams]) -> VlrRankingsResponse: ...
    @overload
    def results(self, **params: Unpack[VlrResultsStreamParams]) -> BinaryIO: ...
    @overload
    def results(self, **params: Unpack[VlrResultsTextResponseParams]) -> str: ...
    @overload
    def results(self, **params: Unpack[VlrResultsDefaultParams]) -> VlrResultsResponse: ...
    @overload
    def search(self, **params: Unpack[VlrSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[VlrSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[VlrSearchDefaultParams]) -> VlrSearchResponse: ...
    @overload
    def stats(self, **params: Unpack[VlrStatsStreamParams]) -> BinaryIO: ...
    @overload
    def stats(self, **params: Unpack[VlrStatsTextResponseParams]) -> str: ...
    @overload
    def stats(self, **params: Unpack[VlrStatsDefaultParams]) -> VlrStatsResponse: ...
    @overload
    def team(self, **params: Unpack[VlrTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[VlrTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[VlrTeamDefaultParams]) -> VlrTeamResponse: ...
    @overload
    def team_maps(self, **params: Unpack[VlrTeamMapsStreamParams]) -> BinaryIO: ...
    @overload
    def team_maps(self, **params: Unpack[VlrTeamMapsTextResponseParams]) -> str: ...
    @overload
    def team_maps(self, **params: Unpack[VlrTeamMapsDefaultParams]) -> VlrTeamMapsResponse: ...
    @overload
    def team_matches(self, **params: Unpack[VlrTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_matches(self, **params: Unpack[VlrTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def team_matches(self, **params: Unpack[VlrTeamMatchesDefaultParams]) -> VlrTeamMatchesResponse: ...

OperationId = Literal[
    'vlr-event',
    'vlr-event-agents',
    'vlr-event-matches',
    'vlr-event-stats',
    'vlr-events',
    'vlr-forum-categories',
    'vlr-forum-threads',
    'vlr-match',
    'vlr-match-economy',
    'vlr-match-performance',
    'vlr-match-rounds',
    'vlr-matches',
    'vlr-news',
    'vlr-news-article',
    'vlr-player',
    'vlr-player-matches',
    'vlr-rankings',
    'vlr-results',
    'vlr-search',
    'vlr-stats',
    'vlr-team',
    'vlr-team-maps',
    'vlr-team-matches',
]

class CrawloraClient:
    vlr: VlrGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-event'],
        params: VlrEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-event-agents'],
        params: VlrEventAgentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventAgentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-event-matches'],
        params: VlrEventMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-event-stats'],
        params: VlrEventStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-events'],
        params: VlrEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-forum-categories'],
        params: VlrForumCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrForumCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-forum-threads'],
        params: VlrForumThreadsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrForumThreadsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-match'],
        params: VlrMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-match-economy'],
        params: VlrMatchEconomyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchEconomyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-match-performance'],
        params: VlrMatchPerformanceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchPerformanceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-match-rounds'],
        params: VlrMatchRoundsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchRoundsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-matches'],
        params: VlrMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-news'],
        params: VlrNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-news-article'],
        params: VlrNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrNewsArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-player'],
        params: VlrPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrPlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-player-matches'],
        params: VlrPlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrPlayerMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-rankings'],
        params: VlrRankingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-results'],
        params: VlrResultsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-search'],
        params: VlrSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-stats'],
        params: VlrStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-team'],
        params: VlrTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-team-maps'],
        params: VlrTeamMapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrTeamMapsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['vlr-team-matches'],
        params: VlrTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrTeamMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-event'],
        params: VlrEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-event-agents'],
        params: VlrEventAgentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventAgentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-event-matches'],
        params: VlrEventMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-event-stats'],
        params: VlrEventStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-events'],
        params: VlrEventsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-forum-categories'],
        params: VlrForumCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrForumCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-forum-threads'],
        params: VlrForumThreadsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrForumThreadsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-match'],
        params: VlrMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-match-economy'],
        params: VlrMatchEconomyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchEconomyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-match-performance'],
        params: VlrMatchPerformanceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchPerformanceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-match-rounds'],
        params: VlrMatchRoundsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchRoundsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-matches'],
        params: VlrMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-news'],
        params: VlrNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-news-article'],
        params: VlrNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrNewsArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-player'],
        params: VlrPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrPlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-player-matches'],
        params: VlrPlayerMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrPlayerMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-rankings'],
        params: VlrRankingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-results'],
        params: VlrResultsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-search'],
        params: VlrSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-stats'],
        params: VlrStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-team'],
        params: VlrTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-team-maps'],
        params: VlrTeamMapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrTeamMapsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['vlr-team-matches'],
        params: VlrTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> VlrTeamMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class VLRClient(CrawloraClient):
    def __enter__(self) -> VLRClient: ...
    @overload
    def event(self, **params: Unpack[VlrEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[VlrEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[VlrEventDefaultParams]) -> VlrEventResponse: ...
    @overload
    def event_agents(self, **params: Unpack[VlrEventAgentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_agents(self, **params: Unpack[VlrEventAgentsTextResponseParams]) -> str: ...
    @overload
    def event_agents(self, **params: Unpack[VlrEventAgentsDefaultParams]) -> VlrEventAgentsResponse: ...
    @overload
    def event_matches(self, **params: Unpack[VlrEventMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def event_matches(self, **params: Unpack[VlrEventMatchesTextResponseParams]) -> str: ...
    @overload
    def event_matches(self, **params: Unpack[VlrEventMatchesDefaultParams]) -> VlrEventMatchesResponse: ...
    @overload
    def event_stats(self, **params: Unpack[VlrEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    def event_stats(self, **params: Unpack[VlrEventStatsTextResponseParams]) -> str: ...
    @overload
    def event_stats(self, **params: Unpack[VlrEventStatsDefaultParams]) -> VlrEventStatsResponse: ...
    @overload
    def events(self, **params: Unpack[VlrEventsStreamParams]) -> BinaryIO: ...
    @overload
    def events(self, **params: Unpack[VlrEventsTextResponseParams]) -> str: ...
    @overload
    def events(self, **params: Unpack[VlrEventsDefaultParams]) -> VlrEventsResponse: ...
    @overload
    def forum_categories(self, **params: Unpack[VlrForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def forum_categories(self, **params: Unpack[VlrForumCategoriesTextResponseParams]) -> str: ...
    @overload
    def forum_categories(self, **params: Unpack[VlrForumCategoriesDefaultParams]) -> VlrForumCategoriesResponse: ...
    @overload
    def forum_threads(self, **params: Unpack[VlrForumThreadsStreamParams]) -> BinaryIO: ...
    @overload
    def forum_threads(self, **params: Unpack[VlrForumThreadsTextResponseParams]) -> str: ...
    @overload
    def forum_threads(self, **params: Unpack[VlrForumThreadsDefaultParams]) -> VlrForumThreadsResponse: ...
    @overload
    def match(self, **params: Unpack[VlrMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[VlrMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[VlrMatchDefaultParams]) -> VlrMatchResponse: ...
    @overload
    def match_economy(self, **params: Unpack[VlrMatchEconomyStreamParams]) -> BinaryIO: ...
    @overload
    def match_economy(self, **params: Unpack[VlrMatchEconomyTextResponseParams]) -> str: ...
    @overload
    def match_economy(self, **params: Unpack[VlrMatchEconomyDefaultParams]) -> VlrMatchEconomyResponse: ...
    @overload
    def match_performance(self, **params: Unpack[VlrMatchPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    def match_performance(self, **params: Unpack[VlrMatchPerformanceTextResponseParams]) -> str: ...
    @overload
    def match_performance(self, **params: Unpack[VlrMatchPerformanceDefaultParams]) -> VlrMatchPerformanceResponse: ...
    @overload
    def match_rounds(self, **params: Unpack[VlrMatchRoundsStreamParams]) -> BinaryIO: ...
    @overload
    def match_rounds(self, **params: Unpack[VlrMatchRoundsTextResponseParams]) -> str: ...
    @overload
    def match_rounds(self, **params: Unpack[VlrMatchRoundsDefaultParams]) -> VlrMatchRoundsResponse: ...
    @overload
    def matches(self, **params: Unpack[VlrMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[VlrMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[VlrMatchesDefaultParams]) -> VlrMatchesResponse: ...
    @overload
    def news(self, **params: Unpack[VlrNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[VlrNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[VlrNewsDefaultParams]) -> VlrNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[VlrNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[VlrNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[VlrNewsArticleDefaultParams]) -> VlrNewsArticleResponse: ...
    @overload
    def player(self, **params: Unpack[VlrPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[VlrPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[VlrPlayerDefaultParams]) -> VlrPlayerResponse: ...
    @overload
    def player_matches(self, **params: Unpack[VlrPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def player_matches(self, **params: Unpack[VlrPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    def player_matches(self, **params: Unpack[VlrPlayerMatchesDefaultParams]) -> VlrPlayerMatchesResponse: ...
    @overload
    def rankings(self, **params: Unpack[VlrRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[VlrRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[VlrRankingsDefaultParams]) -> VlrRankingsResponse: ...
    @overload
    def results(self, **params: Unpack[VlrResultsStreamParams]) -> BinaryIO: ...
    @overload
    def results(self, **params: Unpack[VlrResultsTextResponseParams]) -> str: ...
    @overload
    def results(self, **params: Unpack[VlrResultsDefaultParams]) -> VlrResultsResponse: ...
    @overload
    def search(self, **params: Unpack[VlrSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[VlrSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[VlrSearchDefaultParams]) -> VlrSearchResponse: ...
    @overload
    def stats(self, **params: Unpack[VlrStatsStreamParams]) -> BinaryIO: ...
    @overload
    def stats(self, **params: Unpack[VlrStatsTextResponseParams]) -> str: ...
    @overload
    def stats(self, **params: Unpack[VlrStatsDefaultParams]) -> VlrStatsResponse: ...
    @overload
    def team(self, **params: Unpack[VlrTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[VlrTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[VlrTeamDefaultParams]) -> VlrTeamResponse: ...
    @overload
    def team_maps(self, **params: Unpack[VlrTeamMapsStreamParams]) -> BinaryIO: ...
    @overload
    def team_maps(self, **params: Unpack[VlrTeamMapsTextResponseParams]) -> str: ...
    @overload
    def team_maps(self, **params: Unpack[VlrTeamMapsDefaultParams]) -> VlrTeamMapsResponse: ...
    @overload
    def team_matches(self, **params: Unpack[VlrTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_matches(self, **params: Unpack[VlrTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def team_matches(self, **params: Unpack[VlrTeamMatchesDefaultParams]) -> VlrTeamMatchesResponse: ...

class AsyncVLRClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncVLRClient: ...
    vlr: _AsyncVlrGroup
    @overload
    async def event(self, **params: Unpack[VlrEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[VlrEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[VlrEventDefaultParams]) -> VlrEventResponse: ...
    @overload
    async def event_agents(self, **params: Unpack[VlrEventAgentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_agents(self, **params: Unpack[VlrEventAgentsTextResponseParams]) -> str: ...
    @overload
    async def event_agents(self, **params: Unpack[VlrEventAgentsDefaultParams]) -> VlrEventAgentsResponse: ...
    @overload
    async def event_matches(self, **params: Unpack[VlrEventMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_matches(self, **params: Unpack[VlrEventMatchesTextResponseParams]) -> str: ...
    @overload
    async def event_matches(self, **params: Unpack[VlrEventMatchesDefaultParams]) -> VlrEventMatchesResponse: ...
    @overload
    async def event_stats(self, **params: Unpack[VlrEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_stats(self, **params: Unpack[VlrEventStatsTextResponseParams]) -> str: ...
    @overload
    async def event_stats(self, **params: Unpack[VlrEventStatsDefaultParams]) -> VlrEventStatsResponse: ...
    @overload
    async def events(self, **params: Unpack[VlrEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def events(self, **params: Unpack[VlrEventsTextResponseParams]) -> str: ...
    @overload
    async def events(self, **params: Unpack[VlrEventsDefaultParams]) -> VlrEventsResponse: ...
    @overload
    async def forum_categories(self, **params: Unpack[VlrForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def forum_categories(self, **params: Unpack[VlrForumCategoriesTextResponseParams]) -> str: ...
    @overload
    async def forum_categories(self, **params: Unpack[VlrForumCategoriesDefaultParams]) -> VlrForumCategoriesResponse: ...
    @overload
    async def forum_threads(self, **params: Unpack[VlrForumThreadsStreamParams]) -> BinaryIO: ...
    @overload
    async def forum_threads(self, **params: Unpack[VlrForumThreadsTextResponseParams]) -> str: ...
    @overload
    async def forum_threads(self, **params: Unpack[VlrForumThreadsDefaultParams]) -> VlrForumThreadsResponse: ...
    @overload
    async def match(self, **params: Unpack[VlrMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[VlrMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[VlrMatchDefaultParams]) -> VlrMatchResponse: ...
    @overload
    async def match_economy(self, **params: Unpack[VlrMatchEconomyStreamParams]) -> BinaryIO: ...
    @overload
    async def match_economy(self, **params: Unpack[VlrMatchEconomyTextResponseParams]) -> str: ...
    @overload
    async def match_economy(self, **params: Unpack[VlrMatchEconomyDefaultParams]) -> VlrMatchEconomyResponse: ...
    @overload
    async def match_performance(self, **params: Unpack[VlrMatchPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    async def match_performance(self, **params: Unpack[VlrMatchPerformanceTextResponseParams]) -> str: ...
    @overload
    async def match_performance(self, **params: Unpack[VlrMatchPerformanceDefaultParams]) -> VlrMatchPerformanceResponse: ...
    @overload
    async def match_rounds(self, **params: Unpack[VlrMatchRoundsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_rounds(self, **params: Unpack[VlrMatchRoundsTextResponseParams]) -> str: ...
    @overload
    async def match_rounds(self, **params: Unpack[VlrMatchRoundsDefaultParams]) -> VlrMatchRoundsResponse: ...
    @overload
    async def matches(self, **params: Unpack[VlrMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[VlrMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[VlrMatchesDefaultParams]) -> VlrMatchesResponse: ...
    @overload
    async def news(self, **params: Unpack[VlrNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[VlrNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[VlrNewsDefaultParams]) -> VlrNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[VlrNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[VlrNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[VlrNewsArticleDefaultParams]) -> VlrNewsArticleResponse: ...
    @overload
    async def player(self, **params: Unpack[VlrPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[VlrPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[VlrPlayerDefaultParams]) -> VlrPlayerResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[VlrPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[VlrPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[VlrPlayerMatchesDefaultParams]) -> VlrPlayerMatchesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[VlrRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[VlrRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[VlrRankingsDefaultParams]) -> VlrRankingsResponse: ...
    @overload
    async def results(self, **params: Unpack[VlrResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def results(self, **params: Unpack[VlrResultsTextResponseParams]) -> str: ...
    @overload
    async def results(self, **params: Unpack[VlrResultsDefaultParams]) -> VlrResultsResponse: ...
    @overload
    async def search(self, **params: Unpack[VlrSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[VlrSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[VlrSearchDefaultParams]) -> VlrSearchResponse: ...
    @overload
    async def stats(self, **params: Unpack[VlrStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def stats(self, **params: Unpack[VlrStatsTextResponseParams]) -> str: ...
    @overload
    async def stats(self, **params: Unpack[VlrStatsDefaultParams]) -> VlrStatsResponse: ...
    @overload
    async def team(self, **params: Unpack[VlrTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[VlrTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[VlrTeamDefaultParams]) -> VlrTeamResponse: ...
    @overload
    async def team_maps(self, **params: Unpack[VlrTeamMapsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_maps(self, **params: Unpack[VlrTeamMapsTextResponseParams]) -> str: ...
    @overload
    async def team_maps(self, **params: Unpack[VlrTeamMapsDefaultParams]) -> VlrTeamMapsResponse: ...
    @overload
    async def team_matches(self, **params: Unpack[VlrTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_matches(self, **params: Unpack[VlrTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_matches(self, **params: Unpack[VlrTeamMatchesDefaultParams]) -> VlrTeamMatchesResponse: ...

class _AsyncVlrGroup:
    @overload
    async def event(self, **params: Unpack[VlrEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[VlrEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[VlrEventDefaultParams]) -> VlrEventResponse: ...
    @overload
    async def event_agents(self, **params: Unpack[VlrEventAgentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_agents(self, **params: Unpack[VlrEventAgentsTextResponseParams]) -> str: ...
    @overload
    async def event_agents(self, **params: Unpack[VlrEventAgentsDefaultParams]) -> VlrEventAgentsResponse: ...
    @overload
    async def event_matches(self, **params: Unpack[VlrEventMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_matches(self, **params: Unpack[VlrEventMatchesTextResponseParams]) -> str: ...
    @overload
    async def event_matches(self, **params: Unpack[VlrEventMatchesDefaultParams]) -> VlrEventMatchesResponse: ...
    @overload
    async def event_stats(self, **params: Unpack[VlrEventStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_stats(self, **params: Unpack[VlrEventStatsTextResponseParams]) -> str: ...
    @overload
    async def event_stats(self, **params: Unpack[VlrEventStatsDefaultParams]) -> VlrEventStatsResponse: ...
    @overload
    async def events(self, **params: Unpack[VlrEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def events(self, **params: Unpack[VlrEventsTextResponseParams]) -> str: ...
    @overload
    async def events(self, **params: Unpack[VlrEventsDefaultParams]) -> VlrEventsResponse: ...
    @overload
    async def forum_categories(self, **params: Unpack[VlrForumCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def forum_categories(self, **params: Unpack[VlrForumCategoriesTextResponseParams]) -> str: ...
    @overload
    async def forum_categories(self, **params: Unpack[VlrForumCategoriesDefaultParams]) -> VlrForumCategoriesResponse: ...
    @overload
    async def forum_threads(self, **params: Unpack[VlrForumThreadsStreamParams]) -> BinaryIO: ...
    @overload
    async def forum_threads(self, **params: Unpack[VlrForumThreadsTextResponseParams]) -> str: ...
    @overload
    async def forum_threads(self, **params: Unpack[VlrForumThreadsDefaultParams]) -> VlrForumThreadsResponse: ...
    @overload
    async def match(self, **params: Unpack[VlrMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[VlrMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[VlrMatchDefaultParams]) -> VlrMatchResponse: ...
    @overload
    async def match_economy(self, **params: Unpack[VlrMatchEconomyStreamParams]) -> BinaryIO: ...
    @overload
    async def match_economy(self, **params: Unpack[VlrMatchEconomyTextResponseParams]) -> str: ...
    @overload
    async def match_economy(self, **params: Unpack[VlrMatchEconomyDefaultParams]) -> VlrMatchEconomyResponse: ...
    @overload
    async def match_performance(self, **params: Unpack[VlrMatchPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    async def match_performance(self, **params: Unpack[VlrMatchPerformanceTextResponseParams]) -> str: ...
    @overload
    async def match_performance(self, **params: Unpack[VlrMatchPerformanceDefaultParams]) -> VlrMatchPerformanceResponse: ...
    @overload
    async def match_rounds(self, **params: Unpack[VlrMatchRoundsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_rounds(self, **params: Unpack[VlrMatchRoundsTextResponseParams]) -> str: ...
    @overload
    async def match_rounds(self, **params: Unpack[VlrMatchRoundsDefaultParams]) -> VlrMatchRoundsResponse: ...
    @overload
    async def matches(self, **params: Unpack[VlrMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[VlrMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[VlrMatchesDefaultParams]) -> VlrMatchesResponse: ...
    @overload
    async def news(self, **params: Unpack[VlrNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[VlrNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[VlrNewsDefaultParams]) -> VlrNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[VlrNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[VlrNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[VlrNewsArticleDefaultParams]) -> VlrNewsArticleResponse: ...
    @overload
    async def player(self, **params: Unpack[VlrPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[VlrPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[VlrPlayerDefaultParams]) -> VlrPlayerResponse: ...
    @overload
    async def player_matches(self, **params: Unpack[VlrPlayerMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_matches(self, **params: Unpack[VlrPlayerMatchesTextResponseParams]) -> str: ...
    @overload
    async def player_matches(self, **params: Unpack[VlrPlayerMatchesDefaultParams]) -> VlrPlayerMatchesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[VlrRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[VlrRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[VlrRankingsDefaultParams]) -> VlrRankingsResponse: ...
    @overload
    async def results(self, **params: Unpack[VlrResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def results(self, **params: Unpack[VlrResultsTextResponseParams]) -> str: ...
    @overload
    async def results(self, **params: Unpack[VlrResultsDefaultParams]) -> VlrResultsResponse: ...
    @overload
    async def search(self, **params: Unpack[VlrSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[VlrSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[VlrSearchDefaultParams]) -> VlrSearchResponse: ...
    @overload
    async def stats(self, **params: Unpack[VlrStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def stats(self, **params: Unpack[VlrStatsTextResponseParams]) -> str: ...
    @overload
    async def stats(self, **params: Unpack[VlrStatsDefaultParams]) -> VlrStatsResponse: ...
    @overload
    async def team(self, **params: Unpack[VlrTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[VlrTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[VlrTeamDefaultParams]) -> VlrTeamResponse: ...
    @overload
    async def team_maps(self, **params: Unpack[VlrTeamMapsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_maps(self, **params: Unpack[VlrTeamMapsTextResponseParams]) -> str: ...
    @overload
    async def team_maps(self, **params: Unpack[VlrTeamMapsDefaultParams]) -> VlrTeamMapsResponse: ...
    @overload
    async def team_matches(self, **params: Unpack[VlrTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_matches(self, **params: Unpack[VlrTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_matches(self, **params: Unpack[VlrTeamMatchesDefaultParams]) -> VlrTeamMatchesResponse: ...

VlrEventDefaultParams = TypedDict('VlrEventDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrEventTextResponseParams = TypedDict('VlrEventTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrEventStreamParams = TypedDict('VlrEventStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrEventAgentsDefaultParams = TypedDict('VlrEventAgentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrEventAgentsTextResponseParams = TypedDict('VlrEventAgentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrEventAgentsStreamParams = TypedDict('VlrEventAgentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrEventMatchesDefaultParams = TypedDict('VlrEventMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'series_id': NotRequired[str],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

VlrEventMatchesTextResponseParams = TypedDict('VlrEventMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'series_id': NotRequired[str],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

VlrEventMatchesStreamParams = TypedDict('VlrEventMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'series_id': NotRequired[str],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

VlrEventStatsDefaultParams = TypedDict('VlrEventStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'stage': NotRequired[str],
    'min_rounds': NotRequired[int],
    'sort': NotRequired[str],
    'dir': NotRequired[Literal['desc', 'asc']],
}, total=False)

VlrEventStatsTextResponseParams = TypedDict('VlrEventStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'stage': NotRequired[str],
    'min_rounds': NotRequired[int],
    'sort': NotRequired[str],
    'dir': NotRequired[Literal['desc', 'asc']],
}, total=False)

VlrEventStatsStreamParams = TypedDict('VlrEventStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'stage': NotRequired[str],
    'min_rounds': NotRequired[int],
    'sort': NotRequired[str],
    'dir': NotRequired[Literal['desc', 'asc']],
}, total=False)

VlrEventsDefaultParams = TypedDict('VlrEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tier': NotRequired[Literal['all', 'vct', 'vcl', 't3', 'gc', 'cg', 'off']],
    'region': NotRequired[Literal['all', 'americas', 'emea', 'pacific', 'china']],
    'page': NotRequired[int],
}, total=False)

VlrEventsTextResponseParams = TypedDict('VlrEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tier': NotRequired[Literal['all', 'vct', 'vcl', 't3', 'gc', 'cg', 'off']],
    'region': NotRequired[Literal['all', 'americas', 'emea', 'pacific', 'china']],
    'page': NotRequired[int],
}, total=False)

VlrEventsStreamParams = TypedDict('VlrEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tier': NotRequired[Literal['all', 'vct', 'vcl', 't3', 'gc', 'cg', 'off']],
    'region': NotRequired[Literal['all', 'americas', 'emea', 'pacific', 'china']],
    'page': NotRequired[int],
}, total=False)

VlrForumCategoriesDefaultParams = TypedDict('VlrForumCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

VlrForumCategoriesTextResponseParams = TypedDict('VlrForumCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

VlrForumCategoriesStreamParams = TypedDict('VlrForumCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

VlrForumThreadsDefaultParams = TypedDict('VlrForumThreadsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['valorant-discussion', 'off-topic', 'site-feedback']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['hot', 'new', 'top']],
}, total=False)

VlrForumThreadsTextResponseParams = TypedDict('VlrForumThreadsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['valorant-discussion', 'off-topic', 'site-feedback']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['hot', 'new', 'top']],
}, total=False)

VlrForumThreadsStreamParams = TypedDict('VlrForumThreadsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['valorant-discussion', 'off-topic', 'site-feedback']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['hot', 'new', 'top']],
}, total=False)

VlrMatchDefaultParams = TypedDict('VlrMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrMatchTextResponseParams = TypedDict('VlrMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrMatchStreamParams = TypedDict('VlrMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrMatchEconomyDefaultParams = TypedDict('VlrMatchEconomyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrMatchEconomyTextResponseParams = TypedDict('VlrMatchEconomyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrMatchEconomyStreamParams = TypedDict('VlrMatchEconomyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrMatchPerformanceDefaultParams = TypedDict('VlrMatchPerformanceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrMatchPerformanceTextResponseParams = TypedDict('VlrMatchPerformanceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrMatchPerformanceStreamParams = TypedDict('VlrMatchPerformanceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrMatchRoundsDefaultParams = TypedDict('VlrMatchRoundsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrMatchRoundsTextResponseParams = TypedDict('VlrMatchRoundsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrMatchRoundsStreamParams = TypedDict('VlrMatchRoundsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrMatchesDefaultParams = TypedDict('VlrMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'page': NotRequired[int],
}, total=False)

VlrMatchesTextResponseParams = TypedDict('VlrMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'page': NotRequired[int],
}, total=False)

VlrMatchesStreamParams = TypedDict('VlrMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'page': NotRequired[int],
}, total=False)

VlrNewsDefaultParams = TypedDict('VlrNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'page': NotRequired[int],
}, total=False)

VlrNewsTextResponseParams = TypedDict('VlrNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'page': NotRequired[int],
}, total=False)

VlrNewsStreamParams = TypedDict('VlrNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'page': NotRequired[int],
}, total=False)

VlrNewsArticleDefaultParams = TypedDict('VlrNewsArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrNewsArticleTextResponseParams = TypedDict('VlrNewsArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrNewsArticleStreamParams = TypedDict('VlrNewsArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrPlayerDefaultParams = TypedDict('VlrPlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d']],
}, total=False)

VlrPlayerTextResponseParams = TypedDict('VlrPlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d']],
}, total=False)

VlrPlayerStreamParams = TypedDict('VlrPlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d']],
}, total=False)

VlrPlayerMatchesDefaultParams = TypedDict('VlrPlayerMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

VlrPlayerMatchesTextResponseParams = TypedDict('VlrPlayerMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

VlrPlayerMatchesStreamParams = TypedDict('VlrPlayerMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

VlrRankingsDefaultParams = TypedDict('VlrRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'region': NotRequired[Literal['north-america', 'europe', 'brazil', 'asia-pacific', 'korea', 'china', 'japan', 'la-s', 'la-n', 'oceania', 'mena', 'gc', 'collegiate']],
    'limit': NotRequired[int],
}, total=False)

VlrRankingsTextResponseParams = TypedDict('VlrRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'region': NotRequired[Literal['north-america', 'europe', 'brazil', 'asia-pacific', 'korea', 'china', 'japan', 'la-s', 'la-n', 'oceania', 'mena', 'gc', 'collegiate']],
    'limit': NotRequired[int],
}, total=False)

VlrRankingsStreamParams = TypedDict('VlrRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'region': NotRequired[Literal['north-america', 'europe', 'brazil', 'asia-pacific', 'korea', 'china', 'japan', 'la-s', 'la-n', 'oceania', 'mena', 'gc', 'collegiate']],
    'limit': NotRequired[int],
}, total=False)

VlrResultsDefaultParams = TypedDict('VlrResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'page': NotRequired[int],
}, total=False)

VlrResultsTextResponseParams = TypedDict('VlrResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'page': NotRequired[int],
}, total=False)

VlrResultsStreamParams = TypedDict('VlrResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'page': NotRequired[int],
}, total=False)

VlrSearchDefaultParams = TypedDict('VlrSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'teams', 'events', 'players']],
}, total=False)

VlrSearchTextResponseParams = TypedDict('VlrSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'teams', 'events', 'players']],
}, total=False)

VlrSearchStreamParams = TypedDict('VlrSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'type': NotRequired[Literal['all', 'teams', 'events', 'players']],
}, total=False)

VlrStatsDefaultParams = TypedDict('VlrStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tier': NotRequired[str],
    'region': NotRequired[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d', '2026', '2025', '2024', '2023', '2022', '2021', '2020']],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'min_rounds': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'min_rating': NotRequired[Literal['0', '1300', '1400', '1500', '1550', '1650', '1750', '1850']],
    'sort': NotRequired[Literal['rating', 'maps', 'rnd', 'acs', 'kd', 'kast', 'adr', 'kpr', 'apr', 'fkfd', 'fkpr', 'fdpr', 'hsp', 'clp', 'cl', 'kmax', 'k', 'd', 'a', 'fk', 'fd']],
    'dir': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
}, total=False)

VlrStatsTextResponseParams = TypedDict('VlrStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tier': NotRequired[str],
    'region': NotRequired[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d', '2026', '2025', '2024', '2023', '2022', '2021', '2020']],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'min_rounds': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'min_rating': NotRequired[Literal['0', '1300', '1400', '1500', '1550', '1650', '1750', '1850']],
    'sort': NotRequired[Literal['rating', 'maps', 'rnd', 'acs', 'kd', 'kast', 'adr', 'kpr', 'apr', 'fkfd', 'fkpr', 'fdpr', 'hsp', 'clp', 'cl', 'kmax', 'k', 'd', 'a', 'fk', 'fd']],
    'dir': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
}, total=False)

VlrStatsStreamParams = TypedDict('VlrStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tier': NotRequired[str],
    'region': NotRequired[str],
    'timespan': NotRequired[Literal['all', '30d', '60d', '90d', '2026', '2025', '2024', '2023', '2022', '2021', '2020']],
    'side': NotRequired[Literal['all', 't', 'ct']],
    'role': NotRequired[str],
    'agent': NotRequired[str],
    'map': NotRequired[str],
    'min_rounds': NotRequired[int],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'min_rating': NotRequired[Literal['0', '1300', '1400', '1500', '1550', '1650', '1750', '1850']],
    'sort': NotRequired[Literal['rating', 'maps', 'rnd', 'acs', 'kd', 'kast', 'adr', 'kpr', 'apr', 'fkfd', 'fkpr', 'fdpr', 'hsp', 'clp', 'cl', 'kmax', 'k', 'd', 'a', 'fk', 'fd']],
    'dir': NotRequired[Literal['asc', 'desc']],
    'page': NotRequired[int],
}, total=False)

VlrTeamDefaultParams = TypedDict('VlrTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrTeamTextResponseParams = TypedDict('VlrTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrTeamStreamParams = TypedDict('VlrTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrTeamMapsDefaultParams = TypedDict('VlrTeamMapsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

VlrTeamMapsTextResponseParams = TypedDict('VlrTeamMapsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

VlrTeamMapsStreamParams = TypedDict('VlrTeamMapsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

VlrTeamMatchesDefaultParams = TypedDict('VlrTeamMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

VlrTeamMatchesTextResponseParams = TypedDict('VlrTeamMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)

VlrTeamMatchesStreamParams = TypedDict('VlrTeamMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
    'group': NotRequired[Literal['completed', 'upcoming']],
}, total=False)
