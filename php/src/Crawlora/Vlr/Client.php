<?php

declare(strict_types=1);

namespace Crawlora\Vlr;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'vlr';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 23;
    public const OPERATION_IDS = ["vlr-event", "vlr-event-agents", "vlr-event-matches", "vlr-event-stats", "vlr-events", "vlr-forum-categories", "vlr-forum-threads", "vlr-match", "vlr-match-economy", "vlr-match-performance", "vlr-match-rounds", "vlr-matches", "vlr-news", "vlr-news-article", "vlr-player", "vlr-player-matches", "vlr-rankings", "vlr-results", "vlr-search", "vlr-stats", "vlr-team", "vlr-team-maps", "vlr-team-matches"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"vlr-event": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}], "path": "/vlr/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-event-agents": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event-agents", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}], "path": "/vlr/event-agents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-event-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event-matches", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}, {"description": "Stage id from the stages list of an earlier response (a week, group or bracket round); omit for every stage", "in": "query", "name": "series_id", "type": "string", "x-example": "6080"}, {"description": "Match group; one of completed, upcoming; omit for both", "enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "path": "/vlr/event-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "series_id", "type": "string"}, {"enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-event-stats": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event-stats", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}, {"description": "Side; one of all, t, ct; defaults to all", "enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"description": "Comma-separated agent roles; any of controller, initiator, sentinel, duelist", "in": "query", "name": "role", "type": "string", "x-example": "duelist"}, {"description": "Comma-separated agents, for example jett,sage; the same 29 agents as vlr-stats", "in": "query", "name": "agent", "type": "string", "x-example": "jett"}, {"description": "Comma-separated map names, for example ascent,bind; the same 13 maps as vlr-stats", "in": "query", "name": "map", "type": "string", "x-example": "ascent"}, {"description": "Comma-separated stage ids from the stages list of vlr-event-matches", "in": "query", "name": "stage", "type": "string", "x-example": "6080"}, {"description": "Minimum rounds played; 0 to 100000", "in": "query", "maximum": 100000, "minimum": 0, "name": "min_rounds", "type": "integer"}, {"description": "Sort column, the same set as vlr-stats; defaults to rating", "in": "query", "name": "sort", "type": "string"}, {"description": "Sort direction; one of desc, asc; defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "dir", "type": "string"}], "path": "/vlr/event-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "agent", "type": "string"}, {"in": "query", "name": "map", "type": "string"}, {"in": "query", "name": "stage", "type": "string"}, {"in": "query", "name": "min_rounds", "type": "integer"}, {"in": "query", "name": "sort", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "dir", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-events": {"bodyParam": null, "bodyRequired": false, "id": "vlr-events", "method": "GET", "params": [{"description": "Event tier; one of all, vct, vcl, t3, gc, cg, off; defaults to all", "enum": ["all", "vct", "vcl", "t3", "gc", "cg", "off"], "in": "query", "name": "tier", "type": "string"}, {"description": "Event region; one of all, americas, emea, pacific, china; defaults to all", "enum": ["all", "americas", "emea", "pacific", "china"], "in": "query", "name": "region", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "vct", "vcl", "t3", "gc", "cg", "off"], "in": "query", "name": "tier", "type": "string"}, {"enum": ["all", "americas", "emea", "pacific", "china"], "in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-forum-categories": {"bodyParam": null, "bodyRequired": false, "id": "vlr-forum-categories", "method": "GET", "params": [], "path": "/vlr/forum-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "vlr-forum-threads": {"bodyParam": null, "bodyRequired": false, "id": "vlr-forum-threads", "method": "GET", "params": [{"description": "Forum category; one of valorant-discussion, off-topic, site-feedback; omit for the combined list", "enum": ["valorant-discussion", "off-topic", "site-feedback"], "in": "query", "name": "category", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}, {"description": "Order; one of hot, new, top; omit for the site default (recent activity)", "enum": ["hot", "new", "top"], "in": "query", "name": "sort", "type": "string"}], "path": "/vlr/forum-threads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["valorant-discussion", "off-topic", "site-feedback"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["hot", "new", "top"], "in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "777956"}], "path": "/vlr/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match-economy": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match-economy", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "754737"}], "path": "/vlr/match-economy", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match-performance": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match-performance", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "754737"}], "path": "/vlr/match-performance", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match-rounds": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match-rounds", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "754737"}], "path": "/vlr/match-rounds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-matches", "method": "GET", "params": [{"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-news": {"bodyParam": null, "bodyRequired": false, "id": "vlr-news", "method": "GET", "params": [{"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-news-article": {"bodyParam": null, "bodyRequired": false, "id": "vlr-news-article", "method": "GET", "params": [{"description": "Numeric VLR news article id from vlr-news", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "781119"}], "path": "/vlr/news-article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-player": {"bodyParam": null, "bodyRequired": false, "id": "vlr-player", "method": "GET", "params": [{"description": "Numeric VLR player id from vlr-team or vlr-stats", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9780"}, {"description": "Window of the agent statistics; one of all, 30d, 60d, 90d; omit for the site default", "enum": ["all", "30d", "60d", "90d"], "in": "query", "name": "timespan", "type": "string"}], "path": "/vlr/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["all", "30d", "60d", "90d"], "in": "query", "name": "timespan", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-player-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-player-matches", "method": "GET", "params": [{"description": "Numeric VLR player id from vlr-team or vlr-stats", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9780"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/player-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-rankings": {"bodyParam": null, "bodyRequired": false, "id": "vlr-rankings", "method": "GET", "params": [{"description": "Ranking region; one of north-america, europe, brazil, asia-pacific, korea, china, japan, la-s, la-n, oceania, mena, gc, collegiate; defaults to north-america", "enum": ["north-america", "europe", "brazil", "asia-pacific", "korea", "china", "japan", "la-s", "la-n", "oceania", "mena", "gc", "collegiate"], "in": "query", "name": "region", "type": "string"}, {"description": "Number of top teams to return, 1 to 250; defaults to 50", "in": "query", "maximum": 250, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/vlr/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["north-america", "europe", "brazil", "asia-pacific", "korea", "china", "japan", "la-s", "la-n", "oceania", "mena", "gc", "collegiate"], "in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-results": {"bodyParam": null, "bodyRequired": false, "id": "vlr-results", "method": "GET", "params": [{"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-search": {"bodyParam": null, "bodyRequired": false, "id": "vlr-search", "method": "GET", "params": [{"description": "Search text, 1 to 100 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "sentinels"}, {"description": "Result group; one of all, teams, events, players; defaults to all", "enum": ["all", "teams", "events", "players"], "in": "query", "name": "type", "type": "string"}], "path": "/vlr/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"enum": ["all", "teams", "events", "players"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-stats": {"bodyParam": null, "bodyRequired": false, "id": "vlr-stats", "method": "GET", "params": [{"description": "Comma-separated tiers from vct, vcl, t3, gc, cg, off; site default vct", "in": "query", "name": "tier", "type": "string"}, {"description": "Comma-separated regions from americas, emea, pacific, china, intl", "in": "query", "name": "region", "type": "string"}, {"description": "Timespan; one of all, 30d, 60d, 90d, 2026, 2025, 2024, 2023, 2022, 2021, 2020; site default 60d", "enum": ["all", "30d", "60d", "90d", "2026", "2025", "2024", "2023", "2022", "2021", "2020"], "in": "query", "name": "timespan", "type": "string"}, {"description": "Side; one of all, t, ct", "enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"description": "Comma-separated roles from controller, initiator, sentinel, duelist", "in": "query", "name": "role", "type": "string"}, {"description": "Comma-separated agents from astra, brimstone, clove, harbor, miks, omen, viper, breach, fade, gekko, kayo, skye, sova, tejo, chamber, cypher, deadlock, killjoy, sage, veto, vyse, iso, jett, neon, phoenix, raze, reyna, waylay, yoru", "in": "query", "name": "agent", "type": "string"}, {"description": "Comma-separated maps from abyss, bind, corrode, haven, lotus, summit, sunset, ascent, breeze, fracture, icebox, pearl, split", "in": "query", "name": "map", "type": "string"}, {"description": "Minimum rounds played; site default 100", "in": "query", "minimum": 0, "name": "min_rounds", "type": "integer"}, {"description": "First day of a custom date range, YYYY-MM-DD (UTC); requires to and replaces timespan", "in": "query", "name": "from", "type": "string", "x-example": "2026-09-01"}, {"description": "Last day of a custom date range, YYYY-MM-DD (UTC); requires from and replaces timespan", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-01"}, {"description": "Minimum player rating; one of 0, 1300, 1400, 1500, 1550, 1650, 1750, 1850", "enum": [0, 1300, 1400, 1500, 1550, 1650, 1750, 1850], "in": "query", "name": "min_rating", "type": "integer"}, {"description": "Sort column; one of rating, maps, rnd, acs, kd, kast, adr, kpr, apr, fkfd, fkpr, fdpr, hsp, clp, cl, kmax, k, d, a, fk, fd; defaults to rating", "enum": ["rating", "maps", "rnd", "acs", "kd", "kast", "adr", "kpr", "apr", "fkfd", "fkpr", "fdpr", "hsp", "clp", "cl", "kmax", "k", "d", "a", "fk", "fd"], "in": "query", "name": "sort", "type": "string"}, {"description": "Sort direction; one of asc, desc; defaults to desc", "enum": ["asc", "desc"], "in": "query", "name": "dir", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tier", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"enum": ["all", "30d", "60d", "90d", "2026", "2025", "2024", "2023", "2022", "2021", "2020"], "in": "query", "name": "timespan", "type": "string"}, {"enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "agent", "type": "string"}, {"in": "query", "name": "map", "type": "string"}, {"in": "query", "name": "min_rounds", "type": "integer"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["0", "1300", "1400", "1500", "1550", "1650", "1750", "1850"], "in": "query", "name": "min_rating", "type": "integer"}, {"enum": ["rating", "maps", "rnd", "acs", "kd", "kast", "adr", "kpr", "apr", "fkfd", "fkpr", "fdpr", "hsp", "clp", "cl", "kmax", "k", "d", "a", "fk", "fd"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "dir", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-team": {"bodyParam": null, "bodyRequired": false, "id": "vlr-team", "method": "GET", "params": [{"description": "Numeric VLR team id from vlr-rankings, vlr-event or vlr-match", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2059"}], "path": "/vlr/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-team-maps": {"bodyParam": null, "bodyRequired": false, "id": "vlr-team-maps", "method": "GET", "params": [{"description": "Numeric VLR team id from vlr-rankings, vlr-event or vlr-match", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2059"}], "path": "/vlr/team-maps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-team-matches", "method": "GET", "params": [{"description": "Numeric VLR team id from vlr-rankings, vlr-event or vlr-match", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2059"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}, {"description": "Match group; one of completed (default), upcoming", "enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "path": "/vlr/team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-vlr-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function event(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-event", $params, $responseType);
    }
    public function event_agents(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-event-agents", $params, $responseType);
    }
    public function event_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-event-matches", $params, $responseType);
    }
    public function event_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-event-stats", $params, $responseType);
    }
    public function events(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-events", $params, $responseType);
    }
    public function forum_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-forum-categories", $params, $responseType);
    }
    public function forum_threads(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-forum-threads", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-match", $params, $responseType);
    }
    public function match_economy(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-match-economy", $params, $responseType);
    }
    public function match_performance(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-match-performance", $params, $responseType);
    }
    public function match_rounds(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-match-rounds", $params, $responseType);
    }
    public function matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-matches", $params, $responseType);
    }
    public function news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-news", $params, $responseType);
    }
    public function news_article(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-news-article", $params, $responseType);
    }
    public function player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-player", $params, $responseType);
    }
    public function player_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-player-matches", $params, $responseType);
    }
    public function rankings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-rankings", $params, $responseType);
    }
    public function results(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-results", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-search", $params, $responseType);
    }
    public function stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-stats", $params, $responseType);
    }
    public function team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-team", $params, $responseType);
    }
    public function team_maps(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-team-maps", $params, $responseType);
    }
    public function team_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("vlr-team-matches", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
