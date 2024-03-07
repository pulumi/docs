import pulumi

web_server = pulumi.Output.from_input({
    "hostName": "www.mywebserver.com",
    "port": "8080",
});

# concat takes a list of args and concatenates all of them into a single output:
url1 = pulumi.Output.concat("http://", web_server.hostName, ":", web_server.port, "/")

# format takes a template string and a list of args or keyword args and formats the string, expanding outputs correctly:
url2 = pulumi.Output.format("http://{0}:{1}/", web_server.hostName, web_server.port);

pulumi.export("serverUrl1", url1)
pulumi.export("serverUrl2", url2)