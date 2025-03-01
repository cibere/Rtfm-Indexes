import {githubHandler} from "./handlers/github.js";
import {mathworksHandler} from "./handlers/mathworks.js";
import {algoliaHandler} from "./handlers/algolia.js";
import {mintlifyHandler} from "./handlers/mintlifytrieve.js"

const handlers = {
  "/github": githubHandler,
  "/mathworks": mathworksHandler,
  "/algolia": algoliaHandler,
  "/mintlify": mintlifyHandler,
}

export default {
  async fetch(request, env, ctx) {
    if (request.method !== "POST"){
      return new Response(JSON.stringify({"error": "Invalid Method Received"}), {"status": 400});
    };

    const url = new URL(request.url);
    const body = await request.json();
    const handler = handlers[url.pathname];

    if (handler == null){
      return new Response(JSON.stringify({"error": "API handler not found"}), {"status": 404});
    }

    const data = await handler(body);

    console.log("returning data", data);
    return new Response(JSON.stringify({
      version: "2.1",
      cache: data,
      type: "cache-index",
      name: url.pathname,
      favicon_url: null,
    }));
  },
};