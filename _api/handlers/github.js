const base_url = "https://docs.github.com";
const favicon_url = "https://github.com/favicon.ico";
const name = "github.com";

export async function githubHandler(query){
    if (query == ""){
        return {"Github Docs": base_url};
    }

    const data = await fetch(`${base_url}/api/search/v1?query=${query}`, {
        "method": "GET",
    }).then(v => v.json());
    const cache = {};

    for (let hit of data.hits){
        console.log("serializing hit", hit);

        cache[hit.title] = {
            "text": `${hit.title} / ${hit.breadcrumbs}`,
            url: `${base_url}${hit.url}`,
            options: {
                sub: hit.highlights.content[0],
            }
        };
    };

    return {
        version: "2.0",
        cache,
        name,
        favicon_url,
    };
};