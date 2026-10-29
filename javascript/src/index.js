import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class VLRClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-vlr-js/0.1.0" });
    this["event"] = (...args) => this.request("vlr-event", ...args);
    this["eventAgents"] = (...args) => this.request("vlr-event-agents", ...args);
    this["eventMatches"] = (...args) => this.request("vlr-event-matches", ...args);
    this["eventStats"] = (...args) => this.request("vlr-event-stats", ...args);
    this["events"] = (...args) => this.request("vlr-events", ...args);
    this["forumCategories"] = (...args) => this.request("vlr-forum-categories", ...args);
    this["forumThreads"] = (...args) => this.request("vlr-forum-threads", ...args);
    this["match"] = (...args) => this.request("vlr-match", ...args);
    this["matchEconomy"] = (...args) => this.request("vlr-match-economy", ...args);
    this["matchPerformance"] = (...args) => this.request("vlr-match-performance", ...args);
    this["matchRounds"] = (...args) => this.request("vlr-match-rounds", ...args);
    this["matches"] = (...args) => this.request("vlr-matches", ...args);
    this["news"] = (...args) => this.request("vlr-news", ...args);
    this["newsArticle"] = (...args) => this.request("vlr-news-article", ...args);
    this["player"] = (...args) => this.request("vlr-player", ...args);
    this["playerMatches"] = (...args) => this.request("vlr-player-matches", ...args);
    this["rankings"] = (...args) => this.request("vlr-rankings", ...args);
    this["results"] = (...args) => this.request("vlr-results", ...args);
    this["search"] = (...args) => this.request("vlr-search", ...args);
    this["stats"] = (...args) => this.request("vlr-stats", ...args);
    this["team"] = (...args) => this.request("vlr-team", ...args);
    this["teamMaps"] = (...args) => this.request("vlr-team-maps", ...args);
    this["teamMatches"] = (...args) => this.request("vlr-team-matches", ...args);
  }
}

export { VLRClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default VLRClient;
