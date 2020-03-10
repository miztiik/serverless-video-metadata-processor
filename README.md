# Serverless Video Metadata Extractor

Media processing applications often need information about what’s in audio and video files before they can do anything with those files. Video providers use it to get technical metadata about video codecs, frame rates, audio channels, duration, and more.

  ![Miztiik Serverless Video Metadata Extractor](images/serverless-video-metadata-processor-arch-00.png)

  Follow this article in **[Youtube](https://www.youtube.com/c/ValaxyTechnologies)**

1. ## Prerequisites

    This demo, instructions, scripts and cloudformation template is designed to be run in `us-east-1`. With few modifications you can try it out in other regions as well(_Not covered here_).

    - AWS CLI pre-configured - [Get help here](https://youtu.be/TPyyfmQte0U)
    - **Optional** AWS CDK Installed & Configured - [Get help here](https://www.youtube.com/watch?v=MKwxpszw0Rc)

1. ## ⚙️ Setting up the environment

    - Get the application code

        ```bash
        git clone https://github.com:miztiik/serverless-video-metadata-processor.git
        cd serverless-video-metadata-processor
        ```

1. ## 🚀 Deployment using AWS CDK

    If you have AWS CDK installed you can close this repository and deploy the stack with,

    ```bash
    # If you DONT have cdk installed
    npm install -g aws-cdk

    # Make sure you in root directory
    cd fargate-chat-app
    source .env/bin/activate
    pip install -r requirements.txt
    ```

    The very first time you deploy an AWS CDK app into an environment _(account/region)_, you’ll need to install a `bootstrap stack`, Otherwise just go aheadand   deploy using `cdk deploy`

    ```bash
    cdk bootstrap
    cdk deploy
    ```

1. ## 🔬 Test the app

    The `cdk deploy` command should provide you the application load balancer url to access the web app. _You can get the same from cloudformation outputs or in the ALB page.

    You should be seeing something like this,
    ![Server Chat App using Fargate](images/miztiik-fargate-chat-app_00.png)

1. ## Testing the solution

    - Upload a video to S3 Bucket, _A sample file is provided in the repo under `sample_events` directory_
    - After a few seconds check the dynamodb for new entry

    You should be able to see entry something similar to this,

    ```json
    {
    "media_id": "8a59cdca-e110-46bc-8798-25759c8d9711",
    "metadata": {
        "tracks": [
        {
            "audio_codecs": "AAC LC",
            "audio_format_list": "AAC LC",
            "audio_format_withhint_list": "AAC LC",
            "audio_language_list": "English",
            "codec_id": "mp42",
            "codec_id_url": "http://www.apple.com/quicktime/download/standalone.html",
            "codecid_compatible": "mp42/isom/avc1",
            "codecs_video": "AVC",
            "commercial_name": "MPEG-4",
            "complete_name": "/tmp/8a59cdca-e110-46bc-8798-25759c8d9711",
            "count": "332",
            "count_of_audio_streams": "1",
            "count_of_stream_of_this_kind": "1",
            "count_of_video_streams": "1",
            "datasize": "379880",
            "duration": 5568,
            "encoded_date": "UTC 2010-03-20 21:29:11",
            "file_last_modification_date": "UTC 2020-03-10 12:46:00",
            "file_last_modification_date__local": "2020-03-10 12:46:00",
            "file_name": "8a59cdca-e110-46bc-8798-25759c8d9711",
            "file_name_extension": "8a59cdca-e110-46bc-8798-25759c8d9711",
            "file_size": 383631,
            "fileextension_invalid": "braw mov mp4 m4v m4a m4b m4p m4r 3ga 3gpa 3gpp 3gp 3gpp2 3g2 k3g jpm jpx mqv ismv isma ismt f4a f4b f4v",
            "folder_name": "/tmp",
            "footersize": "3591",
            "format": "MPEG-4",
            "format_extensions_usually_used": "braw mov mp4 m4v m4a m4b m4p m4r 3ga 3gpa 3gpp 3gp 3gpp2 3g2 k3g jpm jpx mqv ismv isma ismt f4a f4b f4v",
            "format_profile": "Base Media / Version 2",
            "frame_count": "166",
            "frame_rate": "30.000",
            "headersize": "160",
            "internet_media_type": "video/mp4",
            "isstreamable": "No",
            "kind_of_stream": "General",
            "other_codec_id": [
            "mp42 (mp42/isom/avc1)"
            ],
            "other_duration": [
            "5 s 568 ms",
            "5 s 568 ms",
            "5 s 568 ms",
            "00:00:05.568",
            "00:00:05:16",
            "00:00:05.568 (00:00:05:16)"
            ],
            "other_file_size": [
            "375 KiB",
            "375 KiB",
            "375 KiB",
            "375 KiB",
            "374.6 KiB"
            ],
            "other_format": [
            "MPEG-4"
            ],
            "other_frame_rate": [
            "30.000 FPS"
            ],
            "other_kind_of_stream": [
            "General"
            ],
            "other_overall_bit_rate": [
            "551 kb/s"
            ],
            "other_overall_bit_rate_mode": [
            "Variable"
            ],
            "other_stream_size": [
            "3.67 KiB (1%)",
            "4 KiB",
            "3.7 KiB",
            "3.67 KiB",
            "3.671 KiB",
            "3.67 KiB (1%)"
            ],
            "other_writing_application": [
            "HandBrake 0.9.4 2009112300"
            ],
            "overall_bit_rate": 551194,
            "overall_bit_rate_mode": "VBR",
            "proportion_of_this_stream": "0.00980",
            "stream_identifier": "0",
            "stream_size": 3759,
            "tagged_date": "UTC 2010-03-20 21:29:12",
            "track_type": "General",
            "video_format_list": "AVC",
            "video_format_withhint_list": "AVC",
            "writing_application": "HandBrake 0.9.4 2009112300"
        },
        {
            "bit_depth": 8,
            "bit_rate": 465642,
            "bits__pixel_frame": "0.087",
            "chroma_subsampling": "4:2:0",
            "codec_configuration_box": "avcC",
            "codec_id": "avc1",
            "codec_id_info": "Advanced Video Coding",
            "color_primaries": "BT.709",
            "color_range": "Limited",
            "color_space": "YUV",
            "colour_description_present": "Yes",
            "colour_description_present_source": "Container / Stream",
            "colour_primaries_source": "Container / Stream",
            "colour_range_source": "Stream",
            "commercial_name": "AVC",
            "count": "378",
            "count_of_stream_of_this_kind": "1",
            "display_aspect_ratio": "1.750",
            "duration": 5533,
            "encoded_date": "UTC 2010-03-20 21:29:11",
            "encoded_library_name": "x264",
            "encoded_library_version": "core 79",
            "encoding_settings": "cabac=0 / ref=2 / deblock=1:0:0 / analyse=0x1:0x111 / me=umh / subme=6 / psy=1 / psy_rd=1.0:0.0 / mixed_ref=1 / me_range=16 / chroma_me=1 / trellis=0 / 8x8dct=0 / cqm=0 / deadzone=21,11 / chroma_qp_offset=-2 / threads=6 / nr=0 / decimate=1 / mbaff=0 / constrained_intra=0 / bframes=0 / wpredp=0 / keyint=300 / keyint_min=30 / scenecut=40 / rc_lookahead=40 / rc=crf / mbtree=1 / crf=20.0 / qcomp=0.60 / qpmin=10 / qpmax=51 / qpstep=4 / ip_ratio=1.40 / aq=1:1.00",
            "format": "AVC",
            "format_info": "Advanced Video Codec",
            "format_profile": "Baseline@L3",
            "format_settings": "2 Ref Frames",
            "format_settings__cabac": "No",
            "format_settings__reference_frames": 2,
            "format_url": "http://developers.videolan.org/x264.html",
            "frame_count": "166",
            "frame_rate": "30.000",
            "frame_rate_mode": "CFR",
            "height": 320,
            "internet_media_type": "video/H264",
            "kind_of_stream": "Video",
            "matrix_coefficients": "BT.709",
            "matrix_coefficients_source": "Container / Stream",
            "other_bit_depth": [
            "8 bits"
            ],
            "other_bit_rate": [
            "466 kb/s"
            ],
            "other_chroma_subsampling": [
            "4:2:0"
            ],
            "other_display_aspect_ratio": [
            "16:9"
            ],
            "other_duration": [
            "5 s 533 ms",
            "5 s 533 ms",
            "5 s 533 ms",
            "00:00:05.533",
            "00:00:05:16",
            "00:00:05.533 (00:00:05:16)"
            ],
            "other_format": [
            "AVC"
            ],
            "other_format_settings__cabac": [
            "No"
            ],
            "other_format_settings__reference_frames": [
            "2 frames"
            ],
            "other_frame_rate": [
            "30.000 FPS"
            ],
            "other_frame_rate_mode": [
            "Constant"
            ],
            "other_height": [
            "320 pixels"
            ],
            "other_kind_of_stream": [
            "Video"
            ],
            "other_scan_type": [
            "Progressive"
            ],
            "other_stream_size": [
            "315 KiB (84%)",
            "315 KiB",
            "315 KiB",
            "315 KiB",
            "314.5 KiB",
            "315 KiB (84%)"
            ],
            "other_track_id": [
            "1"
            ],
            "other_width": [
            "560 pixels"
            ],
            "other_writing_library": [
            "x264 core 79"
            ],
            "pixel_aspect_ratio": "1.000",
            "proportion_of_this_stream": "0.83953",
            "rotation": "0.000",
            "sampled_height": "320",
            "sampled_width": "560",
            "scan_type": "Progressive",
            "stream_identifier": "0",
            "stream_size": 322069,
            "streamorder": "0",
            "tagged_date": "UTC 2010-03-20 21:29:12",
            "track_id": 1,
            "track_type": "Video",
            "transfer_characteristics": "BT.709",
            "transfer_characteristics_source": "Container / Stream",
            "width": 560,
            "writing_library": "x264 - core 79"
        },
        {
            "bit_rate": 83051,
            "bit_rate_mode": "VBR",
            "channel_layout": "C",
            "channel_positions": "Front: C",
            "channel_s": 1,
            "codec_id": "mp4a-40-2",
            "commercial_name": "AAC",
            "compression_mode": "Lossy",
            "count": "280",
            "count_of_stream_of_this_kind": "1",
            "duration": 5568,
            "encoded_date": "UTC 2010-03-20 21:29:11",
            "format": "AAC",
            "format_additionalfeatures": "LC",
            "format_info": "Advanced Audio Codec Low Complexity",
            "frame_count": "261",
            "frame_rate": "46.875",
            "kind_of_stream": "Audio",
            "language": "en",
            "maximum_bit_rate": 91632,
            "other_bit_rate": [
            "83.1 kb/s"
            ],
            "other_bit_rate_mode": [
            "Variable"
            ],
            "other_channel_positions": [
            "1/0/0"
            ],
            "other_channel_s": [
            "1 channel"
            ],
            "other_compression_mode": [
            "Lossy"
            ],
            "other_duration": [
            "5 s 568 ms",
            "5 s 568 ms",
            "5 s 568 ms",
            "00:00:05.568",
            "00:00:05:26",
            "00:00:05.568 (00:00:05:26)"
            ],
            "other_format": [
            "AAC LC"
            ],
            "other_frame_rate": [
            "46.875 FPS (1024 SPF)"
            ],
            "other_kind_of_stream": [
            "Audio"
            ],
            "other_language": [
            "English",
            "English",
            "en",
            "eng",
            "en"
            ],
            "other_maximum_bit_rate": [
            "91.6 kb/s"
            ],
            "other_sampling_rate": [
            "48.0 kHz"
            ],
            "other_stream_size": [
            "56.4 KiB (15%)",
            "56 KiB",
            "56 KiB",
            "56.4 KiB",
            "56.45 KiB",
            "56.4 KiB (15%)"
            ],
            "other_track_id": [
            "2"
            ],
            "proportion_of_this_stream": "0.15067",
            "samples_count": "267264",
            "samples_per_frame": "1024",
            "sampling_rate": 48000,
            "stream_identifier": "0",
            "stream_size": 57803,
            "streamorder": "1",
            "tagged_date": "UTC 2010-03-20 21:29:12",
            "title": "Stereo",
            "track_id": 2,
            "track_type": "Audio"
        }
        ]
    },
    "title": "sample_media.mp4"
    }
    ```

1. ## 🧹 CleanUp

    If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or _you can delete the stack from console as well_

    - _Any other customer resources, you have created for this demo_

    ```bash
    # Delete from cdk
    cdk destroy

    # Delete the CF Stack, If you used cloudformation to deploy the stack.
    aws cloudformation delete-stack \
        --stack-name "MiztiikAutomationStack" \
        --region "${AWS_REGION}"
    ```

    This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

## 👋 Buy me a coffee

Buy me a coffee ☕ through [Paypal](https://paypal.me/valaxy), _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

### 📚 References

1. [Source Repo](https://aws.amazon.com/blogs/media/running-mediainfo-as-an-aws-lambda-function)

1. [Stackoverflow oserror-libmediainfo-so](https://stackoverflow.com/questions/52516828/oserror-libmediainfo-so-0-cannot-open-shared-object-file-no-such-file-or-dire)

### ℹ️ Metadata

**Level**: 300
