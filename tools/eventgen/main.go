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

func writeEventFile(contentType string, title string, urlSlug string) {
	filePath := fmt.Sprintf("./content/events/%s.md", urlSlug);
	eventFile, err := os.Create(filePath)
	checkError(err)

	defer eventFile.Close()

	frontMatterContent := generateFrontMatter(title, urlSlug)
	pageContent := getPageContent(contentType)
	fileContent := fmt.Sprintf("%s\n\n%s", frontMatterContent, pageContent)

	if _, err := eventFile.WriteString(fileContent); err != nil {
		panic(err)
	}
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
	ContentType string
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

func writeEventFiles(events []Event) string {
	event := events[0]
	writeEventFile(event.ContentType, event.Name, event.URLSlug)
	remainingEvents := events[1:]
	if len(remainingEvents) > 0 {
		return writeEventFiles(remainingEvents)
	}

	return "Event pages have been generated."
}

func main() {

	events := getEventData()
	result := writeEventFiles(events)

	fmt.Printf("%v\n", result)
}
