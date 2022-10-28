import json
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from urllib.parse import urlsplit, urlunsplit
from tld import get_tld

from deta import Deta

import secrets

app = FastAPI()  # create app instance

deta = Deta()  # provide project key

db = deta.Base("gittaxi_links")  # create a DetaBase

cbdb = deta.Base("gittaxi_cb_1")  # create a DetaBase

require_allowed_domains = False

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

@app.post("/api/short")
async def shorten_url(url, token):
    if token == None:
        token = secrets.token_urlsafe(6)

    if require_allowed_domains == True:
        if cbdb.get(token) == None and db.get(token) == None:
            if get_tld(url, as_object=True).fld in allowed_domains:
                cbdb.insert(url, key=token)
                db.insert(url, key=token)
                return {"url": token, "allowed_url": "true"}
            else:
                return {"allowed_url": "false"}
        else:
            return {"success": "false"}
    else:
        cbdb.insert(url, key=token)
        db.insert(url, key=token)
        return {"url": token, "allowed_url": "true"}

@app.post("/api/delete")
async def delete_shorten_url(token):
    if cbdb.get(token) != None and db.get(token) != None:
        try:
            cbdb.delete(token)
            db.delete(token)
        except:
            return {"deleted": "false"}
        finally:
            return {"deleted": "true"}