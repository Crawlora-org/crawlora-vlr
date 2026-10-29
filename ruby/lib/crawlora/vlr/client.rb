require "json"
require "net/http"
require "uri"

module Crawlora
  module Vlr
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"vlr-event": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}], "path": "/vlr/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-event-agents": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event-agents", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}], "path": "/vlr/event-agents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-event-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event-matches", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}, {"description": "Stage id from the stages list of an earlier response (a week, group or bracket round); omit for every stage", "in": "query", "name": "series_id", "type": "string", "x-example": "6080"}, {"description": "Match group; one of completed, upcoming; omit for both", "enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "path": "/vlr/event-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "series_id", "type": "string"}, {"enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-event-stats": {"bodyParam": null, "bodyRequired": false, "id": "vlr-event-stats", "method": "GET", "params": [{"description": "Numeric VLR event id from vlr-events", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3166"}, {"description": "Side; one of all, t, ct; defaults to all", "enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"description": "Comma-separated agent roles; any of controller, initiator, sentinel, duelist", "in": "query", "name": "role", "type": "string", "x-example": "duelist"}, {"description": "Comma-separated agents, for example jett,sage; the same 29 agents as vlr-stats", "in": "query", "name": "agent", "type": "string", "x-example": "jett"}, {"description": "Comma-separated map names, for example ascent,bind; the same 13 maps as vlr-stats", "in": "query", "name": "map", "type": "string", "x-example": "ascent"}, {"description": "Comma-separated stage ids from the stages list of vlr-event-matches", "in": "query", "name": "stage", "type": "string", "x-example": "6080"}, {"description": "Minimum rounds played; 0 to 100000", "in": "query", "maximum": 100000, "minimum": 0, "name": "min_rounds", "type": "integer"}, {"description": "Sort column, the same set as vlr-stats; defaults to rating", "in": "query", "name": "sort", "type": "string"}, {"description": "Sort direction; one of desc, asc; defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "dir", "type": "string"}], "path": "/vlr/event-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "agent", "type": "string"}, {"in": "query", "name": "map", "type": "string"}, {"in": "query", "name": "stage", "type": "string"}, {"in": "query", "name": "min_rounds", "type": "integer"}, {"in": "query", "name": "sort", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "dir", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-events": {"bodyParam": null, "bodyRequired": false, "id": "vlr-events", "method": "GET", "params": [{"description": "Event tier; one of all, vct, vcl, t3, gc, cg, off; defaults to all", "enum": ["all", "vct", "vcl", "t3", "gc", "cg", "off"], "in": "query", "name": "tier", "type": "string"}, {"description": "Event region; one of all, americas, emea, pacific, china; defaults to all", "enum": ["all", "americas", "emea", "pacific", "china"], "in": "query", "name": "region", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "vct", "vcl", "t3", "gc", "cg", "off"], "in": "query", "name": "tier", "type": "string"}, {"enum": ["all", "americas", "emea", "pacific", "china"], "in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-forum-categories": {"bodyParam": null, "bodyRequired": false, "id": "vlr-forum-categories", "method": "GET", "params": [], "path": "/vlr/forum-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "vlr-forum-threads": {"bodyParam": null, "bodyRequired": false, "id": "vlr-forum-threads", "method": "GET", "params": [{"description": "Forum category; one of valorant-discussion, off-topic, site-feedback; omit for the combined list", "enum": ["valorant-discussion", "off-topic", "site-feedback"], "in": "query", "name": "category", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}, {"description": "Order; one of hot, new, top; omit for the site default (recent activity)", "enum": ["hot", "new", "top"], "in": "query", "name": "sort", "type": "string"}], "path": "/vlr/forum-threads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["valorant-discussion", "off-topic", "site-feedback"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["hot", "new", "top"], "in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "777956"}], "path": "/vlr/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match-economy": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match-economy", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "754737"}], "path": "/vlr/match-economy", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match-performance": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match-performance", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "754737"}], "path": "/vlr/match-performance", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-match-rounds": {"bodyParam": null, "bodyRequired": false, "id": "vlr-match-rounds", "method": "GET", "params": [{"description": "Numeric VLR match id from vlr-matches, vlr-results or vlr-event-matches", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "754737"}], "path": "/vlr/match-rounds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-matches", "method": "GET", "params": [{"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-news": {"bodyParam": null, "bodyRequired": false, "id": "vlr-news", "method": "GET", "params": [{"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-news-article": {"bodyParam": null, "bodyRequired": false, "id": "vlr-news-article", "method": "GET", "params": [{"description": "Numeric VLR news article id from vlr-news", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "781119"}], "path": "/vlr/news-article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-player": {"bodyParam": null, "bodyRequired": false, "id": "vlr-player", "method": "GET", "params": [{"description": "Numeric VLR player id from vlr-team or vlr-stats", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9780"}, {"description": "Window of the agent statistics; one of all, 30d, 60d, 90d; omit for the site default", "enum": ["all", "30d", "60d", "90d"], "in": "query", "name": "timespan", "type": "string"}], "path": "/vlr/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["all", "30d", "60d", "90d"], "in": "query", "name": "timespan", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-player-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-player-matches", "method": "GET", "params": [{"description": "Numeric VLR player id from vlr-team or vlr-stats", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9780"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/player-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-rankings": {"bodyParam": null, "bodyRequired": false, "id": "vlr-rankings", "method": "GET", "params": [{"description": "Ranking region; one of north-america, europe, brazil, asia-pacific, korea, china, japan, la-s, la-n, oceania, mena, gc, collegiate; defaults to north-america", "enum": ["north-america", "europe", "brazil", "asia-pacific", "korea", "china", "japan", "la-s", "la-n", "oceania", "mena", "gc", "collegiate"], "in": "query", "name": "region", "type": "string"}, {"description": "Number of top teams to return, 1 to 250; defaults to 50", "in": "query", "maximum": 250, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/vlr/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["north-america", "europe", "brazil", "asia-pacific", "korea", "china", "japan", "la-s", "la-n", "oceania", "mena", "gc", "collegiate"], "in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-results": {"bodyParam": null, "bodyRequired": false, "id": "vlr-results", "method": "GET", "params": [{"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-search": {"bodyParam": null, "bodyRequired": false, "id": "vlr-search", "method": "GET", "params": [{"description": "Search text, 1 to 100 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "sentinels"}, {"description": "Result group; one of all, teams, events, players; defaults to all", "enum": ["all", "teams", "events", "players"], "in": "query", "name": "type", "type": "string"}], "path": "/vlr/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"enum": ["all", "teams", "events", "players"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-stats": {"bodyParam": null, "bodyRequired": false, "id": "vlr-stats", "method": "GET", "params": [{"description": "Comma-separated tiers from vct, vcl, t3, gc, cg, off; site default vct", "in": "query", "name": "tier", "type": "string"}, {"description": "Comma-separated regions from americas, emea, pacific, china, intl", "in": "query", "name": "region", "type": "string"}, {"description": "Timespan; one of all, 30d, 60d, 90d, 2026, 2025, 2024, 2023, 2022, 2021, 2020; site default 60d", "enum": ["all", "30d", "60d", "90d", "2026", "2025", "2024", "2023", "2022", "2021", "2020"], "in": "query", "name": "timespan", "type": "string"}, {"description": "Side; one of all, t, ct", "enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"description": "Comma-separated roles from controller, initiator, sentinel, duelist", "in": "query", "name": "role", "type": "string"}, {"description": "Comma-separated agents from astra, brimstone, clove, harbor, miks, omen, viper, breach, fade, gekko, kayo, skye, sova, tejo, chamber, cypher, deadlock, killjoy, sage, veto, vyse, iso, jett, neon, phoenix, raze, reyna, waylay, yoru", "in": "query", "name": "agent", "type": "string"}, {"description": "Comma-separated maps from abyss, bind, corrode, haven, lotus, summit, sunset, ascent, breeze, fracture, icebox, pearl, split", "in": "query", "name": "map", "type": "string"}, {"description": "Minimum rounds played; site default 100", "in": "query", "minimum": 0, "name": "min_rounds", "type": "integer"}, {"description": "First day of a custom date range, YYYY-MM-DD (UTC); requires to and replaces timespan", "in": "query", "name": "from", "type": "string", "x-example": "2026-09-01"}, {"description": "Last day of a custom date range, YYYY-MM-DD (UTC); requires from and replaces timespan", "in": "query", "name": "to", "type": "string", "x-example": "2026-10-01"}, {"description": "Minimum player rating; one of 0, 1300, 1400, 1500, 1550, 1650, 1750, 1850", "enum": [0, 1300, 1400, 1500, 1550, 1650, 1750, 1850], "in": "query", "name": "min_rating", "type": "integer"}, {"description": "Sort column; one of rating, maps, rnd, acs, kd, kast, adr, kpr, apr, fkfd, fkpr, fdpr, hsp, clp, cl, kmax, k, d, a, fk, fd; defaults to rating", "enum": ["rating", "maps", "rnd", "acs", "kd", "kast", "adr", "kpr", "apr", "fkfd", "fkpr", "fdpr", "hsp", "clp", "cl", "kmax", "k", "d", "a", "fk", "fd"], "in": "query", "name": "sort", "type": "string"}, {"description": "Sort direction; one of asc, desc; defaults to desc", "enum": ["asc", "desc"], "in": "query", "name": "dir", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}], "path": "/vlr/stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tier", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"enum": ["all", "30d", "60d", "90d", "2026", "2025", "2024", "2023", "2022", "2021", "2020"], "in": "query", "name": "timespan", "type": "string"}, {"enum": ["all", "t", "ct"], "in": "query", "name": "side", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "agent", "type": "string"}, {"in": "query", "name": "map", "type": "string"}, {"in": "query", "name": "min_rounds", "type": "integer"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}, {"enum": ["0", "1300", "1400", "1500", "1550", "1650", "1750", "1850"], "in": "query", "name": "min_rating", "type": "integer"}, {"enum": ["rating", "maps", "rnd", "acs", "kd", "kast", "adr", "kpr", "apr", "fkfd", "fkpr", "fdpr", "hsp", "clp", "cl", "kmax", "k", "d", "a", "fk", "fd"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "dir", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "vlr-team": {"bodyParam": null, "bodyRequired": false, "id": "vlr-team", "method": "GET", "params": [{"description": "Numeric VLR team id from vlr-rankings, vlr-event or vlr-match", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2059"}], "path": "/vlr/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-team-maps": {"bodyParam": null, "bodyRequired": false, "id": "vlr-team-maps", "method": "GET", "params": [{"description": "Numeric VLR team id from vlr-rankings, vlr-event or vlr-match", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2059"}], "path": "/vlr/team-maps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "vlr-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "vlr-team-matches", "method": "GET", "params": [{"description": "Numeric VLR team id from vlr-rankings, vlr-event or vlr-match", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2059"}, {"description": "1-based page number; defaults to 1", "in": "query", "maximum": 500, "minimum": 1, "name": "page", "type": "integer"}, {"description": "Match group; one of completed (default), upcoming", "enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "path": "/vlr/team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["completed", "upcoming"], "in": "query", "name": "group", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["vlr-event", "vlr-event-agents", "vlr-event-matches", "vlr-event-stats", "vlr-events", "vlr-forum-categories", "vlr-forum-threads", "vlr-match", "vlr-match-economy", "vlr-match-performance", "vlr-match-rounds", "vlr-matches", "vlr-news", "vlr-news-article", "vlr-player", "vlr-player-matches", "vlr-rankings", "vlr-results", "vlr-search", "vlr-stats", "vlr-team", "vlr-team-maps", "vlr-team-matches"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-vlr-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('event') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-event', params, response_type: response_type)
      end
      define_method('event_agents') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-event-agents', params, response_type: response_type)
      end
      define_method('event_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-event-matches', params, response_type: response_type)
      end
      define_method('event_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-event-stats', params, response_type: response_type)
      end
      define_method('events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-events', params, response_type: response_type)
      end
      define_method('forum_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-forum-categories', params, response_type: response_type)
      end
      define_method('forum_threads') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-forum-threads', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-match', params, response_type: response_type)
      end
      define_method('match_economy') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-match-economy', params, response_type: response_type)
      end
      define_method('match_performance') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-match-performance', params, response_type: response_type)
      end
      define_method('match_rounds') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-match-rounds', params, response_type: response_type)
      end
      define_method('matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-matches', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-news', params, response_type: response_type)
      end
      define_method('news_article') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-news-article', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-player', params, response_type: response_type)
      end
      define_method('player_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-player-matches', params, response_type: response_type)
      end
      define_method('rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-rankings', params, response_type: response_type)
      end
      define_method('results') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-results', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-search', params, response_type: response_type)
      end
      define_method('stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-stats', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-team', params, response_type: response_type)
      end
      define_method('team_maps') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-team-maps', params, response_type: response_type)
      end
      define_method('team_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('vlr-team-matches', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
