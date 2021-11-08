package pkg

// PackageStatus is a type to indicate a package's status.
type PackageStatus string

// PackageCategory is a type to indicate the category a package
// belongs to.
type PackageCategory string

const (
	// PackageStatusGA indicates that a package is generally available for use.
	PackageStatusGA PackageStatus = "ga"
	// PackageStatusPublicPreview indicates that a package is available as
	// pre-release and can undergo changes before it goes GA.
	PackageStatusPublicPreview PackageStatus = "public_preview"

	PackageCategoryCloud          PackageCategory = "Cloud"
	PackageCategoryDatabase       PackageCategory = "Database"
	PackageCategoryInfrastructure PackageCategory = "Infrastructure"
	PackageCategoryMonitoring     PackageCategory = "Monitoring"
	PackageCategoryNetwork        PackageCategory = "Network"
	PackageCategoryUtility        PackageCategory = "Utility"
	PackageCategoryVCS            PackageCategory = "Version Control System"
)

// PackageMeta represents the metadata of a package to be published
// on the website.
type PackageMeta struct {
	// Name is the package's common name.
	Name string `json:"name"`
	// Title is the package's display-friendly name.
	Title       string `json:"title"`
	Description string `json:"description"`
	LogoURL     string `json:"logo_url"`
	RepoURL     string `json:"repo_url"`
	// SchemaFilePath is the path to the package's schema file (json or yaml)
	// relative to the root of that package's repo.
	SchemaFilePath string `json:"schema_file_path"`

	UpdatedOn     int64           `json:"updated_on"`
	Publisher     string          `json:"publisher"`
	Category      PackageCategory `json:"category"`
	PackageStatus PackageStatus   `json:"package_status"`
	Version       string          `json:"version"`

	// Featured indicates whether or not a package is highlighted as
	// a featured package.
	Featured bool `json:"featured"`
	// Native is true if the package does not use the TF bridge.
	Native bool `json:"native"`
	// Component indicates if the package is a component and not
	// a provider.
	Component bool `json:"component"`
}
