## Prerequisites

1. [Install Pulumi](https://pulumi.io/install)
1. [Install Node.js version 6 or later](https://nodejs.org/en/download/)
1. Install a package manager for Node.js, such as [npm](https://www.npmjs.com/get-npm) or [Yarn](https://yarnpkg.com/en/docs/install).
1. [Install Google Cloud SDK (`gcloud`)](https://cloud.google.com/sdk/docs/downloads-interactive)
1. Configure Auth Options
    1. `gcloud` Login

        ```bash
        $ gcloud auth login
        $ gcloud config set project <YOUR_PROJECT_HERE>
        $ gcloud auth application-default login
        ```
    1. [Configure GCP Service Account Key & Download Credentials](https://pulumi.io/install/gcp.html)
        * **Note**: The Service Account key credentials used must have the
        role `Kubernetes Engine Admin` / `container.admin`
