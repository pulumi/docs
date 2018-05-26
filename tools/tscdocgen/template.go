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
	"github.com/cbroglie/mustache"
)

var indexTemplate, _ = mustache.ParseString(`---
title: {{Title}}
---

{{#Breadcrumbs}}{{{.}}}{{/Breadcrumbs}}
{{#Package}}
Node.js:

` + "```" + `javascript
var {{PackageVar}} = require("{{Package}}");
` + "```" + `

ES6 modules:

` + "```" + `typescript
import * as {{PackageVar}} from "{{Package}}";
` + "```" + `
{{/Package}}

{{#HasMembers}}
<h2 class="pdoc-module-header">Index</h2>

{{#Members}}
* <a href="#{{Name}}">{{Label}}</a>
{{/Members}}

{{#Files}}<a href="{{RepoURL}}/{{.}}">{{.}}</a> {{/Files}}
{{/HasMembers}}

{{#HasModules}}
<h2 class="pdoc-module-header">Modules</h2>

{{#Modules}}
* <a href="{{Link}}">{{Name}}</a>
{{/Modules}}
{{/HasModules}}

{{#Members}}
<h2 class="pdoc-module-header" id="{{Name}}">
<a class="pdoc-member-name" href="{{RepoURL}}">{{{Label}}}</a>
</h2>
{{#DetailedLabel}}

` + "```typescript" + `
{{{DetailedLabel}}}
` + "```" + `

{{/DetailedLabel}}
{{#Comment.ShortText}}

{{{Comment.ShortText}}}

{{#Comment.Text}}
{{{Comment.Text}}}
{{/Comment.Text}}
{{/Comment.ShortText}}
{{#Children}}
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="{{RepoURL}}">{{{Label}}}</a>
</h3>
{{#DetailedLabel}}

` + "```typescript" + `
{{{DetailedLabel}}}
` + "```" + `

{{/DetailedLabel}}
{{#Signatures}}

` + "```typescript" + `
{{{Label}}}
` + "```" + `

{{#Comment.ShortText}}

{{{Comment.ShortText}}}

{{#Comment.Text}}
{{{Comment.Text}}}
{{/Comment.Text}}
{{/Comment.ShortText}}
{{#Parameters}}
{{#Comment.ShortText}}
* ` + "`{{Name}}`" + ` {{Comment.ShortText}}
{{/Comment.ShortText}}
{{/Parameters}}
{{/Signatures}}
{{^Signatures}}
{{#Comment.ShortText}}

{{{Comment.ShortText}}}

{{#Comment.Text}}
{{{Comment.Text}}}
{{/Comment.Text}}
{{/Comment.ShortText}}
{{/Signatures}}
{{/Children}}
{{#Signatures}}

` + "```typescript" + `
{{{Label}}}
` + "```" + `

{{#Comment.ShortText}}

{{{Comment.ShortText}}}

{{#Comment.Text}}
{{{Comment.Text}}}
{{/Comment.Text}}
{{/Comment.ShortText}}
{{#Parameters}}
{{#Comment.ShortText}}
* ` + "`{{Name}}`" + ` {{Comment.ShortText}}
{{/Comment.ShortText}}
{{/Parameters}}
{{/Signatures}}
{{/Members}}
`)
