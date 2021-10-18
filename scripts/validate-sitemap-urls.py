from bs4 import BeautifulSoup
import requests
import gzip
import asyncio
import aiohttp

BASE_URL = "https://www.pulumi.com"
PULUMI_COM_LEN = len(BASE_URL)

errorMessages = []

async def crawler(locs):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[load_url_from_loc(loc, session) for loc in locs])

    if len(errorMessages) == 0:
        print("No sitemap regressions found!")
        exit(0)
    else:
        print("\n\nError: Found " + str(len(errorMessages)) + " sitemap regressions:\n\n")
        print("\n".join(errorMessages))
        exit(1)

def getURLFromTag(loc):
    return "https://www-reg-staging.pulumi-dev.io" + loc.text[PULUMI_COM_LEN:]

async def load_url_from_loc(loc, session):
    url = getURLFromTag(loc)
    print("Analyzing page: " + url)
    try:
        async with session.get(url=url, timeout=5000) as response:
            resp = await response.read()
            if (response.status != 200):
                message = "{ URL: \"" + url + ", StatusCode: " + str(response.status) + " }"
                errorMessages.append(message)

    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))

html = requests.get("https://www.pulumi.com/sitemap.xml")
sitemap = BeautifulSoup(html.text, features="html.parser")
locs = sitemap.findAll('loc', text=True)
asyncio.run(crawler(locs))
