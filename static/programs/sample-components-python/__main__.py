import pulumi
from static_page import StaticPage, StaticPageArgs

page_html = "<h1>I love Pulumi!</h1>"
page = StaticPage(
    "my-static-page",
    StaticPageArgs(index_content=page_html)
)

website_url = page.endpoint.apply(lambda v: f"http://{v}")
pulumi.export("websiteURL", website_url)
