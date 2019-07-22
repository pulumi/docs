# Writing and Publishing a Pulumi Blog Post

So you're interested in contributing to the Pulumi blog? Great! Follow these steps to make it happen.

## Set Up Your Development Environment

If you haven't already, clone this repository and [follow the instructions in the README](https://github.com/pulumi/docs#pulumi-documentation-site) to set up your environment and run the development web  server. Once you're able to run

```
make serve
```

and browse the site locally, you're ready to move on to the next section.

## Make a New Post

1. Resist the temptation to copy-and-tweak an existing post! Instead, paste the following command into the terminal (at the root of the project) to generate a new one:

    ```
    hugo new --kind blog-post blog/my-new-post
    ```

    This will create a minimal post browsable at http://localhost:1313/blog/. You'll find the new post's source file at `content/blog/my-new-post/_index.md` containing the set of [Hugo front matter](https://gohugo.io/content-management/front-matter/) properties you'll need to get started:

    ```
    ---
    title: "My New Post"
    date: 2019-07-17T14:26:50-07:00
    draft: true
    meta_image: meta.png
    authors:
        - joe-duffy
    tags:
        - some-tag
    ---
    ```

    Feel free to adjust the title, authors (more on this below) and tags as appropriate. To change the post's URL, simply rename the folder containing `_index.md`; changing the folder name to `my-awesome-post`, for example, would result in a post ultimately published at https://www.pulumi.com/blog/my-awesome-post.

    **Keep in mind that only posts dated prior to "now" (meaning the moment the build process begins) and _not_ marked as `draft`s will published to production.** The development server renders both future and draft content (so you can work on scheduled posts in advance), but the build process does not; see below for details on scheduling posts for future publishing.

2. If you don't already have a [TOML](https://github.com/toml-lang/toml) file [in the `team` directory](https://github.com/pulumi/docs/tree/master/data/team/team) of the repo, create one now. For Pulumi employees, that file should look something like this:

    ```
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

    ```
    id = "mikhail-shilkov"
    name = "Mikhail Shilkov"
    title = "Microsoft Azure MVP and early Pulumi user"
    status = "guest"
    ...
    ```

    The `social` section, and the items within it, are optional.

    Once your team-member file's been created, update the new post's `authors` property to refer to your team member `id` string. If you're still running the development server, you should see the change reflected in the browser immediately.

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

### Media

#### Inline Images

To add images to the body of your post, first place them within in the folder containing the post's Markdown file (e.g., at `blog/my-new-post/platypus.png`), then reference them relatively:

```
![The humble platypus](platypus.png)
```

#### Social ("Meta") Images

When you generate a new post, an [OpenGraph](http://ogp.me/) placeholder image is included for you, and a reference to that image is added to the post's frontmatter as well, as its `meta_image`. The `meta_image` is meant to accompany the post in social previews (Twitter cards, unfurled Slack links, etc.) and on the Pulumi blog home page. It's optional, but recommended, as it can help to make your post more attractive and informative.

For best results, we suggest the following specs for the `meta_image`, largely based on [Twitter's dev docs](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards):

Aspect Ratio  | Minimum Size  | Format  | Background
------------- | ------------- | ------- | ------------------------
2:1           | 1600×800      | PNG     | Opaque (No Transparency)

Remember to replace the `meta_image` placeholder (or remove the property altogether and delete the placeholder `meta.png` file) before submitting your post.

#### Video

To embed a YouTube video, you can use Hugo's built-in [`youtube` shortcode](https://gohugo.io/content-management/shortcodes/#youtube), which takes the video's YouTube ID, obtainable from its public URL on youtube.com:

```
{{< youtube "kDB-YRKFfYE?rel=0" >}}
```

For videos belonging to the [Pulumi YouTube channel](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw), you'll usually want to append the `?rel=0` query parameter as well (as above), which tells YouTube to limit the suggestions it makes at the end of a video to those from the same YouTube channel. [Learn more about player parameters here](https://developers.google.com/youtube/player_parameters).

#### Tweets

There's a Hugo [shortcode for Tweets](https://gohugo.io/content-management/shortcodes/#tweet), too, which accepts a Tweet ID, accessible [from its permalink](https://twitter.com/jcreed/status/1147203941609984002):

```
{{< tweet 1147203941609984002 >}}
```

For more Hugo shortcode fun, [go here](https://gohugo.io/content-management/shortcodes).

## Done? Submit!

When you're ready to submit your post for review, issue a Pull Request against the `master` branch of the repo, and the team will have a look. Once merged &mdash; provided its `date` has passed and its `draft` status is no longer `true` &mdash; the post will be deployed to https://www.pulumi.com/.

## A Note on Dates and Scheduling for Future Publishing

If you'd like your post to be published at some future date or time, you have a couple of options.

Since the build process is triggered by (and so requires) a commit to `master`, you can either wait for the post's `date` to pass, remove its `draft` setting (or change it to `false`), and _then_ merge it, or leave its `draft` property `true`, merge, then change the property to `false` once the `date`'s gone by. If a post happens to get merged with `draft: false` and a future date, the resulting build will exclude the post, requiring a commit of some sort to occur _after_ its `date` in order to trigger a build and get the post published.

For this reason, leaving the `draft` property `true` until you're actually ready to publish gives you an easy way to kick off a build when the time comes.
