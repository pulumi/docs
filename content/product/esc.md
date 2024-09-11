---
title: "Pulumi ESC: Environments, Secrets, and Configuration"
layout: esc

meta_title: "Pulumi ESC: Environments, Secrets, and Configuration"
meta_desc: Centralized environments, secrets, and configuration management for cloud applications and infrastructure
meta_image: "/images/product/esc-how-it-works-diagram.png"
aliases:
    - /esc

subtitle: Centralized secrets management & orchestration. Easily access, share, and manage secrets securely on any cloud, using your favorite programming languages.

overview:
    header: Centralized environments, secrets, and configuration management and orchestration that helps streamline operations, improve traceability, and ensure consistent security practices
    body: |
      - **Stop secret sprawl.** Pull and sync configuration and secrets with any secrets store – including HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, 1Password, and more – and consume in any application, tool, or CI/CD platform.  
      - **Trust (and prove) your secrets are secure.** Every environment can be locked down with role-based access controls (RBAC) and versioned with all changes fully logged for auditing.  
      - **Ditch `.env` files.** No more storing secrets in plaintext on dev computers. Developers can easily access secrets via CLI, API, Kubernetes operator, the Pulumi Cloud UI, and in-code with Typescript/Javascript, Python, and Go SDKs.
      - **Use with or without Pulumi IaC.** Use Pulumi ESC to centrally manage your configuration and secrets independently of Pulumi IaC, or use ESC and IaC together for the convenience of storing secrets in config with a higher degree of security than using plaintext.

benefits:
    title: Benefits of Pulumi ESC
    items:
        - icon: lock
          icon_color: purple
          title: Frictionless Security
          description: Easy-to-use single source of truth for all configuration and secrets with guardrails. Seamlessly adopt short-lived dynamic secrets.
          points:
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Vel mollis vel luctus quis ex. Montes inceptos venenatis ligula dictumst magnis fringilla. Accumsan luctus neque ex eros leo fusce; mi aliquet. Laoreet laoreet potenti facilisis vehicula mi velit odio.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Fusce magnis neque; suscipit dui metus blandit suspendisse. Luctus aliquet malesuada sapien venenatis amet velit. Est praesent commodo ullamcorper finibus fames quam augue, aliquet viverra.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Nam at mauris lacus consequat a finibus luctus. Nisi cras ac pretium tincidunt viverra vitae volutpat. Maecenas nascetur sem habitant nec; quisque per orci. Praesent ligula malesuada finibus dolor per tincidunt lacinia.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Vehicula quisque rhoncus dis senectus class sem natoque. Id aenean aliquet lacinia, senectus conubia eros quam?
        - icon: lightning
          icon_color: yellow
          title: Improve Developer Efficiency
          description: Never have downtime over changed configuration. Change once and have it updated everywhere.
          points:
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Tristique venenatis lectus condimentum massa risus massa turpis conubia commodo. Habitasse quis sollicitudin cras aliquam; nulla class odio scelerisque. Magnis ad potenti accumsan eleifend, fames etiam bibendum. At dolor dapibus non adipiscing mi aenean primis vehicula.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Convallis luctus lacinia luctus duis facilisi ornare aliquet feugiat ligula. Libero libero elit praesent mi ultricies congue, libero tempus volutpat. Gravida metus felis purus quisque varius luctus.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Curae nulla taciti duis tincidunt curabitur pharetra. In massa erat; fames vulputate taciti himenaeos. Luctus nam sed accumsan elementum ullamcorper, habitasse odio suspendisse.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Nisi augue nec sociosqu placerat finibus molestie finibus eu. Gravida ex proin in facilisi ultricies amet ligula phasellus. Mauris torquent habitasse duis primis ad non.
        - icon: gavel
          icon_color: salmon
          title: Control Access and Compliance
          description: Enforce least-privileged access through role-based access controls. All changes are fully logged for auditing.
          points:
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Ultricies ad urna tempus bibendum ullamcorper rutrum curae imperdiet odio. Et id senectus dis semper imperdiet? Cras hendrerit magna himenaeos euismod leo! Mattis torquent aptent imperdiet mollis sociosqu sed sollicitudin nostra.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Vitae nostra nisl morbi finibus posuere. Sit mauris justo consequat dolor feugiat per torquent litora. Diam massa porttitor lectus malesuada iaculis sed rutrum.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Nulla dui cursus massa sem sociosqu lacus. Tincidunt maecenas cubilia dictum placerat ex tellus sodales sodales. Odio magnis egestas venenatis nisl magna torquent scelerisque. Litora primis libero habitasse id leo blandit quam ipsum.
            - Lorem ipsum odor amet, consectetuer adipiscing elit. Dui ridiculus justo dis maximus turpis quam facilisis mi lobortis. Turpis leo felis aenean nisi aliquet vehicula potenti turpis. Nec pharetra imperdiet sapien leo torquent nisi augue consectetur.

diagram:
    items:
        - number: 1
          description: Pulumi ESC enables you to define environments, which contain collections of secrets and configuration. Each environment can be composed from multiple environments.
        - number: 2
          description: Pulumi ESC supports a variety of configuration and secrets sources, and it has an extensible plugin model that allows third-party sources. 
        - number: 3
          description: Pulumi ESC has a rich API that allows for easy integration.  Every value in an environment can be accessed from any execution environment. 
        - number: 4
          description: Every environment can be locked down with RBAC, versioned, and audited. 

screenshot:
    items:
        - title: Composable
          description: Secrets and configurations are organized into logical groupings called environments. Environments support importing one into another, allowing for easy composability and inheritance of shared secrets and configuration.
        - title: Traceable
          description: Never lose track of where configurations are being used. Trace the downstream impact of any secrets or configuration changes to see if they match expectations. 
        - title: Versionable
          description: Create different versions of environments, so you can gracefully migrate between breaking configuration changes.

customer_quotes:
  tetrate:
    text: |
      “With Pulumi ESC, our developers get dynamic AWS and Azure credentials on-demand. Onboarding new developers is quick and secure, with no more manually filling in .env templates.”
    author: Liam White, Platform Lead
    logo: tetrate
  mysten:
    text: |
      “Pulumi ESC has been a lifesaver for us. It’s nice to throw everything behind an ESC environment and eliminate one-off granting IAM permissions and other issues related to static credentials.”
    author: JK Jensen, Software Engineering Team Lead
    logo: mysten-labs

---
