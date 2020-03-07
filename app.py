#!/usr/bin/env python3

from aws_cdk import core

from serverless_video_metadata_processor.serverless_video_metadata_processor_stack import ServerlessVideoMetadataProcessorStack


app = core.App()
ServerlessVideoMetadataProcessorStack(app, "serverless-video-metadata-processor")

app.synth()
