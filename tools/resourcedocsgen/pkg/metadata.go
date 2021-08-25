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
	Name string `yaml:"name"`
	// Title is the package's display-friendly name.
	Title       string `yaml:"title"`
	Description string `yaml:"description"`

	UpdatedOn     int64           `yaml:"updated_on"`
	Publisher     string          `yaml:"publisher"`
	Category      PackageCategory `yaml:"category"`
	PackageStatus PackageStatus   `yaml:"package_status"`
	Version       string          `yaml:"version"`

	// Featured indicates whether or not a package is highlighted as
	// a featured package.
	Featured bool `yaml:"featured"`
	// Native is true if the package does not use the TF bridge.
	Native bool `yaml:"native"`
}
