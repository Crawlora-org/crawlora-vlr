import { VLRClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new VLRClient({ apiKey });

  const matches = await client.matches({  });
  console.log("matches", matches);
  const events = await client.events({  });
  console.log("events", events);
