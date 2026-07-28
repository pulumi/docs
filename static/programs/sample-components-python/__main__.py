import pulumi
from static_website import StaticWebsite, StaticWebsiteArgs

page_html = "<h1>I love Pulumi!</h1>"
page = StaticWebsite(
    "my-static-website",
    StaticWebsiteArgs(index_content=page_html)
)

website_url = page.endpoint.apply(lambda v: f"http://{v}")
pulumi.export("websiteURL", website_url)
