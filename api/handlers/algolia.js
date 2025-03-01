const resultTitleFallbackKeys = ["title", "pageTitle", "mainTitle", "page_title"];
const resultHrefKeys = ["url", "objectID", "slug"];

function getAnyKeyFromList(obj, keys){
    for (let key of keys){
        try {
            let item = obj[key];
            if (item != null){
                return item;
            };
        } catch {};
    };
}

function getLabel(hit){
    let label = getAnyKeyFromList(hit, resultTitleFallbackKeys);

    if (!label){
        const parts = [];
        for (let i = 0; i <= 6; i++) {
            const lvl = `lvl${i}`;
            try {
                if (hit.hierarchy[lvl] != null) {
                    parts.push(hit.hierarchy[lvl]);
                }
            } catch {};
        };
        label = parts.join(" - ");
    }
    if (!label){
        const parts = [];
        for (let i = 1; i <= 5; i++) {
            const key = `h${i}`;
            try {
                if (hit[key] != null) {
                    parts.push(hit[key]);
                }
            } catch {};
        };
        label = parts.join(" - ");
    }

    return label;
}

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
            let options = {};

            let excerpt	= hit.excerpt;
            if (excerpt	!= null) {
                options["sub"] = excerpt;
            };
            
            let href = getAnyKeyFromList(hit, resultHrefKeys);
            let text = getLabel(hit);

            cache[text] = {
                text,
                url: href,
                options,
            };
        };
    };

    return cache;
}