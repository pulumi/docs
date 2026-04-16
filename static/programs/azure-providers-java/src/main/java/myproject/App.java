package myproject;

import com.pulumi.Pulumi;
import com.pulumi.azurenative.resources.ResourceGroup;
import com.pulumi.azurenative.resources.ResourceGroupArgs;
import com.pulumi.azuread.Application;
import com.pulumi.azuread.ApplicationArgs;
import com.pulumi.azuread.ServicePrincipal;
import com.pulumi.azuread.ServicePrincipalArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a resource group using the Azure Native provider.
            var resourceGroup = new ResourceGroup("my-resource-group", ResourceGroupArgs.builder()
                .location("eastus")
                .build());

            // Create an Entra ID application registration using the Azure AD provider.
            var application = new Application("my-application", ApplicationArgs.builder()
                .displayName("my-application")
                .build());

            // Create a service principal for the application.
            var servicePrincipal = new ServicePrincipal("my-service-principal", ServicePrincipalArgs.builder()
                .clientId(application.clientId())
                .build());

            ctx.export("resourceGroupName", resourceGroup.name());
            ctx.export("applicationClientId", application.clientId());
            ctx.export("servicePrincipalId", servicePrincipal.id());
        });
    }
}
