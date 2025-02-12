import {githubHandler} from "./handlers/github.js";
import {mathworksHandler} from "./handlers/mathworks.js";

const handlers = {
  "/github": githubHandler,
  "/mathworks": mathworksHandler,
}

export default {
    async fetch(request, env, ctx) {
      const url = new URL(request.url);
      console.log("URL", url);
      
      var handler = handlers[url.pathname];

      if (handler == undefined){
        return new Response("API handler not found", {"status": 404});
      }
      console.log("got handler", handler)

      let query = url.searchParams.get("q")
      var data = await handler(query ? query : "");

      console.log("got data", data);
      return new Response(JSON.stringify(data));
    },
  };