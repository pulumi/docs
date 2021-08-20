package pkg

type PackageStatus string
type PackageCategory string

const (
	PackageStatusGA            PackageStatus = "ga"
	PackageStatusPublicPreview PackageStatus = "public_preview"

	PackageCategoryCloud     PackageCategory = "Cloud"
	PackageCategoryNetwork   PackageCategory = "Network"
	PackageCategoryUtilities PackageCategory = "Utilities"
	PackageCategoryDatabase  PackageCategory = "Database"
)

type PackageMeta struct {
	Name          string          `yaml:"name"`
	UpdatedOn     int64           `yaml:"updated_on"`
	Publisher     string          `yaml:"publisher"`
	Title         string          `yaml:"title"`
	Description   string          `yaml:"description"`
	Category      PackageCategory `yaml:"category"`
	PackageStatus PackageStatus   `yaml:"package_status"`
	Featured      bool            `yaml:"featured"`
	Native        bool            `yaml:"native"`
}
