from aws_cdk import aws_apigateway as _apigw
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_dynamodb as _dynamodb
from aws_cdk import aws_s3_notifications as _s3n
from aws_cdk import core


class global_args:
    '''
    Helper to define global statics
    '''
    OWNER = 'MystiqueAutomation'
    ENVIRONMENT = 'production'
    REPO_NAME = 'serverless-video-metadata-processor'
    SOURCE_INFO = f'https://github.com/miztiik/{REPO_NAME}'
    VERSION = '2020_03_20'


class ServerlessVideoMetadataProcessorStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        media_bkt = _s3.Bucket(
            self, "s3bucket", removal_policy=core.RemovalPolicy.DESTROY)

        core.Tag.add(media_bkt, key="isMediaBucket", value="True")

        # DynamodDB MediaTable
        media_metadata_table = _dynamodb.Table(self, "mediaMetadataTable",
                                               partition_key=_dynamodb.Attribute(
                                                   name="media_id", type=_dynamodb.AttributeType.STRING)
                                               )

        media_info_layer = _lambda.LayerVersion(self, "mediaInfoLayer",
                                                code=_lambda.Code.from_asset(
                                                    "lambda_src/layer_code/pymediainfo-python37.zip"),
                                                compatible_runtimes=[
                                                    _lambda.Runtime.PYTHON_3_7],
                                                license=f"This product uses MediaInfo (https://mediaarea.net/en/MediaInfo) library, Copyright (c) 2002-2020 MediaArea.net SARL.",
                                                description="Layer to extract video metadata"
                                                )

        # Defines an AWS Lambda resource
        with open("lambda_src/get_video_metadata.py", encoding="utf8") as fp:
            get_video_metadata_fn_handler_code = fp.read()
        get_video_metadata_fn = _lambda.Function(
            self,
            id='getVideoMetadaFn',
            function_name="get_video_metadata_fn",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.InlineCode(get_video_metadata_fn_handler_code),
            handler='index.lambda_handler',
            timeout=core.Duration.seconds(300),
            environment={
                "LD_LIBRARY_PATH": "/opt/python",
                "BUCKET_NAME": media_bkt.bucket_name,
                "S3_KEY_NAME": "3.mp4",
                "DDB_TABLE_NAME": media_metadata_table.table_name
            },
            layers=[media_info_layer]
        )
        core.Tag.add(get_video_metadata_fn, key="Owner",
                     value=global_args.OWNER)
        core.Tag.add(get_video_metadata_fn, key="ToKnowMore",
                     value=global_args.SOURCE_INFO)

        get_video_metadata_fn_perms = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW,
            resources=[
                f"{media_bkt.bucket_arn}/*",
                f"{media_bkt.bucket_arn}",
            ],
            actions=[
                "s3:GetObject",
                "s3:HeadBucket"
            ]
        )
        get_video_metadata_fn_perms.sid = "GetObjects"
        get_video_metadata_fn.add_to_role_policy(get_video_metadata_fn_perms)

        # Grant Lambda permissions to write to Dynamodb
        media_metadata_table.grant_read_write_data(get_video_metadata_fn)

        # Setup S3 Event Trigger for S3
        s3_event_trigger = media_bkt.add_event_notification(
            _s3.EventType.OBJECT_CREATED, _s3n.LambdaDestination(
                get_video_metadata_fn)
        )

        # Create API Gateway
        media_manager_api = _apigw.LambdaRestApi(
            self,
            'mediaManagerApiId',
            default_cors_preflight_options={
                "allow_origins": _apigw.Cors.ALL_ORIGINS,
                "allow_methods": _apigw.Cors.ALL_METHODS
            },
            handler=get_video_metadata_fn)

        v_metadata = media_manager_api.root.add_resource("v_metadata")
        v_metadata.add_method("POST")

        ###########################################
        ################# OUTPUTS #################
        ###########################################

        output_0 = core.CfnOutput(self,
                                  "SecuirtyAutomationFrom",
                                  value=f"{global_args.SOURCE_INFO}",
                                  description="To know more about this automation stack, check out our github page."
                                  )

        output_1 = core.CfnOutput(self,
                                  "MediaBucket",
                                  value=(
                                      f"https://console.aws.amazon.com/s3/buckets/"
                                      f"{media_bkt.bucket_name}"
                                  ),
                                  description=f"S3 Bucket for Media Storage"
                                  )

        output_2 = core.CfnOutput(self,
                                  "MediaInfoExtractorLambdaFunction",
                                  value=(
                                      f"https://console.aws.amazon.com/lambda/home?region="
                                      f"{core.Aws.REGION}"
                                      f"#/functions/"
                                      f"{get_video_metadata_fn.function_name}"
                                  ),
                                  description=f"Media info extractor function"
                                  )

        output_3 = core.CfnOutput(self,
                                  "MediaManagerApi",
                                  value=f"{media_manager_api.url}",
                                  description=f"Media Manager API Endpoint")
