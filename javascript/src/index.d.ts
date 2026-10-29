import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class VLRClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  event(params: OperationParamsMap["vlr-event"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventAgents(params: OperationParamsMap["vlr-event-agents"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventMatches(params: OperationParamsMap["vlr-event-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventStats(params: OperationParamsMap["vlr-event-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  events(params?: OperationParamsMap["vlr-events"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  forumCategories(params?: OperationParamsMap["vlr-forum-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  forumThreads(params?: OperationParamsMap["vlr-forum-threads"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["vlr-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchEconomy(params: OperationParamsMap["vlr-match-economy"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchPerformance(params: OperationParamsMap["vlr-match-performance"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchRounds(params: OperationParamsMap["vlr-match-rounds"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matches(params?: OperationParamsMap["vlr-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params?: OperationParamsMap["vlr-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsArticle(params: OperationParamsMap["vlr-news-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["vlr-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerMatches(params: OperationParamsMap["vlr-player-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankings(params?: OperationParamsMap["vlr-rankings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  results(params?: OperationParamsMap["vlr-results"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["vlr-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  stats(params?: OperationParamsMap["vlr-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["vlr-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamMaps(params: OperationParamsMap["vlr-team-maps"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamMatches(params: OperationParamsMap["vlr-team-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  event(params: OperationParamsMap["vlr-event"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventAgents(params: OperationParamsMap["vlr-event-agents"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventMatches(params: OperationParamsMap["vlr-event-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventStats(params: OperationParamsMap["vlr-event-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  events(params?: OperationParamsMap["vlr-events"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  forumCategories(params?: OperationParamsMap["vlr-forum-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  forumThreads(params?: OperationParamsMap["vlr-forum-threads"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["vlr-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchEconomy(params: OperationParamsMap["vlr-match-economy"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchPerformance(params: OperationParamsMap["vlr-match-performance"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchRounds(params: OperationParamsMap["vlr-match-rounds"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matches(params?: OperationParamsMap["vlr-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params?: OperationParamsMap["vlr-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsArticle(params: OperationParamsMap["vlr-news-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["vlr-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerMatches(params: OperationParamsMap["vlr-player-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankings(params?: OperationParamsMap["vlr-rankings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  results(params?: OperationParamsMap["vlr-results"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["vlr-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  stats(params?: OperationParamsMap["vlr-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["vlr-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamMaps(params: OperationParamsMap["vlr-team-maps"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamMatches(params: OperationParamsMap["vlr-team-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  event(...args: OperationRequestArgs<"vlr-event">): Promise<OperationResponseMap["vlr-event"]>;
  eventAgents(...args: OperationRequestArgs<"vlr-event-agents">): Promise<OperationResponseMap["vlr-event-agents"]>;
  eventMatches(...args: OperationRequestArgs<"vlr-event-matches">): Promise<OperationResponseMap["vlr-event-matches"]>;
  eventStats(...args: OperationRequestArgs<"vlr-event-stats">): Promise<OperationResponseMap["vlr-event-stats"]>;
  events(...args: OperationRequestArgs<"vlr-events">): Promise<OperationResponseMap["vlr-events"]>;
  forumCategories(...args: OperationRequestArgs<"vlr-forum-categories">): Promise<OperationResponseMap["vlr-forum-categories"]>;
  forumThreads(...args: OperationRequestArgs<"vlr-forum-threads">): Promise<OperationResponseMap["vlr-forum-threads"]>;
  match(...args: OperationRequestArgs<"vlr-match">): Promise<OperationResponseMap["vlr-match"]>;
  matchEconomy(...args: OperationRequestArgs<"vlr-match-economy">): Promise<OperationResponseMap["vlr-match-economy"]>;
  matchPerformance(...args: OperationRequestArgs<"vlr-match-performance">): Promise<OperationResponseMap["vlr-match-performance"]>;
  matchRounds(...args: OperationRequestArgs<"vlr-match-rounds">): Promise<OperationResponseMap["vlr-match-rounds"]>;
  matches(...args: OperationRequestArgs<"vlr-matches">): Promise<OperationResponseMap["vlr-matches"]>;
  news(...args: OperationRequestArgs<"vlr-news">): Promise<OperationResponseMap["vlr-news"]>;
  newsArticle(...args: OperationRequestArgs<"vlr-news-article">): Promise<OperationResponseMap["vlr-news-article"]>;
  player(...args: OperationRequestArgs<"vlr-player">): Promise<OperationResponseMap["vlr-player"]>;
  playerMatches(...args: OperationRequestArgs<"vlr-player-matches">): Promise<OperationResponseMap["vlr-player-matches"]>;
  rankings(...args: OperationRequestArgs<"vlr-rankings">): Promise<OperationResponseMap["vlr-rankings"]>;
  results(...args: OperationRequestArgs<"vlr-results">): Promise<OperationResponseMap["vlr-results"]>;
  search(...args: OperationRequestArgs<"vlr-search">): Promise<OperationResponseMap["vlr-search"]>;
  stats(...args: OperationRequestArgs<"vlr-stats">): Promise<OperationResponseMap["vlr-stats"]>;
  team(...args: OperationRequestArgs<"vlr-team">): Promise<OperationResponseMap["vlr-team"]>;
  teamMaps(...args: OperationRequestArgs<"vlr-team-maps">): Promise<OperationResponseMap["vlr-team-maps"]>;
  teamMatches(...args: OperationRequestArgs<"vlr-team-matches">): Promise<OperationResponseMap["vlr-team-matches"]>;
}
export { VLRClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default VLRClient;
