const base_url = "https://www.mathworks.com/help";

export async function mathworksHandler(request){
    const query = request.query;

    if (query == ""){
        let text = "Mathwork Docs";
        return {text: {text, url: base_url}};
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
        version: "2.1",
        cache,
    };
}