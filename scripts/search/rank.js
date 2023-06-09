module.exports = {

    // Return the explicit or implicit rank for a given page. See the Algolia documentation to learn
    // more about how Algolia ranking and relevance work.
    // https://www.algolia.com/doc/guides/managing-results/must-do/custom-ranking/
    get(page) {

        // If the page is explicitly ranked zero, return zero.
        const explicitRank = this.getExplicitRank(page);
        if (explicitRank === 0) {
            return 0;
        }

        // If it's ranked otherwise numerically, return that.
        if (!isNaN(explicitRank)) {
            return explicitRank;
        }

        // Otherwise, return its implicit rank.
        return this.getImplicitRank(page);
    },

    // Rank can be set at the page level as well (e.g., in YAML frontmatter: `search.rank: 123`).
    getExplicitRank(page) {
        return page.params?.search?.rank;
    },

    // Pages can be boosted at the page level also (e.g., `search.boost: true`)
    isExplicitlyBoosted(page) {
        return !!page.params?.search?.boost;
    },

    // Implicit keywords are derived from the page's URL. We do this to make string matches more
    // likely. (For example, to surface both AWS Classic and AWS Native for queries for 'aws'.)
    getImplicitKeywords(page) {
        const match = page.href.match(/^\/registry\/packages\/(aws|aws-native|azure|azure-native|gcp|google-native|kubernetes)\/$/);

        if (match && match[1]) {
            return [
                match[1].replace("-native", ""),
            ];
        }

        return [];
    },

    // Implicit rankings allow us to codify how relevant our pages are in relation to one another.
    // Rankings are applied in descending order numerically (i.e., for a given query, higher-ranked
    // pages will will show up before lower-ranked ones).
    getImplicitRank(page) {

        // Get-started pages.
        if (page.href.match(/^\/docs\/clouds\/(aws|azure|gcp|kubernetes)\/get-started\//)) {

            // Top-level get-started pages rank highest.
            if (page.kind === "section") {
                return 1000;
            }

            // All other get-started pages get de-listed. We don't want them noising up the results,
            // as they aren't the kinds of pages you'd typically want to navigate to directly.
            return 0;
        }

        // Cloud landing pages are next.
        if (page.href.match(/^\/docs\/clouds\/(aws|azure|gcp|kubernetes)\//)) {

            // Top-level pages again rank highest.
            if (page.kind === "section") {
                return 990;
            }

            return 980;
        }

        // Docs pages are next.
        if (page.href.startsWith("/docs")) {

            // First concepts.
            if (page.href.startsWith("/docs/concepts/")) {
                return 890;
            }

            // Then using.
            if (page.href.startsWith("/docs/using-pulumi/")) {
                return 880;
            }

            // Top-level pages again rank highest.
            if (page.kind === "section") {
                return 870
            }

            return 860;
        }

        // Tier-1 provider pages are next.
        if (page.href.match(/^\/registry\/packages\/(aws|azure-native|gcp|kubernetes)\//)) {

            if (page.href.match(/^\/registry\/packages\/(aws|azure-native|gcp|kubernetes)\/$/)) {
                return 790;
            } else if (page.href.match(/installation-configuration/)) {
                return 780;
            } else if (page.href.match(/api-docs/)) {

                // Order Kubernetes API docs more recent first (e.g., v1 over v1beta1).
                if (page.href.match(/\/kubernetes\/api-docs/)) {
                    if (page.href.match(/\/v\d\//)) {
                        return 775;
                    }
                }

                return 770;
            } else if (page.href.match(/how-to-guides/)) {
                return 760;
            }
        }

        // Tier-2 providers are next.
        if (page.href.match(/^\/registry\/packages\/(aws-native|azure|google-native|digitalocean)\//)) {

            if (page.href.match(/^\/registry\/packages\/(aws-native|azure|google-native|digitalocean)\/$/)) {
                return 690;
            } else if (page.href.match(/installation-configuration/)) {
                return 680;
            } else if (page.href.match(/api-docs/)) {
                return 670;
            } else if (page.href.match(/how-to-guides/)) {
                return 660;
            }
        }

        // Then officially supported component packages.
        if (page.href.match(/^\/registry\/packages\/(awsx|eks|aws-iam|aws-apigateway|aws-quickstart-vpc)\//)) {

            if (page.href.match(/^\/registry\/packages\/(awsx|eks|aws-iam|aws-apigateway|aws-quickstart-vpc)\/$/)) {
                return 590;
            } else if (page.href.match(/installation-configuration/)) {
                return 580;
            } else if (page.href.match(/api-docs/)) {
                return 570;
            } else if (page.href.match(/how-to-guides/)) {
                return 560;
            }
        }

        // Then the rest.
        if (page.href.match(/^\/registry\/packages\//)) {

            if (page.href.match(/^\/registry\/packages\/[\w-]+\/$/)) {
                return 490;
            } else if (page.href.match(/installation-configuration/)) {
                return 480;
            } else if (page.href.match(/api-docs/)) {
                return 470;
            } else if (page.href.match(/how-to-guides/)) {
                return 460;
            }
        }

        if (page.href.startsWith("/templates")) {
            return 390;
        }

        if (page.href.startsWith("/blog")) {
            return 290;
        }
    },

    isImplicitlyBoosted(page) {

        // Tier-1 provider pages also get boosted.
        if (page.href.match(/^\/registry\/packages\/(aws|azure-native|gcp|kubernetes)\/$/)) {
            return true;
        }

        return false;
    }
}
