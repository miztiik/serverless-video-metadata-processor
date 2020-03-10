#!/usr/bin/env python3

from aws_cdk import core

from serverless_video_metadata_processor.serverless_video_metadata_processor_stack import ServerlessVideoMetadataProcessorStack


app = core.App()
ServerlessVideoMetadataProcessorStack(
    app, "serverless-video-metadata-processor")

app_name = app.node.try_get_context('app_name')


# Tag the stack resources
core.Tag.add(app, key="Owner", value=app.node.try_get_context('owner'))
core.Tag.add(app, key="OwnerProfile",
             value=app.node.try_get_context('github_profile'))
core.Tag.add(app, key="ToKnowMore",
             value=app.node.try_get_context('youtube_profile'))
core.Tag.add(app, key="GitRepo",
             value=app.node.try_get_context('github_repo_url'))

app.synth()
