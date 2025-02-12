export async function algoliaHandler(requestInfo){
    const payload = requestInfo.options.payload;
    payload["query"] = requestInfo.query;

    const data = await fetch(requestInfo.options.url, {
        method: "POST",
        body: JSON.stringify({requests:[payload]})
    }).then(v => v.json());
    const cache = {};

    for (let result of data.results){
        for (let hit of result.hits){
            const parts = [];
            for (let i = 0; i <= 6; i++) {
                const lvl = `lvl${i}`;
                if (hit.hierarchy[lvl] != null) {
                    parts.push(hit.hierarchy[lvl]);
                }
            }
            cache[parts.join(" - ")] = hit.url;
        };
    };

    return {
        version: "2.0",
        cache,
        name: requestInfo.options.name,
        favicon_url: requestInfo.options.favicon_url
    };
}