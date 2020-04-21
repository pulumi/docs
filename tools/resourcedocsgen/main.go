// Copyright 2016-2020, Pulumi Corporation.
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
	"encoding/json"
	"flag"
	"fmt"
	"github.com/pulumi/pulumi/pkg/v2/codegen/dotnet"
	go_gen "github.com/pulumi/pulumi/pkg/v2/codegen/go"
	"github.com/pulumi/pulumi/pkg/v2/codegen/nodejs"
	"io/ioutil"
	"os"
	"path"

	"github.com/golang/glog"
	"github.com/pkg/errors"

	docsgen "github.com/pulumi/pulumi/pkg/v2/codegen/docs"
	pschema "github.com/pulumi/pulumi/pkg/v2/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v2/go/common/tools"
	"github.com/pulumi/pulumi/sdk/v2/go/common/util/contract"
)

func main() {
	// Grab the args.
	flag.Parse()
	args := flag.Args()
	if len(args) < 2 {
		fmt.Fprintf(os.Stderr, "error: usage: %s <out-dir> <provider-schema-file> [overlay-schema-file]>\n", os.Args[0])
		os.Exit(1)
	}

	defer glog.Flush()

	outDir, schemaFile, overlaysSchemaFile := args[0], args[1], args[2]

	schema, err := ioutil.ReadFile(schemaFile)
	if err != nil {
		glog.Infof("error reading schema file from path: %v", err)
		os.Exit(1)
	}

	mainSpec := &pschema.PackageSpec{}
	if err := json.Unmarshal(schema, mainSpec); err != nil {
		glog.Infof("error unmarshalling schema into a PackageSpec: %v", err)
		os.Exit(1)
	}

	if overlaysSchemaFile != "" {
		overlaySpec := &pschema.PackageSpec{}
		overlaysSchema, err := ioutil.ReadFile(overlaysSchemaFile)
		if err != nil {
			glog.Infof("error reading overlay schema file from path: %v", err)
			os.Exit(1)
		}
		if err := json.Unmarshal(overlaysSchema, overlaySpec); err != nil {
			glog.Infof("error unmarshalling overlay schema into a PackageSpec: %v", err)
			os.Exit(1)
		}

		mergeOverlaySchemaSpec(mainSpec, overlaySpec)
	}

	if err := generateDocsFromSchema(outDir, mainSpec); err != nil {
		glog.Infof("error generating docs from schema: %v", err)
		os.Exit(1)
	}
}

// mergeOverlaySchemaSpec merges the resources, types and language info from the overlay schema spec
// into the main package spec.
func mergeOverlaySchemaSpec(mainSpec *pschema.PackageSpec, overlaySpec *pschema.PackageSpec) error {
	// Merge the overlay schema spec into the main schema spec.
	for key, value := range overlaySpec.Types {
		if _, ok := mainSpec.Types[key]; ok {
			glog.Infoln(key, "was skipped because it was already in the main schema spec")
			continue
		}
		mainSpec.Types[key] = value
	}
	for key, value := range overlaySpec.Resources {
		if _, ok := mainSpec.Resources[key]; ok {
			glog.Infoln(key, "was skipped because it was already in the main schema spec")
			continue
		}
		mainSpec.Resources[key] = value
	}
	for lang, overlayLanguageInfo := range overlaySpec.Language {
		switch lang {
		case "go":
			var mainSchemaPkgInfo go_gen.GoPackageInfo
			if err := json.Unmarshal(mainSpec.Language[lang], &mainSchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling Go package info from the main schema spec")
			}

			var overlaySchemaPkgInfo go_gen.GoPackageInfo
			if err := json.Unmarshal(overlayLanguageInfo, &overlaySchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling Go package info from the overlay schema spec")
			}

			for key, value := range overlaySchemaPkgInfo.ModuleToPackage {
				if _, ok := mainSchemaPkgInfo.ModuleToPackage[key]; ok {
					glog.Infoln("Go ModuleToPackage key", key, "was skipped because it was already in the main schema's language info")
					continue
				}
				mainSchemaPkgInfo.ModuleToPackage[key] = value
			}

			// Override the language info for Go in the main schema spec.
			b, err := json.Marshal(mainSchemaPkgInfo)
			if err != nil {
				return errors.Wrap(err, "error marshalling Go package info")
			}
			mainSpec.Language[lang] = json.RawMessage(string(b))
		case "nodejs":
			var mainSchemaPkgInfo nodejs.NodePackageInfo
			if err := json.Unmarshal(mainSpec.Language[lang], &mainSchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling NodeJS package info from the main schema spec")
			}

			var overlaySchemaPkgInfo nodejs.NodePackageInfo
			if err := json.Unmarshal(overlayLanguageInfo, &overlaySchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling NodeJS package info from the overlay schema spec")
			}

			for key, value := range overlaySchemaPkgInfo.ModuleToPackage {
				if _, ok := mainSchemaPkgInfo.ModuleToPackage[key]; ok {
					glog.Infoln("NodeJS ModuleToPackage key", key, "was skipped because it was already in the main schema's language info")
					continue
				}
				mainSchemaPkgInfo.ModuleToPackage[key] = value
			}

			// Override the language info for NodeJS in the main schema spec.
			b, err := json.Marshal(mainSchemaPkgInfo)
			if err != nil {
				return errors.Wrap(err, "error marshalling NodeJS package info")
			}
			mainSpec.Language[lang] = json.RawMessage(string(b))
		case "csharp":
			var mainSchemaPkgInfo dotnet.CSharpPackageInfo
			if err := json.Unmarshal(mainSpec.Language[lang], &mainSchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling C# package info from the main schema spec")
			}

			var overlaySchemaPkgInfo dotnet.CSharpPackageInfo
			if err := json.Unmarshal(overlayLanguageInfo, &overlaySchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling C# package info from overlay schema spec")
			}

			for key, value := range overlaySchemaPkgInfo.Namespaces {
				if _, ok := mainSchemaPkgInfo.Namespaces[key]; ok {
					glog.Infoln("C# Namespaces key", key, "was skipped because it was already in the main schema's language info")
					continue
				}
				mainSchemaPkgInfo.Namespaces[key] = value
			}
			// Override the language info for C# in the main schema spec.
			b, err := json.Marshal(mainSchemaPkgInfo)
			if err != nil {
				return errors.Wrap(err, "error marshalling C# package info")
			}
			mainSpec.Language[lang] = json.RawMessage(string(b))
		}
	}

	return nil
}

func generateDocsFromSchema(outDir string, spec *pschema.PackageSpec) error {
	pulPkg, err := pschema.ImportSpec(*spec, nil)
	if err != nil {
		return errors.Wrapf(err, "error importing package spec: %v", err)
	}

	files, err := docsgen.GeneratePackage("Pulumi Docs Generator", pulPkg)
	if err != nil {
		return errors.Wrap(err, "generating Pulumi package")
	}

	for f, contents := range files {
		if err := emitFile(outDir, f, contents); err != nil {
			return errors.Wrapf(err, "emitting file %v", f)
		}
	}
	return nil
}

func emitFile(outDir, relPath string, contents []byte) error {
	p := path.Join(outDir, relPath)
	if err := tools.EnsureDir(path.Dir(p)); err != nil {
		return errors.Wrap(err, "creating directory")
	}

	f, err := os.Create(p)
	if err != nil {
		return errors.Wrap(err, "creating file")
	}
	defer contract.IgnoreClose(f)

	_, err = f.Write(contents)
	return err
}
