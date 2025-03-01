export async function mintlifyHandler(requestInfo){
    const payload = requestInfo.options.payload;
    payload["query"] = requestInfo.query;
    const headers = {
        "Content-Type": "application/json",
        Authorization: requestInfo.options.token,
        "TR-Dataset": requestInfo.options.dataset
    }

    console.log("URL", requestInfo.options.url);
    console.log("Payload", payload);
    console.log("Headers", headers);

    const data = await fetch(requestInfo.options.url, {
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