package main

import (
	"bufio"
	"bytes"
	"flag"
	"fmt"
	"github.com/golang/glog"
	"github.com/pkg/errors"
	"os"
	"path/filepath"
	"strings"
)

const frontMatterSeparator = "---"

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) < 2 {
		fmt.Fprintf(os.Stderr, "error: usage: %s <old-dir> <new-dir>\n", os.Args[0])
		os.Exit(1)
	}

	defer glog.Flush()

	oldPath, newPath := args[0], args[1]

	redirectPrefix := strings.ReplaceAll(oldPath, "../../themes/default/content", "")
	if err := addAliases(newPath, redirectPrefix); err != nil {
		glog.Fatalf("Failed to add aliases for content under the new path (%s): %v", newPath, err)
	}
}

func addAliases(rootDir, redirectPrefix string) error {
	globPattern := filepath.Join(rootDir, "**", "index.md")
	matches, err := filepath.Glob(globPattern)
	// If err is non-nil, the only possible error is filepath.ErrBadPattern
	// according to the docs for Glob().
	if err != nil {
		return err
	}

	for _, m := range matches {
		fi, err := os.Stat(m)
		if err != nil {
			return errors.Wrapf(err, "reading file (%s) info", m)
		}
		parts := strings.Split(m, rootDir)
		nameWithoutExt := strings.ReplaceAll(parts[1], "/"+fi.Name(), "")

		file, err := os.Open(m)
		if err != nil {
			return errors.Wrapf(err, "opening file %s", m)
		}

		bufsize := 1024 * 1024
		buf := make([]byte, bufsize)

		scanner := bufio.NewScanner(file)
		// Necessary so we can handle larger than default 4096b buffer
		scanner.Buffer(buf, bufsize)

		// optionally, resize scanner's capacity for lines over 64K, see next example
		found := false

		var bodyBytes []byte
		body := bytes.NewBuffer(bodyBytes)

		var fmBytes []byte
		fm := bytes.NewBuffer(fmBytes)
		finishedReadingFrontMatter := false
		updatedExistingAliases := false
		for scanner.Scan() {
			t := scanner.Text()
			if !found && t == frontMatterSeparator {
				found = true
			} else if found && t == frontMatterSeparator {
				finishedReadingFrontMatter = true
				// If we didn't find an existing aliases key,
				// then write a new one.
				if !updatedExistingAliases {
					fm.WriteString("\naliases:\n")
					fm.WriteString("  - " + redirectPrefix + nameWithoutExt)
				}
			} else if !finishedReadingFrontMatter {
				if t == "aliases:" {
					fm.WriteString("\n" + t + "\n")
					fm.WriteString("  - " + redirectPrefix + nameWithoutExt)
					updatedExistingAliases = true
					continue
				}
				fm.WriteString("\n")
				fm.WriteString(t)
			} else {
				body.WriteString(t)
				body.WriteString("\n")
			}
		}

		newContents := "---" + fm.String() + "\n---\n" + body.String()
		if err := os.WriteFile(m, []byte(newContents), fi.Mode()); err != nil {
			return errors.Wrapf(err, "writing updated markdown contents for %s", m)
		}
	}

	return nil
}
