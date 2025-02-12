const base_url = "https://docs.github.com";

export async function githubHandler(request){
    const query = request.query;

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
                sub: decodeURIComponent(hit.highlights.content[0]
                    .replaceAll("\n", "")
                    .replaceAll("<mark>", "")
                    .replaceAll("</mark>", "")),
            }
        };
    };

    return cache;
};