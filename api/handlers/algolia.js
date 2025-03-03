const resultTitleFallbackKeys = ["title", "pageTitle", "mainTitle", "page_title"];
const resultHrefKeys = ["url", "path", "objectID", "slug"];

String.prototype.formatUnicorn = String.prototype.formatUnicorn ||
function () {
    "use strict";
    var str = this.toString();
    if (arguments.length) {
        var t = typeof arguments[0];
        var key;
        var args = ("string" === t || "number" === t) ?
            Array.prototype.slice.call(arguments)
            : arguments[0];

        for (key in args) {
            str = str.replace(new RegExp("\\{" + key + "\\}", "gi"), args[key]);
        }
    }

    return str;
};

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
        label = parts.reverse().join(" - ");
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

function getHashicorpUrl(hit){
    const path = hit.url_path;

    if (path){
        return `https://developer.hashicorp.com/${path}`;
    }
    let url = hit.external_url;
    if (url){
        return url
    }

    let obj = hit.objectID;
    let product = hit.products[0];
    let href = obj.replace(`${hit.type}_${product}`, product);
    return `https://developer.hashicorp.com/${href}`;
}

export async function algoliaHandler(requestInfo){
    const base_url = requestInfo.options.base_url ? requestInfo.options.base_url : ""

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
            console.log("dealing with hit", hit);
            let options = {};

            let excerpt	= hit.excerpt;
            if (excerpt	!= null) {
                options["sub"] = excerpt;
            };
            
            let url

            if (requestInfo.options.is_hashicorp){
                url = getHashicorpUrl(hit);
            } else {
                if (requestInfo.options.url_template) {
                    url = requestInfo.options.url_template.formatUnicorn(
                        {
                            class: hit.class,
                            name: hit.name,
                        }
                    )
                } else {
                    url = `${base_url}${getAnyKeyFromList(hit, resultHrefKeys)}`
                }
            }
            let text = getLabel(hit);

            cache[text] = {
                text,
                url,
                options,
            };
        };
    };

    return cache;
}