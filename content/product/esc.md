---
title: "Pulumi ESC: Environments, Secrets, and Configuration"
layout: esc

meta_title: "Pulumi ESC: Environments, Secrets, and Configuration"
meta_desc: Centralized environments, secrets, and configuration management for cloud applications and infrastructure
meta_image: "/images/product/esc-how-it-works-diagram.png"
aliases:
    - /esc

overview:
    header: Centralized environments, secrets, and configuration management for cloud applications and infrastructure
    description: Today’s cloud environments access a multitude of configurations – including network settings, deployment options, API Keys, and other important secrets like database credentials –  from many different types of cloud infrastructure and SaaS services. Every team stores configuration settings like these in different locations, from secrets managers to plaintext files. This sprawl results in uncontrolled and untraceable configurations, causing operational bottlenecks, outages due to human error, and security breaches. Pulumi ESC enables you to centrally manage all configuration and secrets across your organization.

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
          description: Environments contain collections of secrets and configuration. Compose environments together from multiple other environments to allow easy inheritance of shared configuration, eliminating “copy and paste errors”.
        - title: Traceable
          description: Never lose track of where configurations are being used and where. Trace the downstream impact of any configuration to see if the impact matches your expectations. 
        - title: Versionable
          description: Create different versions of environments, so you can gracefully migrate between breaking configuration changes.
---
