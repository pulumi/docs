# Code Examples in Docs

Our documentation site at [pulumi.com/docs](http://pulumi.com/docs) provides a variety of code examples embedded within our doc pages to help users understand and apply Pulumi concepts. Ensuring the accuracy and reliability of these examples is essential, which is why we have automated testing available.

> **Related documentation:**
> - [CONTRIBUTING.md](CONTRIBUTING.md) - General contribution guidelines
> - [STYLE-GUIDE.md](STYLE-GUIDE.md) - Comprehensive style and UX standards
> - [BLOGGING.md](BLOGGING.md) - Guidelines for blog posts that might include code examples

In order to get automated testing of your code example, the code must be added to a specific directory, and integrated into the document with a [Hugo shortcode](https://gohugo.io/content-management/shortcodes/). Once added, code examples are tested through an [automated pipeline](https://github.com/pulumi/docs/blob/master/.github/workflows/pull-request.yml) on a [regular cadence](https://github.com/pulumi/docs/blob/master/.github/workflows/scheduled-test.yml) to maintain ongoing accuracy.

## How it works

The testing process is limited to verifying code examples in the `/static/programs` directory. It verifies them by running either [`pulumi preview`](https://www.pulumi.com/docs/iac/cli/commands/pulumi_preview) or `make test` (if a `Makefile` is provided) on every example contributed to that directory. The `/static/programs` directory can house examples written in any of the Pulumi-supported languages.

The Hugo shortcode `{{< example-program ...>}}` imports the program into your Markdown file. It also handles the creation of the multi-language chooser widget for examples written in more than one language.

### Directory naming conventions

The `/static/programs` directory contains a collection of Pulumi programs, each in their own directory, using the following naming convention: `<program-name>-<language>`

For example, a program that shows how to use Pulumi to create an AWS S3 Bucket in TypeScript would be added to a directory called `aws-s3-bucket-typescript`. In this example, the program name is `aws-s3-bucket` and the language identifier is `typescript`. To create a version of the same example in Python, add a directory called `aws-s3-bucket-python`.

Later, in the Hugo shortcode, you would refer to both versions of this example using only the common *program name* portion of the directory name, e.g. `aws-s3-bucket`. The shortcode will pull both examples in and generate a code chooser widget containing the two translations of the same example.

The language identifier must be one of:
- `javascript`
- `typescript`
- `python`
- `csharp`
- `java`
- `go`
- `yaml`

The files checked in under these directories should be *complete* programs, including all files necessary for the program to run (and can contain appropriate subdirectories, hidden files, etc as needed per language).

## Including tested code examples in Markdown

To import the code example into your Markdown, use either the `{{< example-program ... >}}` or the `{{< example-program-snippet ... >}}` Hugo shortcode. These shortcodes will insert the code example at that specified location.

### The `example-program` shortcode
The `example-program` shortcode renders a complete listing of the Pulumi program(s) primary code file. It also generates a chooser to switch between multiple language versions of the program. 

For example, the `aws-s3-bucket` program we described above would 

`{{< example-program path="aws-s3-bucket" >}}`

Note that the `path` takes only the *program name* and not the languages. The language suffix is automatically inferred when rendering the code to the specific language chooser. This approach simplifies the consumption and testing of the code and helps ensure we maintain high-quality code examples in our documentation.

Per language, the file that will be displayed is as follows:

| Language     | File displayed                     |
| ------------ | ---------------------------------- |
| `javascript` | `index.js`                         |
| `typescript` | `index.ts`                         |
| `python`     | `__main__.py`                      |
| `csharp`     | `Program.cs`                       |
| `java`       | `src/main/java/myproject/App.java` |
| `go`         | `main.go`                          |
| `yaml`       | `Pulumi.yaml`                      |

If you do not want to show all languages of the example, you can limit it using the `languages` parameter on the shortcode. This parameter accepts a comma separated list of languages:

```go
// Only show the TypeScript and Python examples
{{< example-program path="aws-s3-bucket" languages="typescript,python">}}
```

It can also specify a non-default file and/or a range of lines from the file using the following format:
`<language>:<filename>:<from_n>-<to_n>`

For example. To show only lines 3-10 in the file `package.json` from the TypeScript version of an example called `aws-s3-bucket`, and also show all lines from the `requirements.txt` in the Python example, include the following `language` string:

```go
{{< example-program path="aws-s3-bucket" languages="typescript:package.json:3-10,python:requirements.txt:">}}
```

Note the trailing `:` on the Python segment. The format requires that *if* you use a filename, it *must* have a trailing colon, even if you don't want to specify a range of lines. However, if you don't want to specify a filename, you can add a line-range with only a single colon separating the language and the line range. 

### The `example-program-snippet` shortcode

The `example-program-snippet` shortcode renders a selection of lines from an example, instead of the entire program. This short code only imports the **raw lines of code as plaintext** and does *not* generate a chooser or a fenced code block, so that will need to be done in the Markdown file manually.

This shortcode uses the same conventions for selecting the directory and file to display as the `example-program` shortcode.

For example, to include only lines 10 through 20 from the TypeScript example:

`{{< example-program-snippet path="aws-s3-bucket" language="typescript" from="10" to="20" >}}`

Parameters:
- `path`: the name of the program subdirectory 
- `language`: the language of the code snippet
- `file`: specify a different file than the default for the language
- `from`: the line number at the start of the included block of code
- `to`: the line number at the end of the included block of code


## Steps to add a new code example

For this example we'll show how to add an example of a program that uses Pulumi to create an AWS S3 Bucket in both TypeScript and Python.

1. **Select an appropriate example program name.** The name should follow standard conventions for examples, be unique, and not already exist in the `/static/programs` directory. If there's an existing example with your preferred name, consider reusing it instead of creating a new one.

   For the purposes of this example, we'll use the name `aws-s3-bucket`. 
2. **Create directories for each language:**
   ```shell
    $ cd static/programs
    $ mkdir aws-s3-bucket-typescript
    $ mkdir aws-s3-bucket-python
    ```
3. **Initialize your Pulumi program(s):**
    ```shell
    $ cd aws-s3-bucket-typescript
    $ pulumi new `aws-typescript`
    $ cd ../aws-s3-bucket-python
    $ pulumi new `aws-python`
    ```
4. **Modify your program examples**, and verify that they work by running `pulumi preview` in each directory.
    ```shell
    $ cd aws-s3-bucket-typescript
    $ pulumi preview
    $ cd ../aws-s3-bucket-python
    $ pulumi preview
    ```
5. **Add the `example-program` shortcode** to your Markdown file to import the program. Specify the program name as the `path` argument:
    ```go
    {{< example-program path="aws-s3-bucket" >}}
    ```
6. Run `make serve` to render the documentation website locally, and very that it renders as expected

## Using a Makefile

If you're working with a code example that is not testable w/ `pulumi preview`, we also support including a `Makefile`. The `Makefile` should be located in the root directory of the example, and should include a `test` target. 

***Example:*** *A `Makefile` with a `test` target that runs TypeScript unit tests using `mocha`*
```make
test:
	npm install -g mocha
	npm install
	npm test
.PHONY: test
```

An example of a use case where this would be important would be a Pulumi Crossguard policy pack. This is something that needs to be documented, but it's not directly testable with `pulumi preview`. At minimum you'd need to add the `--policy` flag to do an integration test. Instead, it's better to run unit tests written in the same language that the policy pack is written in. You can use a `Makefile` to run anything we need to test that code. 

## Testing code examples locally

Generally it is not necessary to test all the code examples locally. This is a time consuming process as there are many examples. Instead, test only the programs that have changed, by navigating to each directory and running `pulumi preview`. You can get a list of the programs that have been changed before submitting a PR by first using `git add` to stage them, then running the following command from the root of the docs repo:

```shell
$ git diff --staged --name-only master | grep 'static/programs' | cut -d'/' -f3 | uniq
```

This should output a list of just the program directories that have changes in the current branch.

If for some reason you *do* want to re-run tests for all example programs, run `make test`. Note that this will require that you have all the necessary runtimes and dependencies for **all** example programs, which could be a large amount of runtimes, provider packages, language modules, etc, and may take more than an hour to run.

Another option is to run the `test.sh` script directly.

```sh
$ ./scripts/programs/test.sh
```

By default the script will run all tests. To run tests only for a specific example, use the `ONLY_TEST` environment variable.

```sh
$ ONLY_TEST="unit-test-policy-typescript" ./scripts/programs/test.sh
```