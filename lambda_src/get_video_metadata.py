# -*- coding: utf-8 -*-
"""
.. module: get_video_metadata.py
    :Actions: Get 
    :copyright: (c) 2020 Mystique.,
.. moduleauthor:: Mystique
.. contactauthor:: miztiik@github issues
"""

import json
import logging
import os
import uuid

import boto3
import botocore
from botocore.exceptions import ClientError
from pymediainfo import MediaInfo

__author__ = 'Mystique'
__email__ = 'miztiik@github'
__version__ = '0.0.1'
__status__ = 'production'


class global_args:
    """
    Global statics
    """
    OWNER = 'Mystique'
    ENVIRONMENT = 'production'
    MODULE_NAME = 'get_video_metadata.py'
    LOG_LEVEL = logging.INFO


def set_logging(lv=global_args.LOG_LEVEL):
    '''
    Helper to enable logging
    '''
    logging.basicConfig(level=lv)
    LOGGER = logging.getLogger()
    LOGGER.setLevel(lv)
    return LOGGER


def _ddb_put_item(item):
    '''
    Insert Item to DynamoDB table
    '''
    _ddb = boto3.resource('dynamodb')
    _ddb_table = _ddb.Table(os.environ.get('DDB_TABLE_NAME'))
    LOGGER.info(f"DDB_ITEM:{item}")
    response = _ddb_table.put_item(
        Item=item
    )


def lambda_handler(event, context):
    # Initialize Logger
    global LOGGER
    LOGGER = set_logging(logging.INFO)
    resp = {'status': False, 'media_info': ''}
    LOGGER.info(f'Event: {event}')

    try:
        if 'Records' in event and 's3' in event.get('Records')[0]:
            BUCKET_NAME = event.get('Records')[0].get(
                's3').get('bucket').get('name')
            S3_KEY_NAME = event.get('Records')[0].get(
                's3').get('object').get('key')
        else:
            resp['error_message'] = f"S3 event is malformed. Event:{event}"
            return resp

        s3 = boto3.resource('s3')
        randomized_media_id = str(uuid.uuid4())
        tmp_filename = f"/tmp/{randomized_media_id}"
        s3.Bucket(BUCKET_NAME).download_file(
            S3_KEY_NAME, tmp_filename)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            LOGGER.infof(
                "The object does not exist: s3://{BUCKET_NAME}/{S3_KEY_NAME}")
        else:
            raise

    try:
        media_info = MediaInfo.parse(
            tmp_filename, library_file='/opt/python/libmediainfo.so.0')
        resp['status'] = True
        resp['media_info'] = media_info.to_json()
        item_info = {
            'media_id': randomized_media_id,
            'title': S3_KEY_NAME,
            'metadata': json.loads(media_info.to_json())
        }
        _ddb_put_item(item_info)
    except ClientError as e:
        LOGGER.error(
            f"Unable to extract mediainfo:{BUCKET_NAME}/{S3_KEY_NAME}")
        LOGGER.error(f"ERROR:{str(e)}")
        resp['error_message'] = str(e)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp
        })
    }


if __name__ == '__main__':
    lambda_handler({}, {})
