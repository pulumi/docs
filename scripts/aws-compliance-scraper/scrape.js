// Script to scrape the compliance controls from the AWS security hub pages, to populate
// the list on compliance pages. This reads the /data/compliance/pages.json file and
// retrieves a list of all the services and then loads the page from aws for that
// service to scrape the compliance controls.

const fs = require("fs");
const cheerio = require("cheerio");
const axios = require('axios');


async function fetchAndLoad(url) {
  try {
    const response = await axios.get(url);
    const html = response.data;
    return cheerio.load(html);
  } catch (error) {
    console.error('Error fetching the webpage:', url);
  }
}

function removePrefix(input) {
    return input.replace(/^\[.*?\]\s*/, '');
}

function cleanString(input) {
    return input.replace(/\n\s+/g, ' ').trim();
}

async function parse(service) {
    const url = `https://docs.aws.amazon.com/securityhub/latest/userguide/${service}-controls.html`;
    console.log(url);
    const $ = await fetchAndLoad(url);

    const results = [];

    const frameworks = $("h2");
    frameworks.each((i, elm) => {
        const h2Text = $(elm).text();

      const nextElement = $(elm).next('p');
      if (nextElement.length > 0) {
        const pText = nextElement.text(); 

        results.push({ requirement: h2Text, frameworks: pText });
      }
    });
    
    return results.map(r => removePrefix(r.requirement)).map(r => cleanString(r));
}

function loadServices() {
    const contents = fs.readFileSync("./data/compliance/pages.json", {
        encoding: "utf8",
    });
    const complianceFrameworks = JSON.parse(contents);
    return complianceFrameworks.services.filter(svc => svc.cloud === "AWS").map(svc => svc.name)
}

async function getControls() {
    const services = loadServices();
    const result = {}

    for (let svc of services) {
        console.log(svc);
        result[svc] = await parse(svc.replace(" ", "").toLowerCase())
    }

    console.log("file written to /data/compliance/controls.json");
    fs.writeFileSync("./data/compliance/controls.json", JSON.stringify(result, null, 2));
}

getControls();