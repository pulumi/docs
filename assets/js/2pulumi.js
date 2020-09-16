// Extracts a query string variable from the browser's location.
function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");

    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");

        if (pair[0] === variable) {
            return decodeURIComponent(pair[1].replace(/\+/g, "%20"));
        }
    }
}

function getCurrentInputKind() {
    var ik;
    $("pulumi-chooser[type='input-kind'] > ul > li.active > a").each(function (i, e) {
        ik = $(e).text().trim().toLowerCase();
        return false;
    });
    return ik;
}

function setCurrentInputKind(ik) {
    $("pulumi-chooser[type='input-kind'] > ul > li > a").each(function (i, e) {
        if ($(e).text().trim().toLowerCase() === ik) {
            $(e)[0].click();
            return false;
        }
    });
}

function getCurrentLanguage() {
    var cl;
    $("pulumi-chooser[type='language'] > ul > li.active > a").each(function (i, e) {
        cl = e.innerText.trim().toLowerCase();
        return false;
    });
    return cl;
}

// currentCode will be updated to keep track of the currently converted code files. This
// is updated by convertCode and referenced from downloadCode to turn them into a ZIP for downloading.
var currentCodeFiles = {};

function clearLanguageFiles(language) {
    $("#pulumi-code-"+language+"-files").text("");
    $("#pulumi-code-download-icon").hide();
    $("#pulumi-code-download-button").addClass([ "opacity-50", "cursor-not-allowed" ]);
    currentCodeFiles = {};
}

function addLanguageFile(language, fn, code) {
    // Track this in the current list of files.
    currentCodeFiles[fn] = code;

    // Try to colorize the code first.
    if (window.Prism) {
        try {
            code = window.Prism.highlight(code, Prism.languages[language], language);
        } catch (err) {
            console.log("code highlighting failed: " + err);
        }
    } else {
        console.log("no code highlighting available");
    }

    let files = $(`#pulumi-code-${language}-files`);
    let fileno = files.children().length;
    let filediv = `pulumi-code-${language}-${fileno}`;
    files.append(`
        <p class="m-0 ${fileno == 0 ? "" : "-mt-4"} p-2 bg-purple-300 text-white font-bold font-mono font-xs"
            style="font-size: 0.75rem !important; color: #fff !important">${fn}</p>
        <div class="highlight" id="${filediv}">
            <pre class="chroma"><code class="language-typescript"
                style="font-size: 14px !important;font-family:Source Code Pro, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace" data-lang="typescript">${code}</code></pre>
            <div class="copy-button-container">
                <pulumi-tooltip>
                    <button class="copy-button"><i class="far fa-copy copy text-xl"></i></button>
                    <span slot="content">Click to copy</span>
                </pulumi-tooltip>
            </div>
        </div>
    `);
    $("#code[class*=language-], pre[class*=language-]").css("font-size", "14px");

    addCopyButton($(`#${filediv}`));
}

var couldNotConvertError =`<div id="couldnt-convert-code" class="container mx-auto pt-8">
    <div class="text-center max-w-2xl mx-auto">
        <h3>Sorry, we couldn't convert your code.</h3><br>
        <p class="text-lg mt-0 mb-16">
            There may be a problem with the code you submitted, or it might use a feature the
            converter doesn't yet support. To work with an engineer to help with your evaluation, please
            <a href="{{< relref "/about#contactus" >}})" class="link">contact us</a> or
            <a href="https://slack.pulumi.com" class="link">join our Community Slack</a>. We are here to help!
        </p>
    </div>
</div>
`;

// Display the "could not convert" boilerplate.
function displayCouldNotConvert(language) {
    clearLanguageFiles(language);
    $("#pulumi-code-"+language+"-files").html(couldNotConvertError);
}

// Now set up our event handler for conversion.
function convertCode(language, inputKind) {
    // If we got called without an explicit language, look it up.
    language = language || getCurrentLanguage();

    // Get the currently chosen language by looking up the active language chooser tab.
    let languageTextbox = language;
    if (language === "c#") {
        language = "csharp";
        languageTextbox = "csharp";
    } else if (language === "javascript") {
        language = "typescript";
        languageTextbox = "javascript";
    }

    // Clear the current fields.
    $("#pulumi-errors").hide();
    $("#pulumi-warnings").hide();
    clearLanguageFiles(languageTextbox);

    // Now read the various possible code sources.
    let tfCode = $("#terraform-code").val();
    let tfUrl = $("#terraform-url").val();
    let tfUploadFiles = $("#terraform-upload")[0].files;
    if (tfUrl === "https://") {
        tfUrl = "";
    }

    // Read the input kind and verify that we've got what we need.
    let tfIk = inputKind || getCurrentInputKind();
    switch (tfIk) {
    case "url":
        if (tfUrl === "") {
            $("#pulumi-errors").text("Error: Please enter a URL for the code to convert above, and then try again");
            $("#pulumi-errors").show();
            return;
        }
        break;
    case "upload":
        if (!tfUploadFiles || !tfUploadFiles.length) {
            $("#pulumi-errors").text("Error: Please choose code files to upload above, and then try again");
            $("#pulumi-errors").show();
            return;
        }
        break;
    default: // "code"
        if (tfCode === "") {
            $("#pulumi-errors").text("Error: Please enter the code to convert above, and then try again");
            $("#pulumi-errors").show();
            return;
        }
        break;
    }

    // Add some "waiting" touches.
    $(document.body).css({ "cursor": "wait" });
    $("#terraform-code, #terraform-url").css({ "cursor": "wait" });
    $("pulumi-chooser[type='language'] > ul > li > a").css({ "cursor": "wait" });
    addLanguageFile(languageTextbox, "…", "…");

    // Post to the endpoint and then, afterwards, add the result to the textbox.
    var urlPath = window.location.pathname === "/kube2pulumi/" ? "convertKube" : "convert";
    let post = {
        url: `https://1qm03yusb2.execute-api.us-west-2.amazonaws.com/stage/${urlPath}`,
    };
    if (tfIk === "upload") {
        // If uploading files, we need to take a slightly more complex path.
        var fd = new FormData();
        for (let i = 0; i < tfUploadFiles.length; i++) {
            fd.append("file", tfUploadFiles[i]);
        }
        post.data = fd;
        post.processData = false;
        post.contentType = false;

        // Since the payload is the multipart form upload, send the language in the querystring.
        post.url += "?language=" + language;
    } else {
        switch (tfIk) {
        case "url":
            post.data = JSON.stringify({ url: tfUrl, language: language });
            break;
        default: // "code"
            post.data = JSON.stringify({ code: tfCode, language: language });
            break;
        }
        post.dataType = "json";
    }
    $.post(post)
        .done(function(data) {
            clearLanguageFiles(languageTextbox);

            if (data.files) {
                let filenames = Object.keys(data.files);
                filenames.sort();
                for (let i = 0; i < filenames.length; i++) {
                    let fn = filenames[i];
                    let code = data.files[fn];
                    addLanguageFile(languageTextbox, fn, code);
                }
                $("#pulumi-code-download-icon").show();
                $("#pulumi-code-download-button").removeClass([ "opacity-50", "cursor-not-allowed" ]);
            } else {
                displayCouldNotConvert(languageTextbox);
            }

            if (data.diagnostics) {
                $("#pulumi-warnings").text(data.diagnostics);
                $("#pulumi-warnings").show();
            }
        })
        .fail(function(err) {
            let errorText = "An unspecified error occurred";
            if (err) {
                if (err.responseText) {
                    errorText = err.responseText;
                    try {
                        let errdata = JSON.parse(err.responseText);
                        if (errdata.error) {
                            errorText = errdata.error;
                        }
                    } catch {
                        // ignore.
                    }
                }
                errorText += " [" + err.statusText + " " + err.status + "]";
            }
            $("#pulumi-errors").text(errorText);
            $("#pulumi-errors").show();
            displayCouldNotConvert(languageTextbox);
        }).
        always(function() {
            $(document.body).css({ "cursor": "default" });
            $("#terraform-code, #terraform-url").css({ "cursor": "text" });
            $("pulumi-chooser[type='language'] > ul > li > a").css({ "cursor": "pointer" });
        });
}

// downloadCode downloads the currently converted code, if available.
function downloadCode() {
    let zip = new JSZip();
    for (let fn of Object.keys(currentCodeFiles)) {
        zip.file(fn, currentCodeFiles[fn]);
    }
    zip.generateAsync({ type: "blob" }).then(function(content) {
        // Use FileSaver.js to save the file, triggering download in the user's browser.
        saveAs(content, "kube2pulumi.zip");
    });
}

function getCannedExample(id) {
    if (id === undefined) {
        // Look up the currently selected example ID.
        id = $("#terraform-canned-example").children("option:selected").attr("id");
    }

    let comment = "#"; // to suppress Markdown lint errors.
    switch (id) {
        case "nginx_pod":
            return `apiVersion: v1
kind: Pod
metadata:
  namespace: frontend
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.14-alpine
      resources:
        limits:
          memory: 20Mi
          cpu: 0.2

`;

        case "pulumi_operator":
            return `
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pulumi-kubernetes-operator
spec:
  replicas: 1
  selector:
    matchLabels:
      name: pulumi-kubernetes-operator
  template:
    metadata:
      labels:
        name: pulumi-kubernetes-operator
    spec:
      serviceAccountName: pulumi-kubernetes-operator
      imagePullSecrets:
        - name: pulumi-kubernetes-operator
      containers:
        - name: pulumi-kubernetes-operator
          image: pulumi/pulumi-kubernetes-operator:v0.0.2
          command:
            - pulumi-kubernetes-operator
          args:
            - "--zap-level=debug"
          imagePullPolicy: Always
          env:
            - name: WATCH_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: OPERATOR_NAME
              value: "pulumi-kubernetes-operator"
`;

        case "auth":
            return `
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: null
  name: pulumi-kubernetes-operator
rules:
  \- apiGroups:
      - ""
    resources:
      - pods
      - services
      - services/finalizers
      - endpoints
      - persistentvolumeclaims
      - events
      - configmaps
      - secrets
    verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
  \- apiGroups:
      - apps
    resources:
      - deployments
      - daemonsets
      - replicasets
      - statefulsets
    verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
  \- apiGroups:
      - monitoring.coreos.com
    resources:
      - servicemonitors
    verbs:
      - get
      - create
  \- apiGroups:
      - apps
    resourceNames:
      - pulumi-kubernetes-operator
    resources:
      - deployments/finalizers
    verbs:
      - update
  \- apiGroups:
      - ""
    resources:
      - pods
    verbs:
      - get
  \- apiGroups:
      - apps
    resources:
      - replicasets
      - deployments
    verbs:
      - get
  \- apiGroups:
      - pulumi.com
    resources:
      - '*'
    verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
`;

case "aws_ec2":
    return `${comment} This Terraform sample provisions an AWS EC2 instance running Ubuntu.
${comment} Choose a language on the right hand side -- or try replacing it with your own!

data "aws_ami" "ubuntu" {
most_recent = true

filter {
name   = "name"
values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]
}

filter {
name   = "virtualization-type"
values = ["hvm"]
}

owners = ["099720109477"] ${comment} Canonical
}

resource "aws_instance" "web" {
ami           = "\${data.aws_ami.ubuntu.id}"
instance_type = "t2.micro"

tags = {
Name = "HelloWorld"
}
}
`;

    case "azure_vm":
        return `${comment} This Terraform sample provisions an Azure Virtual Machine running Ubuntu.
${comment} Choose a language on the right hand side -- or try replacing it with your own!

resource "azurerm_resource_group" "example" {
name     = "example-resources"
location = "West Europe"
}

resource "azurerm_virtual_network" "example" {
name                = "example-network"
address_space       = ["10.0.0.0/16"]
location            = azurerm_resource_group.example.location
resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_subnet" "example" {
name                 = "internal"
resource_group_name  = azurerm_resource_group.example.name
virtual_network_name = azurerm_virtual_network.example.name
address_prefix       = "10.0.2.0/24"
}

resource "azurerm_network_interface" "example" {
name                = "example-nic"
location            = azurerm_resource_group.example.location
resource_group_name = azurerm_resource_group.example.name

ip_configuration {
name                          = "internal"
subnet_id                     = azurerm_subnet.example.id
private_ip_address_allocation = "Dynamic"
}
}

resource "azurerm_linux_virtual_machine" "example" {
name                = "example-machine"
resource_group_name = azurerm_resource_group.example.name
location            = azurerm_resource_group.example.location
size                = "Standard_F2"
admin_username      = "adminuser"
network_interface_ids = [
azurerm_network_interface.example.id,
]

os_disk {
caching              = "ReadWrite"
storage_account_type = "Standard_LRS"
}

source_image_reference {
publisher = "Canonical"
offer     = "UbuntuServer"
sku       = "16.04-LTS"
version   = "latest"
}
}
`;

    case "google_gke":
        return `${comment} This Terraform sample provisions a Google Kubernetes Engine (GKE) cluster.
${comment} Choose a language on the right hand side -- or try replacing it with your own!

resource "google_container_cluster" "primary" {
name     = "my-gke-cluster"
location = "us-central1"

${comment} We can't create a cluster with no node pool defined, but we want to only use
${comment} separately managed node pools. So we create the smallest possible default
${comment} node pool and immediately delete it.
remove_default_node_pool = true
initial_node_count       = 1

master_auth {
username = ""
password = ""

client_certificate_config {
issue_client_certificate = false
}
}
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
name       = "my-node-pool"
location   = "us-central1"
cluster    = google_container_cluster.primary.name
node_count = 1

node_config {
preemptible  = true
machine_type = "e2-medium"

metadata = {
disable-legacy-endpoints = "true"
}

oauth_scopes = [
"https://www.googleapis.com/auth/logging.write",
"https://www.googleapis.com/auth/monitoring",
]
}
}
`;

        default:
            return "";
    }
}

function loadCannedExample(id) {
    $("#terraform-code").val(getCannedExample(id));
}

function waitForElementToExists(selector, callback) {
    setTimeout(function () {
        var element = $(selector)[0];

        if (element) {
            return callback();
        } else {
            return waitForElementToExists(selector, callback);
        }
    }, 500);
}

$(function() {
    waitForElementToExist("pulumi-chooser[type='language'] > ul > li > a", function() {
        var validPages = [ "/kube2pulumi/", "/tf2pulumi/" ];
        var currentPath = window.location.pathname;

        // If this is not a *2pulumi page, return.
        if (validPages.indexOf(currentPath) === -1) {
            return;
        }

        // If there are querystring parameters populate the fields.
        let tfUrl = getQueryVariable("url");
        let tfCode = getQueryVariable("code");

        // Let's initialize the code conversion component.
        if (tfUrl) {
            $("#terraform-url").val(tfUrl);
            setCurrentInputKind("url");
            convertCode(getCurrentLanguage() || "typescript", "url");
        } else {
            if (tfCode) {
                $("#terraform-code").val(tfCode);
            } else {
                loadCannedExample();
            }
            setCurrentInputKind("code");
            convertCode(getCurrentLanguage() || "typescript", "code");
        }

        // We auto-submit the code based on user interaction, including (1) after they finish typing,
        // (2) if they hit enter in the URL box, (3) after selecting files to upload, and (4) when
        // switching the language in the right-hand converted code box.

        // After a while of no typing, submit.
        var typingTimer;
        let doneTypingMs = 1500;
        $("#terraform-code").keyup(function (e) {
            clearTimeout(typingTimer);
            if ($(this).val() !== "") {
                typingTimer = setTimeout(convertCode, doneTypingMs);
            }
        });
        $("#terraform-code").keydown(function (e) {
            clearTimeout(typingTimer);
        });
        $("#terraform-url").keyup(function (e) {
            clearTimeout(typingTimer);
            if ($(this).val() !== "" && e.which !== 13) {
                typingTimer = setTimeout(convertCode, doneTypingMs);
            }
        });
        $("#terraform-url").keydown(function (e) {
            clearTimeout(typingTimer);
            if (e.which === 13) {
                // If you hit enter in the URL bar, submit immediately.
                convertCode();
                return false;
            }
        });

        // After the file upload selector has occurred, submit.
        $("#terraform-upload").change(function (e) {
            let files = $("#terraform-upload")[0].files;
            if (files && files.length) {
                convertCode();
                return false;
            }
        });

        // Enable tabs within the code window, to make it easier to type code.
        $("#terraform-code").keydown(function (e) {
            if ((e.which || e.keyCode) === 9) {
                e.preventDefault();
                let start = this.selectionStart;
                let end = this.selectionEnd;
                $(this).val(
                    $(this).val().substring(0, start) +
                    "\t" +
                    $(this).val().substring(end)
                );
                this.selectionStart = this.selectionEnd = start + 1;
            }
        });

        // If the canned example is changed, use it to load the code.
        $("#terraform-canned-example").change(function (e) {
            loadCannedExample();
            convertCode();
        });

        // Hook up event handlers for the language choosers.
        $("pulumi-chooser[type='language'] > ul > li > a").each(function (i, e) {
            $(e).click(function() {
                // We need to check that the inputKind has been properly set and if it
                // has not, let's set the value to "code" and update the handler. If the
                // inputKind is defined we will "reset" the value by using jQuery to click
                // the element. We have seen a inconsistent bug where the code input will disappear
                // when changing a language. This is hacky way to "fix" it, while we work on redesigning
                // the architecture of these types of pages.
                let inputKind = getCurrentInputKind();
                if (inputKind === undefined) {
                    setCurrentInputKind("code");
                    inputKind = "code";
                } else {
                    setCurrentInputKind(inputKind);
                }

                convertCode($(e).text().trim().toLowerCase(), inputKind);
            });
        });
    });
})
