export async function algoliaHandler(requestInfo){
    let payload = requestInfo.options.payload;
    payload["query"] = requestInfo.query;

    if (payload.indexName){
        payload = {requests:[payload]}
    }

    console.log("payload", payload);

    const data = await fetch(requestInfo.options.url, {
        method: "POST",
        body: JSON.stringify(payload)
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
            }

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