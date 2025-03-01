const resultTitleFallbackKeys = ["title", "pageTitle", "mainTitle"];

export async function algoliaHandler(requestInfo){
    let payload

    if (requestInfo.options.payload){
        payload = requestInfo.options.payload;
        payload["query"] = requestInfo.query;
    
        if (payload.indexName){
            payload = {requests:[payload]};
        };
    } else {
        payload = {requests:requestInfo.options.payloads};
        for (let req of payload.requests){
            req.query = requestInfo.query;
        };
    }

    let headers = requestInfo.options.headers ? requestInfo.options.headers : {};

    console.log("payload", payload);
    console.log("headers", headers);

    const data = await fetch(requestInfo.options.url, {
        method: "POST",
        body: JSON.stringify(payload),
        headers
    }).then(v => v.json());
    const cache = {};

    console.log("recieved response", data);

    for (let result of (data.results ? data.results : [data])){
        for (let hit of result.hits){
            // console.log("dealing with hit", hit);
            const parts = [];
            for (let i = 0; i <= 6; i++) {
                const lvl = `lvl${i}`;
                try {
                    if (hit.hierarchy[lvl] != null) {
                        parts.push(hit.hierarchy[lvl]);
                    }
                } catch {};
            }
            
            let text = parts.join(" - ");
            if (text == "") {
                text = hit.title
                for (let key of resultTitleFallbackKeys){
                    try {
                        text = hit[key];
                        if (text){
                            break;
                        };
                    } catch {};
                };
            };

            let options = {}

            let excerpt	= hit.excerpt;
            if (excerpt	!= null) {
                options["sub"] = excerpt
            }

            let href = hit.url
            if (href == null) {
                href = hit.slug
            }
            
            cache[text] = {
                text,
                url: href,
                options
            };
        };
    };

    return cache;
}