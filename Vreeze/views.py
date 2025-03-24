import boto3
from django.conf import settings
from rest_framework.views import APIView

class S3APIView(APIView) :
    # S3 presignedUrl 생성하기
    def get(self, uuid, request):
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )

        file_key = f"audio/{uuid}.aac"  # 저장된 S3 파일 경로

        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": settings.AWS_STORAGE_BUCKET_NAME, "Key": file_key},
            ExpiresIn=3600,  # Presigned URL 만료 시간 (1시간)
        )

        return url

    