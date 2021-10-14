from bs4 import BeautifulSoup
import requests
import gzip

BASE_URL = "https://www.pulumi.com"
PULUMI_COM_LEN = len(BASE_URL)

errorMessages = []

def crawler():
    scannedCount = 0
    html = requests.get("https://www.pulumi.com/sitemap.xml")
    sitemap = BeautifulSoup(html.text, features="html.parser")
    locs = sitemap.findAll('loc', text=True)
    
    for loc in locs:
        url = getURLFromTag(loc)
        print("Analyzing page: " + url)

        response = requests.get(url, allow_redirects=True)
        
        if (response.status_code != 200):
            errorMessages.append("URL: \"" url + ", Status code: " + response.status_code )

    if len(errorMessages) == 0:
        print("No sitemap regressions found")
        exit(0)
    else:
        print("Found " + len(errorMessages) + " sitemap regressions:")
        print(errorMessages)
        exit(1)

def getURLFromTag(loc):
    "https://www-reg-staging.pulumi-dev.io" + loc.text[PULUMI_COM_LEN:]

crawler()