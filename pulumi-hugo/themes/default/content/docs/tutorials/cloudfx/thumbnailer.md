---
title: "Multi-Cloud Containers and Serverless"
meta_desc: Learn how to build a video thumbnailer using serverless, containers, and cloud
           infrastructure.
aliases: ["/docs/quickstart/cloudfx/tutorial-thumbnailer/"]
---

In this tutorial, we'll use JavaScript to combine serverless, containers and cloud infrastructure together into a
"Colada" application. We use serverless functions as event triggers and containers for longer-running tasks.

We'll build an application that extracts a thumbnail from a video using AWS Lambda and
[Fargate](https://aws.amazon.com/fargate/). Below is the architecture of the Pulumi application. The
code for this tutorial is [available on GitHub](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer),
and a video walkthrough of this example is [available on YouTube](https://www.youtube.com/watch?v=Bofmh1qnNSE).

<img src="/images/docs/quickstart/video-thumbnail-diagram.png" alt="Video thumbnail diagram" width="600">

{{< aws-js-prereqs >}}

## Create and deploy the project

1. Make sure [Docker](https://docs.docker.com/install/) is installed and running.

1. Run `pulumi new`:

    ```bash
    $ mkdir video-thumbnail && cd video-thumbnail
    $ pulumi new aws-javascript
    ```

1. Replace the contents of `index.js` with the following:

    ```javascript
    const cloud = require("@pulumi/cloud-aws");

    // A bucket to store videos and thumbnails.
    const bucket = new cloud.Bucket("bucket");
    const bucketName = bucket.bucket.id;

    // A task which runs a containerized FFMPEG job to extract a thumbnail image.
    const ffmpegThumbnailTask = new cloud.Task("ffmpegThumbTask", {
        build: "./",  // folder containing the Dockerfile
        memoryReservation: 512,
    });

    // When a new video is uploaded, run the FFMPEG task on the video file.
    // Use the time index specified in the filename (e.g. cat_00-01.mp4 uses timestamp 00:01)
    bucket.onPut("onNewVideo", bucketArgs => {
        console.log(`*** New video: file ${bucketArgs.key} was uploaded at ${bucketArgs.eventTime}.`);
        const file = bucketArgs.key;

        const thumbnailFile = file.substring(0, file.indexOf('_')) + '.jpg';
        const framePos = file.substring(file.indexOf('_')+1, file.indexOf('.')).replace('-',':');

        ffmpegThumbnailTask.run({
            environment: {
                "S3_BUCKET":   bucketName.get(),
                "INPUT_VIDEO": file,
                "TIME_OFFSET": framePos,
                "OUTPUT_FILE": thumbnailFile,
            },
        }).then(() => {
            console.log(`Running thumbnailer task.`);
        });
    }, { keySuffix: ".mp4" });

    // When a new thumbnail is created, log a message.
    bucket.onPut("onNewThumbnail", bucketArgs => {
        console.log(`*** New thumbnail: file ${bucketArgs.key} was saved at ${bucketArgs.eventTime}.`);
        return Promise.resolve();
    }, { keySuffix: ".jpg" });

    // Export the bucket name.
    exports.bucketName = bucketName;
    ```

    This code declares the following resources:

    - **Cloud infrastructure**. S3 bucket for videos and still frames. We define a [stack output property]({{< relref "/docs/intro/concepts/stack.md#outputs" >}}) `bucketName`, to easily retrieve this value after the project has been deployed.
    - **Containers**. Uses [cloud.Task]({{< relref "/docs/reference/pkg/nodejs/pulumi/cloud#Task" >}}), which is a high-level, convenient component for working with containers. The component automatically provisions a container registry instance in ECR, runs a Docker build, and saves the Docker image to the provisioned ECR instance. It also defines an ECS task and configures it to use the built image.
    - **Serverless functions**
      - The Lambda function `onNewVideo` is triggered whenever a new `.mp4` video file is uploaded to the S3 bucket. The Lambda extracts the time index that is encoded in the video filename (in the form `file_mm-ss`) and launches the container task.
      - The Lambda function `onNewThumbnail` is triggered when a new `.jpg` thumbnail file is uploaded to the S3 bucket, and prints a message to the log file.

1. In the same directory, create a `Dockerfile` with the following contents. For the container setup, it uses an existing container for FFmpeg ad installs Python and the AWS CLI. When the container is started, it copies the video file from S3, runs `ffmpeg`, and copies the output back to S3.

    ```docker
    FROM jrottenberg/ffmpeg

    RUN apt-get update && \
        apt-get install python-dev python-pip -y && \
        apt-get clean

    RUN pip install awscli

    WORKDIR /tmp/workdir

    ENTRYPOINT \
      echo "Starting ffmpeg task..." && \
      echo "Copying video from S3" && \
      aws s3 cp s3://${S3_BUCKET}/${INPUT_VIDEO} ./${INPUT_VIDEO} && \
      ffmpeg -v error -i ./${INPUT_VIDEO} -ss ${TIME_OFFSET} -vframes 1 -f image2 -an -y ${OUTPUT_FILE} && \
      echo "Copying thumbnail to S3" && \
      aws s3 cp ./${OUTPUT_FILE} s3://${S3_BUCKET}/${OUTPUT_FILE}
    ```

1. Install the `@pulumi/cloud-aws` NPM package:

    ```bash
    $ npm install --save @pulumi/cloud-aws @pulumi/cloud
    ```

1. Configure Pulumi to use AWS Fargate. (Note: Fargate is currently available only in `us-east-1`, `us-east-2`, `us-west-2`, and `eu-west-1`).

    ```bash
    $ pulumi config set cloud-aws:useFargate true
    ```

1. Preview and deploy changes via `pulumi up`, which will take a few minutes. During the preview phase, Pulumi runs the Docker build.

    ```bash
    $ pulumi up
    Previewing update of stack 'thumbnailer-testing'
    ...

    Diagnostics:
      ...
      global: global
        info: Building container image 'pulum-dc8d99de-container': context=./docker-ffmpeg-thumb

    Do you want to perform this update? yes
    Updating stack 'thumbnailer-testing'
    Performing changes:
    ...

    ---outputs:---
    bucketName: "bucket-0c91106"

    info: 32 changes performed:
        + 32 resources created
    Update duration: 1m48.486679173s
    ```

## Test the application

To test the application, we'll upload a video to S3, view the running application logs, then download the thumbnail from S3.

### 1. Upload a video to S3

- Download [a short sample video](https://github.com/pulumi/examples/blob/master/cloud-js-thumbnailer/sample/cat.mp4?raw=true) to your project folder.

- Copy the video to S3, encoding the time index in the filename (00:01 becomes `00-01`):

    ```
    $ aws s3 cp cat.mp4 s3://$(pulumi stack output bucketName)/cat_00-01.mp4
    upload: cat.mp4 to s3://bucket-0c91106/cat_00-01.mp4
    ```

### 2. View logs

Run `pulumi logs -f` for the streaming logs of the Lambda functions as well as the Fargate task. Note that the log contains a prefix that matches the functions and tasks in your code, such as `onNewVideo` and `ffmpegThumbTask`:

```
$ pulumi logs -f
Collecting logs for stack thumbnail-quickstart-dev since 2018-05-25T13:32:27.000-07:00.

 2018-05-25T14:29:17.935-07:00[                    onNewVideo] *** New video: file cat_00-01.mp4 was uploaded at 2018-05-25T21:29:17.230Z.
 2018-05-25T14:29:22.319-07:00[                    onNewVideo] Running thumbnailer task.
 2018-05-25T14:30:25.995-07:00[               ffmpegThumbTask] Starting ffmpeg task...
 2018-05-25T14:30:25.995-07:00[               ffmpegThumbTask] Copying video FROM S3
download: s3://bucket-756b44a/cat_00-01.mp4 to ./cat_00-01.mp4    pleted 256.0 KiB/666.5 KiB (1.9 MiB/s) with 1 file(s) remaining
 2018-05-25T14:30:31.037-07:00[               ffmpegThumbTask] Copying thumbnail TO S3
upload: ./cat.jpg to s3://bucket-756b44a/cat.jpg                  pleted 86.6 KiB/86.6 KiB (303.9 KiB/s) with 1 file(s) remaining
 2018-05-25T14:30:34.298-07:00[                onNewThumbnail] *** New thumbnail: file cat.jpg was saved at 2018-05-25T21:30:33.724Z.
```

### 3. Download the thumbnail file

After you see the `*** New thumbnail` message, copy the jpg from S3.

```bash
$ aws s3 cp s3://$(pulumi stack output bucketName)/cat.jpg .
download: s3://bucket-0c91106/cat.jpg to ./cat.jpg
```

## Clean up

{{< cleanup >}}

## Next steps

For a version of this sample that includes AWS Rekognition, see the [Video Thumbnailer with Machine Learning](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer-machine-learning) JavaScript example.

For an example application that connects two containers, see the [Voting App](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app) TypeScript sample.
