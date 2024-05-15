# Writing and Publishing a Pulumi Blog Post

So you're interested in contributing to the Pulumi blog? Great! Follow these
steps to make it happen.

## Set Up Your Development Environment

If you haven't already, clone this repository and
[follow the instructions in the README](https://github.com/pulumi/pulumi-hugo#running-hugo-locally)
to set up your environment and run the development web server.

Once you're able to run:

```zsh
make serve
```

If you can browse the site locally at http://localhost:1313/ then you are ready to
proceed to the next section.

## Make a New Post

1. Move onto a new branch for your blog post using `git checkout -b initials/your-blog-post` (replace initials with your initials, and replace your-blog-post with the name of your blog post).

1. Resist the temptation to copy-and-tweak an existing post! Instead, run the following
command into the terminal (at the root of the project). This will generate a new file,
including all the required frontmatter parameters.

   ```zsh
   make new-blog-post
   ```

   This will prompt you for a "slug" (a URL-friendly path) for your post and create a
   minimal post that you can browse to at http://localhost:1313/blog/. You'll find the new
   post's source file at `themes/default/content/blog/[your-slug]/_index.md` containing the set of
   [Hugo front matter](https://gohugo.io/content-management/front-matter/) properties you'll need to get started:

   ```
   ---
   title: "My New Post"
   date: 2019-07-17T14:26:50-07:00
   meta_image: meta.png
   authors:
       - joe-duffy
   tags:
       - some-tag
   ---
   ```

   Adjust the title and authors and add tags as appropriate (see the two headings below for more details). To change the post's URL, simply rename the folder containing `_index.md`; changing the folder name to `my-awesome-post`, for example, would result in a post ultimately published at https://www.pulumi.com/blog/my-awesome-post.

   **Important**

   The `title` will populate the `<title>` tag of the page, the `<h1>`, and the display value if it is linked to internally. This field has a strict 60 character limit because of SEO related limitations. If you would like to have a longer display title (i.e. the `<h1>` tag) then you will need to specify it by adding `allow_long_title: True` to the front matter. If you would like to display different text on internal links than what the `title` value is, you can also specify a `linktitle` value. Both the `allow_long_title` and `linktitle` values can be of any length. Below is an example of this:

   ```
   ---
   title: This a Page Title
   allow_long_title: true
   linktitle: This is the link text
   ...
   ---
   ```

   **Tags**

   Every tag added makes the overall tagging system harder to quickly grok and use. So, we strongly prefer using existing tags wherever possible. The tag system is as follows:

   - **Pulumi tags:** `pulumi-news` for company news (funding, certifications, etc.), `pulumi-events` for events we participate in or host, `pulumi-interns` for intern posts, `pulumi-enterprise` for enterprise-focused blog posts
   - **Cloud provider tags:** Only add a cloud provider tag if we expect to have multiple posts about the provider. Today, that means `aws`, `azure`, `google-cloud`, `digitalocean`
   - **Feature tags:** Only add a feature tag if we expect to have multiple posts about the feature. Today, that means `features` (for feature announcements), `aliases`, `continuous-delivery`, `logging`, `migration`, `native-providers`, `packages`, `policy-as-code`, `secrets`, `testing`.
   - **Technology/scenario tags:** Similar to feature tags, but focused on user scenarios. Today, that means `cloud-engineering`, `cloud-native`, `containers`, `data-and-analytics`, `development-environment`, `github-actions`, `kubernetes`, `serverless`.
   - **Language tags:** Any post that is language/ecosystem specific should have one or more of `.net`, `go`, `javascript`, `python`, `typescript`.

   **Canonical link**
   If you are posting a blog that originated somewhere else (for example, a syndicated community post) you will want to add the setting `canonical_url` for the URL where the blog post originated.

1. If you don't already have a [TOML](https://github.com/toml-lang/toml) file [in the `team` directory](https://github.com/pulumi/pulumi-hugo/tree/master/themes/default/data/team/team) of the repo, create one now. For Pulumi employees, that file should look something like this (your `id` can be any string, but we recommend `firstname-lastname`):

   ```toml
   id = "christian-nunciato"
   name = "Christian Nunciato"
   title = "Software Engineer"
   status = "active"

   [social]
   github = "cnunciato"
   linkedin = "cnunciato"
   twitter = "cnunciato"
   ```

   For community contributors, it's mostly the same, but with a `status` of `guest`, and a more informative `title`:

   ```toml
   id = "mikhail-shilkov"
   name = "Mikhail Shilkov"
   title = "Microsoft Azure MVP and early Pulumi user"
   status = "guest"
   ...
   ```

   The `social` section, and the items within it, are optional.

   Once your team-member file's been created, add your author image at [`themes/default/static/images/team`](https://github.com/pulumi/pulumi-hugo/tree/master/themes/default/static/images/team). The image should be a square JPG (400x400 max) named with your author `id` (e.g., `christian-nunciato.jpg`).

   Update the new post's `authors` property to use your author `id`. If you're still running the development server, you should see the change reflected in the browser immediately.

## Write Your Post

Posts are written in [Markdown](https://daringfireball.net/projects/markdown/) and rendered with [BlackFriday](https://github.com/russross/blackfriday), Hugo's default Markdown processor. GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) guide is a helpful syntax reference if you need it. You can also include HTML in your posts, if you need greater control over the output than Markdown can provide.

For formatting guidelines, see the Style Guide in [CONTRIBUTING.md](CONTRIBUTING.md#style-guide).

### Code Blocks

There are a couple of ways to do [syntax highlighing](https://gohugo.io/content-management/syntax-highlighting/) in Hugo, but we generally recommend [code fences](https://gohugo.io/content-management/syntax-highlighting/#highlight-in-code-fences), along with an optional language specifier &mdash; e.g., for TypeScript:

<pre>
```typescript
let bucket = new aws.s3.Bucket("stuff");
...
```
</pre>

[Additional languages are available](https://gohugo.io/content-management/syntax-highlighting/#list-of-chroma-highlighting-languages) as well.

### Notes

Shortcode for a warning note:

```
{{% notes type="warning" %}}
**DANGER** Will Robinson!
{{% /notes %}}
```

Shortcode for an info note:

```
{{% notes type="info" %}}
Using Bastion hosts is a best practice.
{{% /notes %}}
```

### Media

#### Inline Images

To add images to the body of your post, first place them within the folder containing the post's Markdown file (e.g., at `blog/my-new-post/platypus.png`), then reference them relatively:

```
![The humble platypus](platypus.png)
```

#### Social ("Meta") Images

> [!IMPORTANT]
> If you are adding _any_ logos to the meta image, you must absolutely ensure these are current. Using a wrong or outdated logo can have a severe negative impact on social sharing timelines due caching. 

When you generate a new post, an [OpenGraph](http://ogp.me/) placeholder image is included for you, and a reference to that image is added to the post's frontmatter as well, as its `meta_image`. The `meta_image` is meant to accompany the post in social previews (Twitter cards, unfurled Slack links, etc.) and on the Pulumi blog home page. It's optional, but recommended, as it can help to make your post more attractive and informative.

For best results, we suggest the following specs for the `meta_image`, largely based on [Twitter's dev docs](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards):

| Aspect Ratio | Recommended Size | Format | Background               |
| ------------ | ---------------- | ------ | ------------------------ |
| 2:1          | 1200×628         | PNG    | Opaque (No Transparency) |

Remember to replace the `meta_image` placeholder (or remove the property altogether and delete the placeholder `meta.png` file) before submitting your post.

For help creating your `meta_image`, check out our [Build Your Own Meta Image file](https://www.figma.com/file/TnD7nxjIxVvXq8w0W7awPG/Build-Your-Own-Meta-Image?node-id=0%3A1) in Figma. There you’ll find backgrounds, images, and logos to assemble the `meta_image` for your blog post.

To use Pulumi's primary brand font Gilroy in your `meta_image`, first [download Gilroy](https://drive.google.com/file/d/1893zFNypEQTvZU0J2Bz5_mVx6xa_7Zxh/view?usp=sharing) and install the file to your local font folder. Then [download the Figma font installer](https://www.figma.com/downloads/) to access your local fonts in Figma.

A few things to keep in mind when designing a `meta image`:

   - Avoid placing important text or graphic elements too close to the edges of the frame — elements at the edges may get cropped at some display ratios
   - Try to include at least one Pulumi identifier (word mark, Pulumipus) so viewers can tell at a glance that the image belongs to the Pulumi blog
   - Use dark text on light backgrounds, and light text on dark backgrounds to ensure readability
   - Remember to zoom out from your image and confirm it looks as you intend at a thumbnail size

#### Video

To embed a YouTube video, you can use Hugo's built-in [`youtube` shortcode](https://gohugo.io/content-management/shortcodes/#youtube), which takes the video's YouTube ID, obtainable from its public URL on youtube.com:

```
{{< youtube "kDB-YRKFfYE?rel=0" >}}
```

For videos belonging to the [Pulumi YouTube channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), you'll usually want to append the `?rel=0` query parameter as well (as above), which tells YouTube to limit the suggestions it makes at the end of a video to those from the same YouTube channel. [Learn more about player parameters here](https://developers.google.com/youtube/player_parameters).

#### Animated GIFs

GIFs are welcome, but should be optimized. In general, animated GIFs should be no more than 1200 pixels wide and 3 MB in size. If you need help optimizing your GIF, consider [Gifsicle](https://www.lcdf.org/gifsicle/); it's available through Homebrew and has an easy-to-use command-line API. For example, to resize (e.g., downscale) and optimize a GIF in place:

```bash
gifsicle ./my-animation.gif --resize-width=1200 --optimize=3 --batch
```

## Done? Submit!

When you're ready to submit your post for review, issue a Pull Request against the `master` branch of the repo, and the team will have a look. Once merged, the post will be deployed to https://www.pulumi.com/.

## Publicize your blog

When you create an awesome blog post, we want to make sure it reaches as many people as possible.
After your Pull Request is approved, but before merge/publication date, reach out in #blogs so that Marketing can broadcast your publication via social media.

## A Note on Dates and Scheduling for Future Publishing

Because the website is deployed in response to a commit to pulumi/docs `master`, it isn't possible to schedule a post to be released automatically at a precise date and time. (The `date` frontmatter property is used only for sorting and display purposes; it has no effect on whether or when a post gets published.) You can, however, influence the timing of the publishing process manually. See the [Merging and Releasing section of the README](README.md#merging-and-releasing) for details.

## Publishing Check List

- [ ] As mentioned, use the Hugo blog-post generator instead of copying another post: `make new-blog-post` (or alternatively, the more verbose but equivalent `hugo new --kind blog-post "themes/default/content/blog/[your-slug]"`)
- [ ] Spell and grammar check. Consider using a service such as [Grammarly](http://grammarly.com).
- [ ] Check for a break `<!--more-->` after the first paragraph, and ensure that your post's introduction looks right on the blog home page.
- [ ] Check that your meta_image appears properly on the blog home page. Do not use animated GIFs for preview images.
- [ ] Check that your meta_image is using the current logos for Pulumi and others.
- [ ] Preview locally. Check formatting, links, and images for appearance.
- [ ] Use the [Twitter card validator](https://cards-dev.twitter.com/validator) to check how the blog appears in a tweet (use the preview provided in the PR).
- [ ] Reach out in [#blogs](https://pulumi.slack.com/archives/CCBFCGU94) to make Marketing aware that your post is about to go live!
