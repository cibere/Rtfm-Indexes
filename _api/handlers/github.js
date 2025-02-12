const base_url = "https://docs.github.com";
const favicon_url = "https://github.com/favicon.ico"
const name = "github.com"

async function process(query){
    if (query == ""){
        return {"Github Docs": base_url};
    }

    var res = await fetch(`${base_url}/api/search/v1?query=${query}`, {
        "method": "GET",
    });
    console.log("gh resp", res);
    var data = await res.json();

    console.log("got github response", data);

    var cache = {};

    for (let hit of data.hits){
        console.log("serializing hit", hit);

        cache[hit.title] = {
            "text": `${hit.title} / ${hit.breadcrumbs}`,
            url: `${base_url}${hit.url}`,
            options: {
                sub: hit.highlights.content[0]
            }
        }
    }

    return {
        version: "2.0",
        cache,
        name,
        favicon_url,
    }
}

export const githubHandler = process