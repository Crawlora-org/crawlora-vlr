package net.crawlora.vlr;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the VLR.gg endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 23;
    public static final List<String> OPERATION_IDS = List.of(
            "vlr-event",
            "vlr-event-agents",
            "vlr-event-matches",
            "vlr-event-stats",
            "vlr-events",
            "vlr-forum-categories",
            "vlr-forum-threads",
            "vlr-match",
            "vlr-match-economy",
            "vlr-match-performance",
            "vlr-match-rounds",
            "vlr-matches",
            "vlr-news",
            "vlr-news-article",
            "vlr-player",
            "vlr-player-matches",
            "vlr-rankings",
            "vlr-results",
            "vlr-search",
            "vlr-stats",
            "vlr-team",
            "vlr-team-maps",
            "vlr-team-matches"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("vlr-event", new Operation("vlr-event", "GET", "/vlr/event", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-event-agents", new Operation("vlr-event-agents", "GET", "/vlr/event-agents", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-event-matches", new Operation("vlr-event-matches", "GET", "/vlr/event-matches", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("series_id", new Param("series_id", "query", false, "string", List.of(), "csv")), Map.entry("group", new Param("group", "query", false, "string", List.of("completed", "upcoming"), "csv"))), List.of("application/json")));
        operations.put("vlr-event-stats", new Operation("vlr-event-stats", "GET", "/vlr/event-stats", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("side", new Param("side", "query", false, "string", List.of("all", "t", "ct"), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of(), "csv")), Map.entry("agent", new Param("agent", "query", false, "string", List.of(), "csv")), Map.entry("map", new Param("map", "query", false, "string", List.of(), "csv")), Map.entry("stage", new Param("stage", "query", false, "string", List.of(), "csv")), Map.entry("min_rounds", new Param("min_rounds", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of(), "csv")), Map.entry("dir", new Param("dir", "query", false, "string", List.of("desc", "asc"), "csv"))), List.of("application/json")));
        operations.put("vlr-events", new Operation("vlr-events", "GET", "/vlr/events", Map.ofEntries(Map.entry("tier", new Param("tier", "query", false, "string", List.of("all", "vct", "vcl", "t3", "gc", "cg", "off"), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of("all", "americas", "emea", "pacific", "china"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-forum-categories", new Operation("vlr-forum-categories", "GET", "/vlr/forum-categories", Map.of(), List.of("application/json")));
        operations.put("vlr-forum-threads", new Operation("vlr-forum-threads", "GET", "/vlr/forum-threads", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("valorant-discussion", "off-topic", "site-feedback"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top"), "csv"))), List.of("application/json")));
        operations.put("vlr-match", new Operation("vlr-match", "GET", "/vlr/match", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-match-economy", new Operation("vlr-match-economy", "GET", "/vlr/match-economy", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-match-performance", new Operation("vlr-match-performance", "GET", "/vlr/match-performance", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-match-rounds", new Operation("vlr-match-rounds", "GET", "/vlr/match-rounds", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-matches", new Operation("vlr-matches", "GET", "/vlr/matches", Map.ofEntries(Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-news", new Operation("vlr-news", "GET", "/vlr/news", Map.ofEntries(Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-news-article", new Operation("vlr-news-article", "GET", "/vlr/news-article", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-player", new Operation("vlr-player", "GET", "/vlr/player", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("timespan", new Param("timespan", "query", false, "string", List.of("all", "30d", "60d", "90d"), "csv"))), List.of("application/json")));
        operations.put("vlr-player-matches", new Operation("vlr-player-matches", "GET", "/vlr/player-matches", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-rankings", new Operation("vlr-rankings", "GET", "/vlr/rankings", Map.ofEntries(Map.entry("region", new Param("region", "query", false, "string", List.of("north-america", "europe", "brazil", "asia-pacific", "korea", "china", "japan", "la-s", "la-n", "oceania", "mena", "gc", "collegiate"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-results", new Operation("vlr-results", "GET", "/vlr/results", Map.ofEntries(Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-search", new Operation("vlr-search", "GET", "/vlr/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("all", "teams", "events", "players"), "csv"))), List.of("application/json")));
        operations.put("vlr-stats", new Operation("vlr-stats", "GET", "/vlr/stats", Map.ofEntries(Map.entry("tier", new Param("tier", "query", false, "string", List.of(), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("timespan", new Param("timespan", "query", false, "string", List.of("all", "30d", "60d", "90d", "2026", "2025", "2024", "2023", "2022", "2021", "2020"), "csv")), Map.entry("side", new Param("side", "query", false, "string", List.of("all", "t", "ct"), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of(), "csv")), Map.entry("agent", new Param("agent", "query", false, "string", List.of(), "csv")), Map.entry("map", new Param("map", "query", false, "string", List.of(), "csv")), Map.entry("min_rounds", new Param("min_rounds", "query", false, "integer", List.of(), "csv")), Map.entry("from", new Param("from", "query", false, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", false, "string", List.of(), "csv")), Map.entry("min_rating", new Param("min_rating", "query", false, "integer", List.of("0", "1300", "1400", "1500", "1550", "1650", "1750", "1850"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("rating", "maps", "rnd", "acs", "kd", "kast", "adr", "kpr", "apr", "fkfd", "fkpr", "fdpr", "hsp", "clp", "cl", "kmax", "k", "d", "a", "fk", "fd"), "csv")), Map.entry("dir", new Param("dir", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-team", new Operation("vlr-team", "GET", "/vlr/team", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-team-maps", new Operation("vlr-team-maps", "GET", "/vlr/team-maps", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("vlr-team-matches", new Operation("vlr-team-matches", "GET", "/vlr/team-matches", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("group", new Param("group", "query", false, "string", List.of("completed", "upcoming"), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown VLR.gg operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object event(Map<String, ?> params) { return request("vlr-event", params); }
    public Object eventAgents(Map<String, ?> params) { return request("vlr-event-agents", params); }
    public Object eventMatches(Map<String, ?> params) { return request("vlr-event-matches", params); }
    public Object eventStats(Map<String, ?> params) { return request("vlr-event-stats", params); }
    public Object events(Map<String, ?> params) { return request("vlr-events", params); }
    public Object forumCategories(Map<String, ?> params) { return request("vlr-forum-categories", params); }
    public Object forumThreads(Map<String, ?> params) { return request("vlr-forum-threads", params); }
    public Object match(Map<String, ?> params) { return request("vlr-match", params); }
    public Object matchEconomy(Map<String, ?> params) { return request("vlr-match-economy", params); }
    public Object matchPerformance(Map<String, ?> params) { return request("vlr-match-performance", params); }
    public Object matchRounds(Map<String, ?> params) { return request("vlr-match-rounds", params); }
    public Object matches(Map<String, ?> params) { return request("vlr-matches", params); }
    public Object news(Map<String, ?> params) { return request("vlr-news", params); }
    public Object newsArticle(Map<String, ?> params) { return request("vlr-news-article", params); }
    public Object player(Map<String, ?> params) { return request("vlr-player", params); }
    public Object playerMatches(Map<String, ?> params) { return request("vlr-player-matches", params); }
    public Object rankings(Map<String, ?> params) { return request("vlr-rankings", params); }
    public Object results(Map<String, ?> params) { return request("vlr-results", params); }
    public Object search(Map<String, ?> params) { return request("vlr-search", params); }
    public Object stats(Map<String, ?> params) { return request("vlr-stats", params); }
    public Object team(Map<String, ?> params) { return request("vlr-team", params); }
    public Object teamMaps(Map<String, ?> params) { return request("vlr-team-maps", params); }
    public Object teamMatches(Map<String, ?> params) { return request("vlr-team-matches", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
