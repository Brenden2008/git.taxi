<center>
<h1> Git.taxi Powered By MiniShort </h1>

<p> A simple URL shortener in Python on Deta </p>
</center>

## NEW! Free Subdomains!
Git.taxi is now a part of the Code Domains Network! This means you can get free subdomains on git.taxi!
Sign up [here](https://github.com/RebootLabs-xyz/code-domains)!

## Technologies Used
- FastAPI
- Deta

## Dependencies
- FastAPI
- aiofiles
- jinja2

## How it works

You open the main site and enter your URL in the form. When you press submit, JavaScript takes care of making an asynchronous request to the underlying server which calls Deta Base to add the URL to the Base.
When you make a request to a short URL, it looks for that which matches in the database and responds with a `RedirectResponse` to the *target*

Live app [here](https://git.taxi)

<center>
<p> Live a star if you like this </p>
<p> Made by Brenden Stahle, Based on MiniShort </p>
<center>
