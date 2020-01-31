package main

import(
	"fmt"
	"io/ioutil"
	"os"

	"github.com/BurntSushi/toml"
)

func checkError(e error) {
	if e != nil {
		panic(e)
	}
}

func generateFrontMatter(title string, urlSlug string) string {
	frontMatter := fmt.Sprintf(`
---
title: %s
url: %s
type: page
layout: event-single
---
	`, title, urlSlug)

	return frontMatter
}

func getPageContent(contentType string) string {
	var text string
	switch contentType {
	case "workshop":
		content, err := ioutil.ReadFile("./tools/eventgen/snippets/workshop.md")
		checkError(err)

		text = string(content)
	default:
		errMsg := fmt.Sprintf("Content Type %s is not supported", contentType)
		panic(errMsg)
	}

	return text
}

func writeEventFile(contentType string, title string, urlSlug string) int {
	filePath := fmt.Sprintf("./content/events/%s.md", urlSlug);
	eventFile, err := os.Create(filePath)
	checkError(err)

	defer eventFile.Close()

	frontMatterContent := generateFrontMatter(title, urlSlug)
	pageContent := getPageContent(contentType)
	fileContent := fmt.Sprintf("%s\n\n%s", frontMatterContent, pageContent)

	r, err := eventFile.WriteString(fileContent)
	checkError(err)

	return r
}

type Event struct {
	Type []string
	Name string
	Location string
	StartDate string
	EndDate string
	Description string
	RegistrationURL string
	URLSlug string
}

type Events struct {
	Events []Event
}

func getEventData() []Event {
	var eventData Events
	filePath := "./data/events.toml"

	if _, err := toml.DecodeFile(filePath, &eventData); err != nil {
		panic(err)
	}

	return eventData.Events
}

func main() {

	test := getEventData()

	fmt.Printf("%v\n", test)
}
