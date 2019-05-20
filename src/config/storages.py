"""Custom Media Storages"""
from filebrowser_safe.storage import S3BotoStorageMixin
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage, S3BotoStorageMixin):
    """Enable Boto3 Storage to interact with Mezzanine file browser"""
