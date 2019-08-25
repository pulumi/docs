// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"fmt"

	"github.com/cbroglie/mustache"
	"github.com/gobuffalo/packr"
)

var (
	templates = packr.NewBox("./templates")

	cloudIndexTemplate  = parseTemplate("cloud_index.tmpl")
	globalIndexTemplate = parseTemplate("global_index.tmpl")
	tutorialTemplate    = parseTemplate("tutorial.tmpl")
)

func parseTemplate(name string) *mustache.Template {
	tstr, err := templates.FindString(name)
	if err != nil {
		panic(fmt.Sprintf("missing templates/%s template: %v", name, err))
	}

	t, err := mustache.ParseString(tstr)
	if err != nil {
		panic(fmt.Sprintf("error parsing templates/%s template: %v", name, err))
	}

	return t
}
