
const formEl = document.getElementById("form");

function createAndAppendUrl(url, shortUrl) {

    // create elementss
    let span = document.createElement("span");
    let p1 = document.createElement("a");
    let p2 = document.createElement("p");

    // set element text values
    p1.innerText = shortUrl;
    p2.innerText = url;

    // set element href values
    p1.href = shortUrl;
    //p2.href = url;

    // add a as child of span
    span.appendChild(p2);
    span.appendChild(p1);

    // add style class to span
    span.classList.add("short");

    // get parent URLs container
    const urlsContainer = document.getElementById("shorts");

    urlsContainer.appendChild(span);
}

function createAndAppendText(text) {

    // create elements
    let span = document.createElement("span");
    let p1 = document.createElement("p");

    // set element text values
    p1.innerHTML = text;

    // add a as child of span
    span.appendChild(p1);

    // add style class to span
    span.classList.add("short");

    // get parent URLs container
    const urlsContainer = document.getElementById("shorts");

    urlsContainer.appendChild(span);
}

async function shortenUrl(url) {
    let res = await fetch(`shorten?url=${url}`, {method: "POST"});
    let data = await res.json();

    if(data.allowed_url == "true"){
        createAndAppendUrl(url, `${location.href}${data.url}`);
    } else {
        createAndAppendText(`
            This is not an allowed domain. You can see the list of allowed domains <a href="/static/allowed_domains.txt">here</a>.
        `)
    }
}

formEl.addEventListener("submit", (event) => {
    event.preventDefault();

    let inputUrl = document.getElementById("inputUrl").value;

    shortenUrl(inputUrl);
})