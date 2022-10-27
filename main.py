import json
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from urllib.parse import urlsplit, urlunsplit

from deta import Deta

import secrets

app = FastAPI()  # create app instance

deta = Deta("")  # provide project key

db = deta.Base("gittaxi_links")  # create a DetaBase

allowed_domains = [
    "github.io",
    "github.com",
    "githubapp.com",
    "githubusercontent.com",
    "githubassets.com",
    "git.io",
    "gitlab.com",
    "gitlab.io",
    "codeberg.page",
    "codeberg.org",
]

def is_root(url):
    head, sep, tail = url.partition('//')
    is_root_domain = tail.split('/', 1)[0] if '/' in tail else url
    # printing or returning is_root_domain will give you what you seek
    print(is_root_domain)

app.mount("/static", StaticFiles(directory="static"), name="static")

pages = Jinja2Templates(directory="pages")


@app.get("/")
async def get_home(request: Request):
    return pages.TemplateResponse("index.html", {"request": request})


@app.post("/shorten")
async def shorten_url(url):
    if is_root(url) in allowed_domains:
        # data = jsonable_encoder(url)
        token = secrets.token_urlsafe(6)
        db.put(url, key=token)
        return {"url": token, "allowed_url": "true"}
    else:
        return {"allowed_url": "false"}


@app.get("/{url}")
async def redirect_to_(url):
    red_ = db.get(url)
    print(red_)
    return RedirectResponse(red_["value"])
