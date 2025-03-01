export async function androidHandler(requestInfo){
    const url = "https://developer.android.com/_d/search/suggestions?" + new URLSearchParams({
        r: [requestInfo.query, null,null,null,null,1,1,1,1]
    }).toString();

    const data = await fetch(url, {
        method: "POST",
        body: JSON.stringify(payload),
        headers,
    }).then(v => v.json());
    const cache = {};

    console.log("data received", data);

    for (let entry of data.score_chunks){
        let metadata = entry.metadata[0]
        cache[metadata.metadata.title] = {
            text: metadata.metadata.breadcrumbs.join(" - "),
            url: `${payload.base_url}${metadata.link}`,
            options: {
                sub: entry.highlights[0]
                    .replaceAll("<mark>", "")
                    .replaceAll("</mark>", "")
                    .replaceAll("<b>", "")
                    .replaceAll("</b>", ""),
            }
        };
    };

    return cache;
}