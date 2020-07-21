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
<textarea id="terraform-code" rows="27" class="w-full px-6 py-4 text-gray-700 text-sm font-mono overflow-hidden whitespace-no-wrap"
    style="resize:vertical-auto" title="Enter a single-file HCL program's text; see the 'UPLOAD' tab for multi-file programs">
</textarea>

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

<p id="couldnt-convert-code" class="text-sm mt-8 text-center hidden" style="color:#cc6600; font-size:1rem">
    <b>Sorry, we couldn't convert your code.</b><br><br>
    There may be a problem with the code you submitted, or it might use a feature the
    converter doesn't yet support. To work with an engineer to help with your evaluation, please
    <a href="{{< relref "/about#contactus" >}})" class="link">contact us</a> or
    <a href="https://slack.pulumi.com" class="link">join our Community Slack</a>. We are here to help!
</p>

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

function setInputKind(ik) {
    $("pulumi-chooser[type='input-kind'] > ul > li > a").each(function (i, e) {
        if ($(e).text().trim().toLowerCase() === ik) {
            $(e)[0].click();
            return false;
        }
    });
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

// Now set up our event handler for conversion.
function convertCode(language) {
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
    $("#couldnt-convert-code").hide();
    clearLanguageFiles(languageTextbox);

    // Now read the various possible code sources.
    let tfCode = $("#terraform-code").val();
    let tfUrl = $("#terraform-url").val();
    let tfUploadFiles = $("#terraform-upload")[0].files;
    if (tfUrl === "https://") {
        tfUrl = "";
    }

    // If there isn't any code, bail early.
    if (tfCode === "" && tfUrl === "" && (!tfUploadFiles || !tfUploadFiles.length)) {
        $("#pulumi-errors").text("Error: Please enter the code to convert above, and then try again");
        $("#pulumi-errors").show();
        return;
    }

    // Make sure the right input tab is selected, for clarity.
    if (tfCode) {
        setInputKind("code");
    } else if (tfUrl) {
        setInputKind("url");
    } else if (tfUploadFiles.length) {
        setInputKind("upload");
    }

    // Add some "waiting" touches.
    $(document.body).css({ "cursor": "wait" });
    $("pulumi-chooser[type='language'] > ul > li > a").css({ "cursor": "wait" });
    addLanguageFile(languageTextbox, "…", "…");

    // Post to the endpoint and then, afterwards, add the result to the textbox.
    let post = {
        url: "https://ukfk72ln69.execute-api.us-west-2.amazonaws.com/stage/convert",
    };
    if (tfUploadFiles.length) {
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
        post.data = JSON.stringify({
            code: tfCode,
            url: tfUrl,
            language: language,
        });
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
                $("#couldnt-convert-code").show();
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
            $("#couldnt-convert-code").show();
        }).
        always(function() {
            $(document.body).css({ "cursor": "default" });
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

window.onload = function() {
    $(document).ready(function() {
        // If there are querystring parameters populate the fields.
        let tfUrl = getQueryVariable("url");
        let tfCode = getQueryVariable("code");
        if (tfUrl) {
            $("#terraform-url").val(tfUrl);
            setInputKind("url");
        } else {
            if (!tfCode) {
                // Populate a simple default example.
                let comment = "#"; // to suppress Markdown lint errors.
                tfCode = `${comment} This Terraform sample provisions an AWS EC2 instance running Ubuntu.
${comment} Choose a language and click CONVERT below -- or try replacing it with your own!

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

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "web" {
  ami           = "\${data.aws_ami.ubuntu.id}"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorld"
  }
}
`;
            }
            $("#terraform-code").val(tfCode);
            setInputKind("code");
        }

        // Clear the URL box when selecting the code box.
        $("#terraform-code").click(function() {
            $(this).select()
            $("#terraform-url").val("https://");
            $("#terraform-upload").val("");
        });

        // URL is pre-populated with "https://" -- select it upon click.
        // Also clear the code box since we can't issue multiple at once.
        $("#terraform-url").click(function() {
            $(this).select();
            $("#terraform-code").val("");
            $("#terraform-upload").val("");
        });

        // Clear the other text boxes when selecting.
        $("#terraform-upload").click(function() {
            $("#terraform-code").val("");
            $("#terraform-url").val("https://");
        });

        // If you hit enter in the URL bar, submit.
        $("#terraform-url").keypress(function (e) {
            if (e.which == 13) {
                convertCode();
                return false;
            }
        });

        // Hook up event handlers for the language choosers.
        $("pulumi-chooser[type='language'] > ul > li > a").each(function (i, e) {
            $(e)[0].addEventListener("click", function() {
                convertCode($(e).text().trim().toLowerCase());
            });
        });

        // Fire off a conversion just to get started using the default code snippet example.
        let currentLanguage = "";
        $("pulumi-chooser[type='language'] > ul > li.active > a").each(function (i, e) {
            currentLanguage = e.innerText.toLowerCase();
        });
        convertCode(currentLanguage || "typescript");
    });
}
</script>

<div class="text-center py-8">
    <a id="pulumi-code-download-button" class="btn btn-lg mr-4 opacity-50 cursor-not-allowed" onclick="downloadCode()">Download Results</a>
</div>
