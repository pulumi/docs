// Copyright 2025, Pulumi Corporation.  All rights reserved.

//go:build ignore

// This script analyzes feature flags and updates the self-hosted feature parity
// summary document with current availability status while preserving ETAs.

package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"sort"
	"strings"
)

type FeatureInfo struct {
	Key                 string
	FriendlyName        string
	Available           bool
	Default             bool
	HasCustomPrecond    bool     // Has customPrecondition function
	CustomPrecondName   string   // Name of the precondition function (e.g., "config.IsOpenAIConfigured")
	FeatureDependencies []string // List of feature keys this depends on
	FeatureFlagKey      string   // LaunchDarkly flag key (if any)
	LaunchDarklyOnly    bool     // Gated only by a LaunchDarkly flag checked directly in code, with no features.go entry

	LaunchDarklyChecks    []ldCheck // Direct LaunchDarkly checks of this flag outside features.go
	DirectLaunchDarklyOff bool      // A direct check defaults to false, so it's off on self-hosted
}

type MarketingFeature struct {
	InternalKey   string
	MarketingName string
	ETA           string
	Notes         string
	Summary       string // Internal description of the feature on self-hosted
	Status        string // "Y", "N", "Y (has toggle)", "Y (needs config)"
	History       string // Git history: PR link and related issues
}

type FeatureMetadata struct {
	MarketingName  string   `json:"marketing_name"`
	DefaultETA     string   `json:"default_eta"`
	Notes          string   `json:"notes"`
	Summary        string   `json:"summary,omitempty"`      // Internal description shown in the summary table
	Status         string   `json:"status,omitempty"`       // Overrides the computed status (for example, "Y (needs config)")
	DependsOn      []string `json:"depends_on,omitempty"`   // Extra dependencies not declared in features.go (for example, Neo sub-features)
	FeatureKeys    []string `json:"feature_keys,omitempty"` // Optional: multiple feature flags mapping to one entry
	IncludeInTable *bool    `json:"include_in_table"`       // Whether to show in summary table (default true)
	Gate           string   `json:"gate,omitempty"`         // For hand-maintained rows with no flag: what controls the feature (for example, "none (configuration only)")
}

type FeatureConfig struct {
	Features map[string]FeatureMetadata `json:"features"` // Key is marketing name or feature key
}

type PublishConfig struct {
	MarketingName string `json:"marketing_name"`
	Publish       bool   `json:"publish"`
	PublicName    string `json:"public_name,omitempty"`  // Name shown on the public page (defaults to marketing_name)
	DocsURL       string `json:"docs_url,omitempty"`     // Docs page that explains the feature
	PublicNotes   string `json:"public_notes,omitempty"` // Friendly explanation shown in the Notes section of the public page
}

type FeaturePublishConfig struct {
	Features map[string]PublishConfig `json:"features"` // Key is marketing name
}

// metadataPath is the feature metadata in the pulumi-service clone, set in main.
// It lives in pulumi-service, not here, because it names internal flags and
// unreleased features.
var metadataPath string

func loadFeatureConfig() *FeatureConfig {
	data, err := os.ReadFile(metadataPath)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading feature metadata: %v\n", err)
		fmt.Fprintf(os.Stderr, "Hint: the pulumi-service checkout may predate %s. It reaches the production branch, which the nightly workflow reads, with the next pulumi-service release; locally, pull the branch you're generating from.\n", metadataFile)
		os.Exit(1)
	}

	var config FeatureConfig
	if err := json.Unmarshal(data, &config); err != nil {
		fmt.Fprintf(os.Stderr, "Error parsing %s: %v\n", metadataPath, err)
		os.Exit(1)
	}

	return &config
}

func loadPublishConfig() *FeaturePublishConfig {
	data, err := os.ReadFile(publishConfigFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading publish config: %v\n", err)
		os.Exit(1)
	}

	var config FeaturePublishConfig
	if err := json.Unmarshal(data, &config); err != nil {
		fmt.Fprintf(os.Stderr, "Error parsing %s: %v\n", publishConfigFile, err)
		os.Exit(1)
	}

	return &config
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s [--all | --generate-raw | --update-summary | --enrich | --publish | --full-report]\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  --all:            Run every step below in order (what make generate-feature-parity runs)\n")
		fmt.Fprintf(os.Stderr, "  --generate-raw:   Generate raw feature data from features.go\n")
		fmt.Fprintf(os.Stderr, "  --update-summary: Generate internal summary from raw data + config\n")
		fmt.Fprintf(os.Stderr, "  --enrich:         Enrich internal summary with git history (skipped without the gh CLI)\n")
		fmt.Fprintf(os.Stderr, "  --publish:        Generate public feature-parity.md from internal summary\n")
		fmt.Fprintf(os.Stderr, "  --full-report:    Generate full feature comparison report\n")
		fmt.Fprintf(os.Stderr, "\nRun from the repo root.\n")
		fmt.Fprintf(os.Stderr, "\nEnvironment:\n")
		fmt.Fprintf(os.Stderr, "  PULUMI_SERVICE_REPO: Path to pulumi-service repo (default: ../pulumi-service)\n")
		os.Exit(1)
	}

	mode := os.Args[1]

	// Like the other doc generators, read a sibling clone that scripts/update_repos.sh manages
	servicePath := os.Getenv("PULUMI_SERVICE_REPO")
	if servicePath == "" {
		servicePath = "../pulumi-service"
	}

	if _, err := os.Stat(filepath.Join(servicePath, featuresFile)); err != nil {
		if mode == "--all" {
			// Most people building docs can't access pulumi-service; keep the existing page
			fmt.Printf("Skipping feature parity generation: no pulumi-service clone at %s.\n", servicePath)
			fmt.Println("If you have access, clone it with ./scripts/update_repos.sh pulumi-service or set PULUMI_SERVICE_REPO.")
			return
		}
		fmt.Fprintf(os.Stderr, "Error: %s not found in %s. Clone pulumi-service with ./scripts/update_repos.sh pulumi-service or set PULUMI_SERVICE_REPO.\n", featuresFile, servicePath)
		os.Exit(1)
	}

	metadataPath = filepath.Join(servicePath, metadataFile)

	if err := os.MkdirAll(generatedDir, 0755); err != nil {
		fmt.Fprintf(os.Stderr, "Error creating %s: %v\n", generatedDir, err)
		os.Exit(1)
	}

	// Parse features.go to get current status
	features := parseFeatures(servicePath)
	addLaunchDarklyOnlyFeatures(servicePath, features)

	switch mode {
	case "--all":
		generateRawDoc(features)
		updateInternalSummaryDoc(features)
		enrichInternalSummaryWithGitHistory(servicePath)
		generatePublicDoc(features)
	case "--generate-raw":
		generateRawDoc(features)
	case "--update-summary":
		updateInternalSummaryDoc(features)
	case "--enrich":
		enrichInternalSummaryWithGitHistory(servicePath)
	case "--publish":
		generatePublicDoc(features)
	case "--full-report":
		generateFullReport(features)
	default:
		fmt.Fprintf(os.Stderr, "Unknown mode: %s\n", mode)
		os.Exit(1)
	}
}

const (
	featuresFile      = "cmd/service/api/features/features.go"
	metadataFile      = "cmd/service/api/features/self-hosted-parity.json"
	publishConfigFile = "scripts/self-hosted-feature-parity/feature-publish-config.json"
	generatedDir      = "scripts/self-hosted-feature-parity/generated"
)

func parseFeatures(servicePath string) map[string]*FeatureInfo {
	fset := token.NewFileSet()

	featuresPath := filepath.Join(servicePath, featuresFile)
	node, err := parser.ParseFile(fset, featuresPath, nil, parser.ParseComments)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error parsing features.go at %s: %v\n", featuresPath, err)
		fmt.Fprintf(os.Stderr, "Hint: Set PULUMI_SERVICE_REPO env var to location of pulumi-service repo\n")
		os.Exit(1)
	}

	features := make(map[string]*FeatureInfo)

	ast.Inspect(node, func(n ast.Node) bool {
		if assign, ok := n.(*ast.ValueSpec); ok {
			if len(assign.Names) > 0 && assign.Names[0].Name == "pulumiFeaturesByKey" {
				if comp, ok := assign.Values[0].(*ast.CompositeLit); ok {
					parseFeatureMap(comp, features)
				}
			}
		}
		return true
	})

	if len(features) == 0 {
		fmt.Fprintf(os.Stderr, "Error: no features found in %s; has pulumiFeaturesByKey moved?\n", featuresPath)
		os.Exit(1)
	}

	return features
}

func parseFeatureMap(comp *ast.CompositeLit, features map[string]*FeatureInfo) {
	for _, elt := range comp.Elts {
		if kv, ok := elt.(*ast.KeyValueExpr); ok {
			var featureKey string

			// Get the key - handle both old format (apitype.PulumiFeatureXxx) and new format (PulumiFeatureXxx)
			switch key := kv.Key.(type) {
			case *ast.SelectorExpr:
				// Old format: apitype.PulumiFeatureXxx
				featureKey = key.Sel.Name
			case *ast.Ident:
				// New format: PulumiFeatureXxx (direct identifier)
				featureKey = key.Name
			}

			// Skip if we couldn't extract a key
			if featureKey == "" {
				continue
			}

			// Parse the value
			if comp2, ok := kv.Value.(*ast.CompositeLit); ok {
				feature := &FeatureInfo{Key: featureKey}
				parseFeatureDetails(comp2, feature)
				features[featureKey] = feature
			}
		}
	}
}

func parseFeatureDetails(comp *ast.CompositeLit, feature *FeatureInfo) {
	for _, elt := range comp.Elts {
		if kv, ok := elt.(*ast.KeyValueExpr); ok {
			if ident, ok := kv.Key.(*ast.Ident); ok {
				switch ident.Name {
				case "PulumiFeatureDetails":
					// Old format: wrapped in PulumiFeatureDetails
					if comp2, ok := kv.Value.(*ast.CompositeLit); ok {
						parsePulumiFeatureDetails(comp2, feature)
					}
				case "FriendlyName":
					// New format: FriendlyName directly in PulumiFeature
					if lit, ok := kv.Value.(*ast.BasicLit); ok {
						feature.FriendlyName = strings.Trim(lit.Value, `"`)
					}
				case "SelfHosted":
					// New/old format: SelfHosted preferences
					if comp2, ok := kv.Value.(*ast.CompositeLit); ok {
						parseSelfHostedPreferences(comp2, feature)
					}
				case "customPrecondition":
					feature.HasCustomPrecond = true
					// Try to extract the function name
					feature.CustomPrecondName = extractExprString(kv.Value)
				case "featureDependencies":
					feature.FeatureDependencies = extractFeatureDependencies(kv.Value)
				case "featureFlagKey":
					// Extract LaunchDarkly key
					feature.FeatureFlagKey = extractExprString(kv.Value)
				}
			}
		}
	}
}

func parsePulumiFeatureDetails(comp *ast.CompositeLit, feature *FeatureInfo) {
	for _, elt := range comp.Elts {
		if kv, ok := elt.(*ast.KeyValueExpr); ok {
			if ident, ok := kv.Key.(*ast.Ident); ok {
				switch ident.Name {
				case "FriendlyName":
					if lit, ok := kv.Value.(*ast.BasicLit); ok {
						feature.FriendlyName = strings.Trim(lit.Value, `"`)
					}
				case "SelfHosted":
					if comp2, ok := kv.Value.(*ast.CompositeLit); ok {
						parseSelfHostedPreferences(comp2, feature)
					}
				}
			}
		}
	}
}

func parseSelfHostedPreferences(comp *ast.CompositeLit, feature *FeatureInfo) {
	for _, elt := range comp.Elts {
		if kv, ok := elt.(*ast.KeyValueExpr); ok {
			if ident, ok := kv.Key.(*ast.Ident); ok {
				if id, ok := kv.Value.(*ast.Ident); ok {
					switch ident.Name {
					case "Available":
						feature.Available = (id.Name == "true")
					case "Default":
						feature.Default = (id.Name == "true")
					}
				}
			}
		}
	}
}

// extractExprString attempts to convert an expression to a readable string
func extractExprString(expr ast.Expr) string {
	switch v := expr.(type) {
	case *ast.SelectorExpr:
		// e.g., config.IsOpenAIConfigured or featureflag.LDKeyXxx
		if x, ok := v.X.(*ast.Ident); ok {
			return x.Name + "." + v.Sel.Name
		}
		return v.Sel.Name
	case *ast.Ident:
		return v.Name
	case *ast.BasicLit:
		return strings.Trim(v.Value, `"`)
	default:
		return ""
	}
}

// extractFeatureDependencies parses the featureDependencies array
func extractFeatureDependencies(expr ast.Expr) []string {
	var deps []string

	if comp, ok := expr.(*ast.CompositeLit); ok {
		for _, elt := range comp.Elts {
			if sel, ok := elt.(*ast.SelectorExpr); ok {
				// e.g., apitype.PulumiFeatureResourceSearch
				deps = append(deps, sel.Sel.Name)
			}
		}
	}

	return deps
}

func generateRawDoc(features map[string]*FeatureInfo) {
	rawPath := "scripts/self-hosted-feature-parity/generated/feature-detection-raw.md"

	// Generate raw content directly from features.go
	content := generateRawContent(features)

	// Write to file
	err := os.WriteFile(rawPath, []byte(content), 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error writing raw doc: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Generated %s (raw feature data from features.go)\n", rawPath)
}

func generateRawContent(features map[string]*FeatureInfo) string {
	var sb strings.Builder

	sb.WriteString("# Self Hosted Feature Parity - Raw Data\n\n")
	sb.WriteString("This document contains the raw, unfiltered feature availability data parsed directly from `cmd/service/api/features/features.go`.\n\n")
	sb.WriteString("**Note:** This is auto-generated. Do not edit manually. For the marketing-friendly summary, see `feature-parity.md`.\n\n")
	sb.WriteString("## Understanding the Columns\n\n")
	sb.WriteString("- **Feature Key**: Internal constant name (e.g., `PulumiFeatureDeployments`)\n")
	sb.WriteString("- **Friendly Name**: Human-readable name from code\n")
	sb.WriteString("- **Self Hosted?**: Whether feature CAN be available in self-hosted (`Y`/`N`)\n")
	sb.WriteString("- **Default On?**: Whether feature is enabled by default (`Y`/`N`)\n")
	sb.WriteString("- **Precondition**: Custom runtime requirement (e.g., OpenAI configured)\n")
	sb.WriteString("- **Dependencies**: Other features that must be enabled first\n")
	sb.WriteString("- **LD Flag**: LaunchDarkly feature flag key (if any)\n\n")
	sb.WriteString("**Important**: A feature marked `Y` for Self Hosted may still require:\n")
	sb.WriteString("1. Preconditions to be met (e.g., AI features need OpenAI API configured)\n")
	sb.WriteString("2. Dependent features to be enabled\n")
	sb.WriteString("3. License toggles or explicit configuration\n\n")

	sb.WriteString("| Feature Key | Friendly Name | Self Hosted? | Default On? | Precondition | Dependencies | LD Flag |\n")
	sb.WriteString("| :---- | :---- | :---- | :---- | :---- | :---- | :---- |\n")

	// Sort features by key for consistency
	keys := make([]string, 0, len(features))
	var ldOnlyKeys []string
	for k, f := range features {
		if f.LaunchDarklyOnly {
			ldOnlyKeys = append(ldOnlyKeys, k)
			continue
		}
		keys = append(keys, k)
	}
	sort.Strings(keys)
	sort.Strings(ldOnlyKeys)

	for _, key := range keys {
		f := features[key]

		var selfHosted string
		if f.Available {
			selfHosted = "Y"
		} else {
			selfHosted = "N"
		}

		var defaultOn string
		if f.Default {
			defaultOn = "Y"
		} else {
			defaultOn = "N"
		}

		precond := ""
		if f.HasCustomPrecond {
			precond = f.CustomPrecondName
		}

		deps := ""
		if len(f.FeatureDependencies) > 0 {
			deps = strings.Join(f.FeatureDependencies, ", ")
		}

		ldFlag := f.FeatureFlagKey

		sb.WriteString(fmt.Sprintf("| %s | %s | %s | %s | %s | %s | %s |\n",
			f.Key, f.FriendlyName, selfHosted, defaultOn, precond, deps, ldFlag))
	}

	sb.WriteString("\n## Direct LaunchDarkly checks\n\n")
	sb.WriteString("These LaunchDarkly flags are checked directly in pulumi-service code, outside features.go. ")
	sb.WriteString("Self-hosted can't reach LaunchDarkly, so each check returns its default: a `false` default turns the gated behavior off whatever the license says, ")
	sb.WriteString("and a `true` default leaves it on. Making an off flag available on self-hosted needs a license key in features.go.\n\n")
	sb.WriteString("A flag that a features.go entry already uses marks that entry as off. Any other flag shows in the internal summary once its key is added to `self-hosted-parity.json` in pulumi-service; ")
	sb.WriteString("set `include_in_table: false` for operational and rollout flags that aren't product features.\n\n")
	sb.WriteString("| LD Key | Flag | Default | Self Hosted | Applies to | Checked at |\n")
	sb.WriteString("| :---- | :---- | :---- | :---- | :---- | :---- |\n")
	config := loadFeatureConfig()
	var checked []*FeatureInfo
	for _, f := range features {
		if len(f.LaunchDarklyChecks) > 0 {
			checked = append(checked, f)
		}
	}
	sort.Slice(checked, func(i, j int) bool {
		return strings.TrimPrefix(checked[i].FeatureFlagKey, "featureflag.") < strings.TrimPrefix(checked[j].FeatureFlagKey, "featureflag.")
	})
	for _, f := range checked {
		key := strings.TrimPrefix(f.FeatureFlagKey, "featureflag.")
		var defaults, locations []string
		seen := make(map[string]bool)
		for _, c := range f.LaunchDarklyChecks {
			if !seen[c.defaultValue] {
				seen[c.defaultValue] = true
				defaults = append(defaults, c.defaultValue)
			}
			locations = append(locations, c.location)
		}
		status := "On"
		if f.DirectLaunchDarklyOff {
			status = "Off"
		} else if !seen["true"] {
			status = "Non-boolean"
		}

		appliesTo := f.Key
		if f.LaunchDarklyOnly {
			appliesTo = "**Not mapped**"
			if metadata, ok := config.Features[key]; ok {
				appliesTo = metadata.MarketingName
				if metadata.IncludeInTable != nil && !*metadata.IncludeInTable {
					appliesTo = "Excluded"
				}
			}
			for _, metadata := range config.Features {
				for _, fk := range metadata.FeatureKeys {
					if fk == key {
						appliesTo = metadata.MarketingName
					}
				}
			}
		}
		name := f.FriendlyName
		if !f.LaunchDarklyOnly {
			name = key
		}
		sb.WriteString(fmt.Sprintf("| %s | %s | %s | %s | %s | %s |\n",
			key, name, strings.Join(defaults, ", "), status, appliesTo, strings.Join(locations, "<br>")))
	}

	sb.WriteString("\n")

	return sb.String()
}

var ldKeyDefinition = regexp.MustCompile(`(?m)^\s*(LDKey[A-Za-z0-9]+)\s+LDKey\s*=\s*"([^"]+)"`)

// ldCheckMethods are the LaunchDarkly client methods that read a flag. Most default to false;
// the rest take the default as their last argument.
var ldCheckMethods = map[string]bool{
	"CheckFlagEnabledForOrgID":               true,
	"CheckFlagEnabledForOrgIDByID":           true,
	"CheckFlagEnabledForOrgSubscription":     true,
	"DeprecatedCheckLaunchDarklyFlag":        true,
	"DeprecatedCheckLaunchDarklyFlagByOrgID": true,
	"GetFlagIntValueForOrg":                  true,
	"GetFlagStringValueForOrgByID":           true,
}

var ldMethodsWithDefaultArg = map[string]bool{
	"DeprecatedCheckLaunchDarklyFlagByOrgID": true,
	"GetFlagIntValueForOrg":                  true,
	"GetFlagStringValueForOrgByID":           true,
}

// pkgFlagFuncs are the pkg/featureflags functions that read a flag. Each takes (ctx, key, default)
// and reads the same offline client, so on self-hosted they return the default too.
var pkgFlagFuncs = map[string]bool{
	"Enabled":             true,
	"EnabledWithDuration": true,
	"EnabledWithFloat":    true,
	"EnabledWithInt":      true,
	"EnabledWithString":   true,
}

// ldCheck is a flag read found in pulumi-service code, with the value it returns on self-hosted.
type ldCheck struct {
	defaultValue string // What the offline client returns: "false", "true", or a non-boolean default
	location     string // File and line of the check
}

// addLaunchDarklyOnlyFeatures finds LaunchDarkly flags that pulumi-service checks directly in
// code. Self-hosted can't reach LaunchDarkly, so each check returns its default. A check that
// defaults to false turns the gated behavior off on self-hosted, whatever the license says.
// Flags with no features.go entry are added as features; flags that a features.go entry
// already uses mark that entry as off.
func addLaunchDarklyOnlyFeatures(servicePath string, features map[string]*FeatureInfo) {
	flagDir := filepath.Join(servicePath, "cmd/service/services/featureflag")
	data, err := os.ReadFile(filepath.Join(flagDir, "launch_darkly.go"))
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading LaunchDarkly keys: %v\n", err)
		os.Exit(1)
	}
	// pkg/featureflags defines a second set of keys, read with featureflags.Enabled and its variants
	if pkgData, err := os.ReadFile(filepath.Join(servicePath, "pkg/featureflags/flags.go")); err == nil {
		data = append(append(data, '\n'), pkgData...)
	} else {
		fmt.Fprintf(os.Stderr, "Error reading pkg/featureflags keys: %v\n", err)
		os.Exit(1)
	}
	flagValues := make(map[string]string) // LDKey constant -> flag name
	keysByValue := make(map[string]string)
	for _, m := range ldKeyDefinition.FindAllStringSubmatch(string(data), -1) {
		flagValues[m[1]] = m[2]
		keysByValue[m[2]] = m[1]
	}

	// Service-wide helpers such as TFModulesRegistryEnabled() wrap getBool(key, context, default)
	helpers := parseLaunchDarklyHelpers(filepath.Join(flagDir, "flags.go"))
	if len(flagValues) == 0 || len(helpers) == 0 {
		// A layout change upstream would otherwise silently drop every direct check
		fmt.Fprintf(os.Stderr, "Error: found %d LaunchDarkly keys and %d helpers in %s; has the featureflag package moved?\n", len(flagValues), len(helpers), flagDir)
		os.Exit(1)
	}

	flagKey := func(expr ast.Expr) string {
		switch v := expr.(type) {
		case *ast.SelectorExpr:
			if strings.HasPrefix(v.Sel.Name, "LDKey") {
				return v.Sel.Name
			}
		case *ast.Ident:
			if strings.HasPrefix(v.Name, "LDKey") {
				return v.Name
			}
		case *ast.BasicLit:
			value := strings.Trim(v.Value, `"`)
			if key, ok := keysByValue[value]; ok {
				return key
			}
			return value
		}
		return ""
	}

	checks := make(map[string][]ldCheck)
	parseFailures := 0
	fset := token.NewFileSet()
	for _, dir := range []string{"cmd", "pkg"} {
		filepath.WalkDir(filepath.Join(servicePath, dir), func(path string, d os.DirEntry, err error) error {
			if err != nil {
				return nil
			}
			if d.IsDir() {
				switch d.Name() {
				// features is where license-gated flags are evaluated; featureflag and featureflags define the clients
				case "featureflag", "featureflags", "features", "mocks", "node_modules", "vendor", "testdata":
					return filepath.SkipDir
				}
				return nil
			}
			if !strings.HasSuffix(path, ".go") || strings.HasSuffix(path, "_test.go") {
				return nil
			}
			file, err := parser.ParseFile(fset, path, nil, 0)
			if err != nil {
				// Counted, not named: paths in pulumi-service can name unreleased features, and CI logs are public
				parseFailures++
				return nil
			}
			ast.Inspect(file, func(n ast.Node) bool {
				call, ok := n.(*ast.CallExpr)
				if !ok {
					return true
				}
				sel, ok := call.Fun.(*ast.SelectorExpr)
				if !ok {
					return true
				}
				pos := fset.Position(call.Pos())
				rel, _ := filepath.Rel(servicePath, pos.Filename)
				location := fmt.Sprintf("%s:%d", rel, pos.Line)

				if helper, ok := helpers[sel.Sel.Name]; ok && len(call.Args) == 0 {
					checks[helper.key] = append(checks[helper.key], ldCheck{defaultValue: helper.defaultValue, location: location})
					return true
				}
				if pkg, ok := sel.X.(*ast.Ident); ok && pkg.Name == "featureflags" && pkgFlagFuncs[sel.Sel.Name] {
					if len(call.Args) == 3 {
						if key := flagKey(call.Args[1]); key != "" {
							checks[key] = append(checks[key], ldCheck{defaultValue: selfHostedValue(call.Args[2]), location: location})
						}
					}
					return true
				}
				if !ldCheckMethods[sel.Sel.Name] {
					return true
				}
				// The flag is the second argument, or the third for CheckFlagEnabledForOrgSubscription
				flagArg := 1
				if sel.Sel.Name == "CheckFlagEnabledForOrgSubscription" {
					flagArg = 2
				}
				if len(call.Args) <= flagArg {
					return true
				}
				key := flagKey(call.Args[flagArg])
				if key == "" {
					return true
				}
				defaultValue := "false"
				if ldMethodsWithDefaultArg[sel.Sel.Name] && len(call.Args) > 0 {
					defaultValue = exprSource(call.Args[len(call.Args)-1])
				}
				checks[key] = append(checks[key], ldCheck{defaultValue: defaultValue, location: location})
				return true
			})
			return nil
		})
	}
	if parseFailures > 0 {
		fmt.Fprintf(os.Stderr, "Error: %d Go files in pulumi-service failed to parse, so their LaunchDarkly checks would be missed\n", parseFailures)
		os.Exit(1)
	}

	// Flags already attached to a features.go entry
	featureByFlag := make(map[string]*FeatureInfo)
	for _, f := range features {
		if f.FeatureFlagKey != "" {
			// features.go names the flag either by its LDKey constant or by its string value
			key := strings.TrimPrefix(f.FeatureFlagKey, "featureflag.")
			if constant, ok := keysByValue[key]; ok {
				key = constant
			}
			featureByFlag[key] = f
		}
	}

	for key, found := range checks {
		off := false
		for _, c := range found {
			if c.defaultValue == "false" {
				off = true
			}
		}
		if f, ok := featureByFlag[key]; ok {
			f.LaunchDarklyChecks = found
			f.DirectLaunchDarklyOff = off
			continue
		}
		name := flagValues[key]
		if name == "" {
			name = key
		}
		features[key] = &FeatureInfo{
			Key:                   key,
			FriendlyName:          name,
			Available:             !off,
			Default:               !off,
			FeatureFlagKey:        key,
			LaunchDarklyOnly:      true,
			LaunchDarklyChecks:    found,
			DirectLaunchDarklyOff: off,
		}
	}
}

type ldHelper struct {
	key          string
	defaultValue string
}

// parseLaunchDarklyHelpers maps each no-argument helper in flags.go to the flag it reads and its default.
func parseLaunchDarklyHelpers(path string) map[string]ldHelper {
	helpers := make(map[string]ldHelper)
	file, err := parser.ParseFile(token.NewFileSet(), path, nil, 0)
	if err != nil {
		return helpers
	}
	for _, decl := range file.Decls {
		fn, ok := decl.(*ast.FuncDecl)
		if !ok || fn.Recv == nil || fn.Body == nil || fn.Type.Params.NumFields() != 0 {
			continue
		}
		ast.Inspect(fn.Body, func(n ast.Node) bool {
			call, ok := n.(*ast.CallExpr)
			if !ok {
				return true
			}
			if sel, ok := call.Fun.(*ast.SelectorExpr); ok && strings.HasPrefix(sel.Sel.Name, "get") && len(call.Args) == 3 {
				if key, ok := call.Args[0].(*ast.Ident); ok && strings.HasPrefix(key.Name, "LDKey") {
					helpers[fn.Name.Name] = ldHelper{key: key.Name, defaultValue: exprSource(call.Args[2])}
				}
			}
			return true
		})
	}
	return helpers
}

// selfHostedValue resolves a default that depends on the deployment, such as
// enterpriseConfig.IsSelfHostedEnterprise(), to what it returns on self-hosted.
func selfHostedValue(expr ast.Expr) string {
	if call, ok := expr.(*ast.CallExpr); ok {
		if sel, ok := call.Fun.(*ast.SelectorExpr); ok && sel.Sel.Name == "IsSelfHostedEnterprise" {
			return "true"
		}
	}
	return exprSource(expr)
}

func exprSource(expr ast.Expr) string {
	switch v := expr.(type) {
	case *ast.Ident:
		return v.Name
	case *ast.BasicLit:
		return v.Value
	}
	return "(expression)"
}

func updateInternalSummaryDoc(features map[string]*FeatureInfo) {
	summaryPath := "scripts/self-hosted-feature-parity/generated/feature-parity-internal.md"

	// Read existing summary to preserve ETAs
	existingFeatures := parseExistingSummary(summaryPath)

	// Map known features
	marketingFeatures := buildMarketingFeatures(features, existingFeatures)

	// Generate updated content
	content := generateInternalSummaryContent(marketingFeatures)

	// Write to file
	err := os.WriteFile(summaryPath, []byte(content), 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error writing internal summary: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Updated %s\n", summaryPath)
}

func parseExistingSummary(path string) map[string]*MarketingFeature {
	existing := make(map[string]*MarketingFeature)

	file, err := os.Open(path)
	if err != nil {
		// File doesn't exist yet, return empty map
		return existing
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	inTable := false

	for scanner.Scan() {
		line := scanner.Text()

		// Detect table start
		if strings.HasPrefix(line, "| Feature") {
			inTable = true
			continue
		}

		// Skip separator line
		if strings.HasPrefix(line, "| :----") || strings.HasPrefix(line, "|------") {
			continue
		}

		// Parse table row
		if inTable && strings.HasPrefix(line, "| ") {
			parts := strings.Split(line, "|")
			if len(parts) >= 4 {
				featureName := strings.TrimSpace(parts[1])
				status := strings.TrimSpace(parts[2])
				eta := strings.TrimSpace(parts[3])

				existing[featureName] = &MarketingFeature{
					MarketingName: featureName,
					Status:        status,
					ETA:           eta,
				}
			}
		}

		// End of table
		if inTable && !strings.HasPrefix(line, "| ") && line != "" {
			break
		}
	}

	return existing
}

func buildMarketingFeatures(features map[string]*FeatureInfo, existing map[string]*MarketingFeature) []*MarketingFeature {
	// Load feature metadata from JSON config (optional)
	config := loadFeatureConfig()

	result := []*MarketingFeature{}

	// Build lookup: feature key -> metadata entry
	featureToMetadata := make(map[string]*FeatureMetadata)
	metadataByMarketingName := make(map[string]*FeatureMetadata)

	for key, metadata := range config.Features {
		metaCopy := metadata
		metadataByMarketingName[metadata.MarketingName] = &metaCopy

		// If feature_keys specified, map each to this metadata
		if len(metadata.FeatureKeys) > 0 {
			for _, fkey := range metadata.FeatureKeys {
				featureToMetadata[fkey] = &metaCopy
			}
		} else {
			// Otherwise, key is the feature key itself
			featureToMetadata[key] = &metaCopy
		}
	}

	states := resolveSelfHostedStates(features, featureToMetadata)

	// Group features by marketing name (many-to-one)
	featureGroups := make(map[string][]*FeatureInfo)

	for featureKey, feature := range features {
		// Skip features whose dependencies are unavailable; the base feature's row covers them
		if states[featureKey].blocked {
			continue
		}
		metadata := featureToMetadata[featureKey]
		// LaunchDarkly-only gates appear only once self-hosted-parity.json names them;
		// the raw report lists the rest
		if feature.LaunchDarklyOnly && metadata == nil {
			continue
		}

		var marketingName string
		if metadata != nil {
			marketingName = metadata.MarketingName
		} else {
			// No config entry - use friendly name from features.go
			marketingName = feature.FriendlyName
		}

		featureGroups[marketingName] = append(featureGroups[marketingName], feature)
	}

	// Hand-maintained rows: capabilities with no flag that are still worth listing, such as ones that need configuration
	for key, metadata := range config.Features {
		if metadata.Gate == "" || features[key] != nil || len(metadata.FeatureKeys) > 0 {
			continue
		}
		if metadata.IncludeInTable != nil && !*metadata.IncludeInTable {
			continue
		}
		metaCopy := metadata
		mf := &MarketingFeature{MarketingName: metadata.MarketingName, Status: "Y"}
		applyMetadata(mf, &metaCopy, existing)
		result = append(result, mf)
	}

	// Create marketing features from groups
	for marketingName, featureList := range featureGroups {
		metadata := metadataByMarketingName[marketingName]

		// Skip if explicitly excluded from table
		if metadata != nil && metadata.IncludeInTable != nil && !*metadata.IncludeInTable {
			continue
		}

		// Determine combined status (most permissive wins)
		// If any feature is Y, status is Y
		// If all are N, status is N
		// Otherwise Y (has toggle)
		hasAvailable := false
		hasDefault := false
		hasUnavailable := false
		ldGated := false

		internalKeys := []string{}
		for _, f := range featureList {
			internalKeys = append(internalKeys, f.Key)
			if f.DirectLaunchDarklyOff {
				// A LaunchDarkly check in the code path is off on self-hosted whatever the license says
				ldGated = true
			}
			if states[f.Key].available {
				hasAvailable = true
				if states[f.Key].enabledByDefault {
					hasDefault = true
				}
			} else {
				hasUnavailable = true
			}
		}

		var status string
		if !hasAvailable || ldGated {
			status = "N"
		} else if hasDefault && !hasUnavailable {
			status = "Y"
		} else {
			status = "Y (has toggle)"
		}

		// Use feature_keys order when given so enrichment picks the same primary key every run
		if metadata != nil && len(metadata.FeatureKeys) > 0 {
			internalKeys = metadata.FeatureKeys
		} else {
			sort.Strings(internalKeys)
		}

		mf := &MarketingFeature{
			InternalKey:   strings.Join(internalKeys, ", "),
			MarketingName: marketingName,
			Status:        status,
		}

		applyMetadata(mf, metadata, existing)

		result = append(result, mf)
	}

	// Sort by marketing name
	sort.Slice(result, func(i, j int) bool {
		return result[i].MarketingName < result[j].MarketingName
	})

	return result
}

type selfHostedState struct {
	available        bool // SelfHosted.Available in features.go
	enabledByDefault bool // On without an explicit license toggle
	blocked          bool // A dependency is unavailable on self-hosted
}

// resolveSelfHostedStates mirrors how the service evaluates a feature on self-hosted:
// LaunchDarkly flags are never consulted, only SelfHosted.Available, the license toggle
// (SelfHosted.Default when absent), and every dependency in featureDependencies.
// depends_on in self-hosted-parity.json adds dependencies that features.go doesn't declare.
func resolveSelfHostedStates(features map[string]*FeatureInfo, featureToMetadata map[string]*FeatureMetadata) map[string]selfHostedState {
	states := make(map[string]selfHostedState)
	visiting := make(map[string]bool)

	var resolve func(key string) selfHostedState
	resolve = func(key string) selfHostedState {
		if s, ok := states[key]; ok {
			return s
		}
		feature, ok := features[key]
		if !ok || visiting[key] {
			// Unknown dependency or cycle: don't let it block anything
			return selfHostedState{available: true, enabledByDefault: true}
		}
		visiting[key] = true

		available := feature.Available && !feature.DirectLaunchDarklyOff
		s := selfHostedState{available: available, enabledByDefault: available && feature.Default}
		deps := feature.FeatureDependencies
		if metadata := featureToMetadata[key]; metadata != nil {
			deps = append(append([]string{}, deps...), metadata.DependsOn...)
		}
		for _, dep := range deps {
			if dep == key {
				continue
			}
			d := resolve(dep)
			if d.blocked || !d.available {
				s.blocked = true
			} else if !d.enabledByDefault {
				// Needs the dependency's license toggle too
				s.enabledByDefault = false
			}
		}

		visiting[key] = false
		states[key] = s
		return s
	}

	for key := range features {
		resolve(key)
	}
	return states
}

func applyMetadata(mf *MarketingFeature, metadata *FeatureMetadata, existing map[string]*MarketingFeature) {
	if metadata != nil {
		mf.Notes = metadata.Notes
		mf.Summary = metadata.Summary
		// An override refines a computed status but can't revive a feature the
		// code turns off on self-hosted, or the page would hide a regression
		if metadata.Status != "" && mf.Status != "N" {
			mf.Status = metadata.Status
		}
	}

	// Preserve ETA from existing summary, or use default from config or notes
	if existingFeature, ok := existing[mf.MarketingName]; ok && existingFeature.ETA != "" {
		mf.ETA = existingFeature.ETA
	} else if metadata != nil && metadata.DefaultETA != "" {
		// Use default_eta when specified
		mf.ETA = metadata.DefaultETA
	} else if metadata != nil && metadata.Notes != "" && mf.Status != "Y" {
		// Fall back to notes for non-Y features when no ETA specified
		mf.ETA = metadata.Notes
	}
}

func escapeTableCell(s string) string {
	return strings.ReplaceAll(s, "|", "\\|")
}

func generateInternalSummaryContent(features []*MarketingFeature) string {
	var sb strings.Builder

	sb.WriteString("# Self Hosted Feature Parity - Internal\n\n")
	sb.WriteString("This is the internal feature parity tracking document with detailed notes and ETAs.\n\n")
	sb.WriteString("**Note:** This is for internal use. The public version is generated from this via `feature-publish-config.json`.\n\n")

	// Check if any features have history data
	hasHistory := false
	for _, f := range features {
		if f.History != "" {
			hasHistory = true
			break
		}
	}

	if hasHistory {
		sb.WriteString("| Feature | Self Hosted? | ETA | History | Summary |\n")
		sb.WriteString("| :---- | :---- | :---- | :---- | :---- |\n")
	} else {
		sb.WriteString("| Feature | Self Hosted? | ETA | Summary |\n")
		sb.WriteString("| :---- | :---- | :---- | :---- |\n")
	}

	for _, f := range features {
		eta := f.ETA
		if eta == "" {
			eta = " "
		}
		summary := escapeTableCell(f.Summary)
		if summary == "" {
			summary = " "
		}
		if hasHistory {
			history := f.History
			if history == "" {
				history = " "
			}
			sb.WriteString(fmt.Sprintf("| %s | %s | %s | %s | %s |\n", f.MarketingName, f.Status, eta, history, summary))
		} else {
			sb.WriteString(fmt.Sprintf("| %s | %s | %s | %s |\n", f.MarketingName, f.Status, eta, summary))
		}
	}

	sb.WriteString("\n")

	return sb.String()
}

func enrichInternalSummaryWithGitHistory(servicePath string) {
	// Check if gh CLI is installed
	if !isGhInstalled() {
		fmt.Println("Note: gh CLI not installed, skipping git history enrichment")
		return
	}

	internalPath := "scripts/self-hosted-feature-parity/generated/feature-parity-internal.md"

	// Read internal summary
	existingFeatures := parseExistingSummary(internalPath)
	if len(existingFeatures) == 0 {
		fmt.Fprintf(os.Stderr, "Error: No features found in internal summary. Run --update-summary first.\n")
		os.Exit(1)
	}

	fmt.Printf("Enriching %d features with git history...\n", len(existingFeatures))

	// Parse features.go to get feature keys
	features := parseFeatures(servicePath)
	addLaunchDarklyOnlyFeatures(servicePath, features)
	marketingFeatures := buildMarketingFeatures(features, existingFeatures)

	// Enrich each feature with git history
	for _, mf := range marketingFeatures {
		// Get the first internal key (for features with multiple keys, use the first one)
		keys := strings.Split(mf.InternalKey, ", ")
		if len(keys) == 0 {
			continue
		}
		primaryKey := keys[0]
		if primaryKey == "" {
			// Hand-maintained rows have no flag to trace
			continue
		}

		history := getFeatureHistory(servicePath, primaryKey)
		if history != "" {
			mf.History = history
		}
	}

	// Regenerate internal doc with history
	content := generateInternalSummaryContent(marketingFeatures)
	err := os.WriteFile(internalPath, []byte(content), 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error writing enriched internal summary: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Enriched %s with git history\n", internalPath)
}

func isGhInstalled() bool {
	_, err := exec.LookPath("gh")
	return err == nil
}

func getFeatureHistory(servicePath, featureKey string) string {
	// Use git log with -S to find the FIRST commit that introduced this feature key
	// --reverse shows commits in chronological order (oldest first)
	// -S searches for commits that add or remove the search string
	// LaunchDarkly-only gates are defined with the other flag keys rather than in features.go
	sourceFile := "cmd/service/api/features/features.go"
	if strings.HasPrefix(featureKey, "LDKey") {
		sourceFile = "cmd/service/services/featureflag/launch_darkly.go"
	}
	cmd := exec.Command("git", "log", "-S", featureKey, "--reverse", "--all", "--pretty=format:%H", "--", sourceFile)
	cmd.Dir = servicePath
	output, err := cmd.Output()
	if err != nil {
		return ""
	}

	// Get the first commit SHA (first line of output)
	lines := strings.Split(strings.TrimSpace(string(output)), "\n")
	if len(lines) == 0 || lines[0] == "" {
		return ""
	}
	commitSHA := lines[0]

	// Get PR number from commit
	prNumber := getPRNumberFromCommit(servicePath, commitSHA)
	if prNumber == "" {
		return ""
	}

	// Get PR details and extract issues
	prLink := fmt.Sprintf("[#%s](https://github.com/pulumi/pulumi-service/pull/%s)", prNumber, prNumber)
	issues := getIssuesFromPR(servicePath, prNumber)

	if len(issues) > 0 {
		issueLinks := make([]string, len(issues))
		for i, issue := range issues {
			issueLinks[i] = fmt.Sprintf("[#%s](https://github.com/pulumi/pulumi-service/issues/%s)", issue, issue)
		}
		return fmt.Sprintf("%s (%s)", prLink, strings.Join(issueLinks, ", "))
	}

	return prLink
}

func getPRNumberFromCommit(servicePath, commitSHA string) string {
	// Try to get PR number from commit message
	cmd := exec.Command("git", "log", "-1", "--pretty=%s", commitSHA)
	cmd.Dir = servicePath
	output, err := cmd.Output()
	if err != nil {
		return ""
	}

	// Look for (#1234) pattern in commit message
	matches := prNumberInCommit.FindStringSubmatch(string(output))
	if len(matches) > 1 {
		return matches[1]
	}

	// Try using gh CLI to find PR
	cmd = exec.Command("gh", "pr", "list", "--search", commitSHA, "--state", "merged", "--json", "number", "--jq", ".[0].number")
	cmd.Dir = servicePath
	output, err = cmd.Output()
	if err != nil {
		return ""
	}

	return strings.TrimSpace(string(output))
}

func getIssuesFromPR(servicePath, prNumber string) []string {
	// Get PR body and title
	cmd := exec.Command("gh", "pr", "view", prNumber, "--json", "body,title")
	cmd.Dir = servicePath
	output, err := cmd.Output()
	if err != nil {
		return nil
	}

	var prData struct {
		Body  string `json:"body"`
		Title string `json:"title"`
	}
	if err := json.Unmarshal(output, &prData); err != nil {
		return nil
	}

	// Extract issue references from title and body
	text := prData.Title + " " + prData.Body
	return extractIssueNumbers(text, prNumber)
}

var prNumberInCommit = regexp.MustCompile(`\(#(\d+)\)`)
var issueReference = regexp.MustCompile(`#(\d+)\b`)

// extractIssueNumbers finds issue references like #1234 in a PR's title and body,
// skipping the PR's own number and short numbers such as #1 or #000 from checklists and templates.
func extractIssueNumbers(text, prNumber string) []string {
	matches := issueReference.FindAllStringSubmatch(text, -1)

	seen := map[string]bool{prNumber: true}
	var issues []string
	for _, match := range matches {
		if len(match) > 1 {
			issue := match[1]
			if len(issue) < 3 || strings.HasPrefix(issue, "0") {
				continue
			}
			if !seen[issue] {
				seen[issue] = true
				issues = append(issues, issue)
			}
		}
	}

	return issues
}

func generatePublicDoc(features map[string]*FeatureInfo) {
	internalPath := "scripts/self-hosted-feature-parity/generated/feature-parity-internal.md"
	publicPath := "content/docs/administration/self-hosting/feature-parity.md"

	// Read internal summary
	existingFeatures := parseExistingSummary(internalPath)

	// Map known features
	marketingFeatures := buildMarketingFeatures(features, existingFeatures)

	// Load publish config
	publishConfig := loadPublishConfig()

	// Filter and transform for public consumption
	publicFeatures := filterForPublish(marketingFeatures, publishConfig)

	// A published row that no longer comes out of the metadata was renamed or
	// removed upstream; fail rather than silently drop it from the page
	rendered := make(map[string]bool)
	for _, f := range publicFeatures {
		rendered[f.MarketingName] = true
	}
	var missing []string
	for name, conf := range publishConfig.Features {
		if conf.Publish && !rendered[name] {
			missing = append(missing, name)
		}
	}
	if len(missing) > 0 {
		sort.Strings(missing)
		fmt.Fprintf(os.Stderr, "Error: published rows with no matching feature: %s\n", strings.Join(missing, ", "))
		os.Exit(1)
	}

	// Generate public content
	content := generatePublicContent(publicFeatures, publishConfig)

	// Write to file
	err := os.WriteFile(publicPath, []byte(content), 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error writing public doc: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Generated %s\n", publicPath)
}

func filterForPublish(features []*MarketingFeature, publishConfig *FeaturePublishConfig) []*MarketingFeature {
	var result []*MarketingFeature

	for _, f := range features {
		// Only rows listed in the public config are published, so a new flag
		// can't reach the public page before someone decides it should
		if pubConf, exists := publishConfig.Features[f.MarketingName]; exists && pubConf.Publish {
			result = append(result, f)
		}
	}

	return result
}

func generatePublicContent(features []*MarketingFeature, publishConfig *FeaturePublishConfig) string {
	var sb strings.Builder

	sb.WriteString("---\n")
	sb.WriteString("title_tag: Self-Hosted Feature Parity | Self-Hosting Pulumi\n")
	sb.WriteString("meta_desc: Which Pulumi Cloud features are available in self-hosted Pulumi Cloud, and which need extra configuration or enablement.\n")
	sb.WriteString("title: Feature parity\n")
	sb.WriteString("h1: Self-hosted feature parity\n")
	sb.WriteString("menu:\n")
	sb.WriteString("  administration:\n")
	sb.WriteString("    name: Feature parity\n")
	sb.WriteString("    parent: administration-self-hosting\n")
	sb.WriteString("    weight: 8\n")
	sb.WriteString("    identifier: administration-self-hosted-feature-parity\n")
	sb.WriteString("pulumi_cloud_feature: self-hosting\n")
	sb.WriteString("---\n\n")

	sb.WriteString("{{< self-hosting-trial-note />}}\n\n")
	sb.WriteString("The table below shows whether selected Pulumi Cloud features are available in self-hosted Pulumi Cloud, and what they need. It isn't a complete list of Pulumi Cloud features: to check one that isn't listed, [contact us](/contact/). The [status key](#status-key) below the table explains what each status means.\n\n")

	type publicRow struct {
		name, docsURL, status, notes string
	}
	var rows []publicRow
	for _, f := range features {
		conf := publishConfig.Features[f.MarketingName]

		name := f.MarketingName
		if conf.PublicName != "" {
			name = conf.PublicName
		}

		var status string
		switch f.Status {
		case "Y":
			status = "Available"
		case "Y (has toggle)":
			status = "Requires enablement"
		case "Y (needs config)":
			status = "Requires configuration"
		case "N":
			status = "Not available"
		default:
			status = f.Status
		}

		rows = append(rows, publicRow{name: name, docsURL: conf.DocsURL, status: status, notes: conf.PublicNotes})
	}
	sort.Slice(rows, func(i, j int) bool {
		return strings.ToLower(rows[i].name) < strings.ToLower(rows[j].name)
	})

	sb.WriteString("| Feature | Self-hosted | Details |\n")
	sb.WriteString("|---|---|---|\n")
	for _, r := range rows {
		name := r.name
		if r.docsURL != "" {
			name = fmt.Sprintf("[%s](%s)", r.name, r.docsURL)
		}
		sb.WriteString(fmt.Sprintf("| %s | %s | %s |\n", name, r.status, escapeTableCell(r.notes)))
	}

	sb.WriteString("\n## Status key\n\n")
	sb.WriteString("| Status | Meaning |\n")
	sb.WriteString("|---|---|\n")
	sb.WriteString("| Available | Works the same way as in Pulumi Cloud. |\n")
	sb.WriteString("| Requires enablement | Included, but turned off by default. Contact Pulumi support to turn it on for your installation. |\n")
	sb.WriteString("| Requires configuration | Works once you set up the extra components described in the feature's details. |\n")
	sb.WriteString("| Not available | Not supported in self-hosted Pulumi Cloud yet. |\n")

	return sb.String()
}

func generateFullReport(features map[string]*FeatureInfo) {
	// Sort features by friendly name
	var featureList []*FeatureInfo
	for _, f := range features {
		featureList = append(featureList, f)
	}
	sort.Slice(featureList, func(i, j int) bool {
		return featureList[i].FriendlyName < featureList[j].FriendlyName
	})

	fmt.Println("# Feature Availability: SaaS vs Self-Hosted")
	fmt.Println()
	fmt.Println("This table shows which features are available in Pulumi Cloud (SaaS) but not in self-hosted installations.")
	fmt.Println()
	fmt.Println("## Features NOT Available in Self-Hosted")
	fmt.Println()
	fmt.Println("| Feature | Internal Key | SaaS | Self-Hosted |")
	fmt.Println("|---------|--------------|------|-------------|")

	for _, f := range featureList {
		if !f.Available {
			fmt.Printf("| %s | %s | ✅ Available | ❌ Not Available |\n", f.FriendlyName, f.Key)
		}
	}

	fmt.Println()
	fmt.Println("## Features Available in Self-Hosted (Disabled by Default)")
	fmt.Println()
	fmt.Println("These features are available in self-hosted but disabled by default. Enable via license file.")
	fmt.Println()
	fmt.Println("| Feature | Internal Key | SaaS | Self-Hosted Available | Self-Hosted Default |")
	fmt.Println("|---------|--------------|------|---------------------|-------------------|")

	for _, f := range featureList {
		if f.Available && !f.Default {
			fmt.Printf("| %s | %s | ✅ Available | ✅ Yes | ❌ Off |\n", f.FriendlyName, f.Key)
		}
	}

	fmt.Println()
	fmt.Println("## Features Available and Enabled in Self-Hosted")
	fmt.Println()
	fmt.Println("| Feature | Internal Key | SaaS | Self-Hosted Available | Self-Hosted Default |")
	fmt.Println("|---------|--------------|------|---------------------|-------------------|")

	for _, f := range featureList {
		if f.Available && f.Default {
			fmt.Printf("| %s | %s | ✅ Available | ✅ Yes | ✅ On |\n", f.FriendlyName, f.Key)
		}
	}
}
