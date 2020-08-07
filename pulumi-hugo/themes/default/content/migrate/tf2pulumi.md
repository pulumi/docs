---
title: Convert Your Terraform to a Real Language
url: /tf2pulumi
layout: tf2pulumi
meta_desc: See what your Terraform HCL would look like in a real language thanks to Pulumi.
form:
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
---

<!-- Load up various Prism JS/CSS files needed to dynamically colorize results -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/prism.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-javascript.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-typescript.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-python.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-python.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-go.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-csharp.min.js" data-manual></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/themes/prism.min.css" />
<!-- JS for dynamically creating and downloading source as zips. -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.5.0/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.2/FileSaver.min.js"></script>

<div class="w-full mx-auto md:flex">

<div class="md:w-1/2 md:mr-2">

<h3 class="text-gray-700 text-center">Enter your Terraform</h3>
<div class="text-gray-500 text-center m-1 -mb-2 text-xs">
    (Don't worry, we send it over SSL and don't store it on our servers.)
</div>

{{< chooser input-kind "code,url,upload" >}}

{{% choosable input-kind "code" %}}

<p class="m-0 -mt-4 p-2 bg-purple-300 text-white font-bold font-mono font-xs"
    style="font-size: 0.75rem !important; color: #fff !important">main.tf</p>
<textarea id="terraform-code" rows="27"
    class="w-full px-6 py-4 text-gray-700 text-sm font-mono overflow-y-scroll overflow-x-hidden whitespace-pre"
    title="Enter a single-file HCL program's text; see the 'UPLOAD' tab for multi-file programs">
</textarea>

<p class="text-gray-700 text-xs mb-1">
    Canned Examples:
</p>
<select id="terraform-canned-example" class="text-gray-700 text-xs">
    <option id=""></option>
    <option id="aws_ec2" selected>AWS EC2 instance running Ubuntu</option>
    <option id="azure_vm">Azure Virtual Machine running Ubuntu</option>
    <option id="google_gke">Google Kubernetes Engine cluster</option>
</select>

{{% /choosable %}}

{{% choosable input-kind "url" %}}

<input id="terraform-url" type="text" class="px-6 py-4 text-gray-700 text-sm w-full" value="https://"
    title="Enter a URL to a single HCL file (e.g., https://raw.githubusercontent.com/pulumi/tf2pulumi/master/tests/terraform/aws/ec2/main.tf); see the 'UPLOAD' tab for multiple files">
</input>

{{% /choosable %}}

{{% choosable input-kind "upload" %}}

<input id="terraform-upload" type="file" multiple class="px-6 py-4 text-gray-700 text-sm w-full">
</input>

{{% /choosable %}}

{{< /chooser >}}

</div>

<div class="md:w-1/2 md:ml-2">

<h3 class="text-gray-700 text-center">Choose your Pulumi Language</h3>
<div class="text-gray-500 text-center m-1 -mb-2 text-xs">
    &nbsp;
</div>

<div id="pulumi-code-download-icon" class="float-right mt-4 mr-1 hidden">
    <button class="copy-button" onclick="downloadCode()"><i class="fa fa-download text-xl" title="Download"></i></button>
</div>

{{< chooser language "typescript,javascript,python,go,csharp" >}}

{{% choosable language "typescript" %}}

<div id="pulumi-code-typescript-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "javascript" %}}

<div id="pulumi-code-javascript-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "python" %}}

<div id="pulumi-code-python-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "go" %}}

<div id="pulumi-code-go-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "csharp" %}}

<div id="pulumi-code-csharp-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{< /chooser >}}

</div>

</div>

<pre id="pulumi-errors" class="text-center text-xs font-bold font-mono bg-gray-200 border-0 hidden" style="color:#ff0000"></pre>
<pre id="pulumi-warnings" class="text-center text-xs font-bold font-mono bg-gray-200 border-0 hidden" style="color:#cc6600"></pre>

<script>
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
function convertCode(language) {
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
    let tfIk = getCurrentInputKind();
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
    let post = {
        url: "https://ukfk72ln69.execute-api.us-west-2.amazonaws.com/stage/convert",
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
        saveAs(content, "tf2pulumi.zip");
    });
}

function getCannedExample(id) {
    if (id === undefined) {
        // Look up the currently selected example ID.
        id = $("#terraform-canned-example").children("option:selected").attr("id");
    }

    let comment = "#"; // to suppress Markdown lint errors.
    switch (id) {
        case "":
            return "";

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
            throw new Error("unrecognized canned example ID: " + id);
    }
}

function loadCannedExample(id) {
    $("#terraform-code").val(getCannedExample(id));
}

window.onload = function() {
    $(document).ready(function() {
        // If there are querystring parameters populate the fields.
        let tfUrl = getQueryVariable("url");
        let tfCode = getQueryVariable("code");
        if (tfUrl) {
            $("#terraform-url").val(tfUrl);
            setCurrentInputKind("url");
        } else {
            if (tfCode) {
                $("#terraform-code").val(tfCode);
            } else {
                loadCannedExample();
            }
            setCurrentInputKind("code");
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
                convertCode($(e).text().trim().toLowerCase());
            });
        });

        // Fire off a conversion just to get started using the default code snippet example.
        convertCode(getCurrentLanguage() || "typescript");
    });
}
</script>

<div class="text-center py-8">
    <a id="pulumi-code-download-button"
        class="btn btn-lg mr-4 opacity-50 cursor-not-allowed" onclick="downloadCode()">Download Code</a>
</div>
