import { VLRClient } from "../src/index.js";

const client = new VLRClient({ apiKey: "test-key" });
void client.event({"id": "sample"});
void client.request("vlr-event", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("vlr-event", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("vlr-event", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.event({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("vlr-event", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("vlr-event", {"id": "sample"}, { responseType: "text" });
void rawText;


void client.events();
void client.request("vlr-events");
// @ts-expect-error The selected operation requires its documented params.
void client.event();
