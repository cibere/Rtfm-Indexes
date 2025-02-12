const base_url = "https://www.mathworks.com/help";
const favicon_url = "https://www.mathworks.com/favicon.ico";
const name = "mathworks.com";

export async function mathworksHandler(query){
    if (query == ""){
        return {"Mathwork Docs": base_url};
    }

    const data = await fetch(`${base_url}/search/suggest/doccenter/en/R2024b?selectedsource=mw&width=785.667&q=${query}`, {
        method: "GET",
        headers: {
            "User-Agent": "python-flow.launcher.plugin.rtfm/1.0.0"
        }
    }).then(v => v.json());
    const cache = {};

    for (let page of data.pages){
        for (let entry of page.suggestions){

            let text = `${entry.title.join("")} - ${entry.summary.join("")}`
            cache[text] = {
                text,
                url: `${base_url}/${entry.path}`,
                options: {
                    sub: `type: ${entry.type} | ${entry.product}`
                }
            };
        };
    };

    return {
        version: "2.0",
        cache,
        name,
        favicon_url,
    };
}