import boto3
import logging
from botocore.exceptions import ClientError
from botocore.client import Config
from django.conf import settings
import uuid

logger = logging.getLogger(__name__)

def get_s3_client():
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=f'https://s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com',
            region_name=settings.AWS_S3_REGION_NAME,
            config=Config(
                signature_version='s3v4',
                s3={'addressing_style': 'path'} 
            )
        )
        return s3_client
    except Exception as e:
        logger.error(f"S3 클라이언트 생성 실패: {str(e)}")
        return None

def generate_presigned_url_for_upload(file_name=None, file_type=None, expiration=3600):
    s3_client = get_s3_client()
    if not s3_client:
        return {'error': 'S3 클라이언트 연결 실패'}
    
    # 파일 이름이 없으면 UUID 생성
    if file_name is None:
        file_name = f"{uuid.uuid4()}"
    else:
        # 파일 이름에 UUID를 추가하여 고유성 보장
        name_parts = file_name.rsplit('.', 1)
        if len(name_parts) > 1:
            file_name = f"{name_parts[0]}_{uuid.uuid4().hex[:8]}.{name_parts[1]}"
        else:
            file_name = f"{file_name}_{uuid.uuid4().hex[:8]}"
    object_key = f"uploads/{file_name}"
    
    try:
        params = {
            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
            'Key': object_key,
        }
        
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params=params,
            ExpiresIn=expiration
        )
        
        return {
            'success': True,
            'presigned_url': presigned_url,
            'file_name': file_name,
            'object_key': object_key,
            'expires_in': expiration
        }
    except ClientError as e:
        logger.error(f"Presigned URL 생성 실패: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }

def generate_presigned_url_for_download(object_key, expiration=3600, file_name=None):
    # 클라이언트 생성
    s3_client = get_s3_client()
    if not s3_client:
        return {'error': 'S3 클라이언트 연결 실패'}
    
    try:
        params = {
            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
            'Key': object_key,
        }
        
        # 다운로드 파일 이름 지정 (필요한 경우)
        if file_name:
            params['ResponseContentDisposition'] = f'attachment; filename="{file_name}"'
        
        # presigned URL 생성
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params=params,
            ExpiresIn=expiration
        )
        
        return {
            'success': True,
            'presigned_url': presigned_url,
            'object_key': object_key,
            'expires_in': expiration
        }
    except ClientError as e:
        logger.error(f"Presigned URL 생성 실패: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }