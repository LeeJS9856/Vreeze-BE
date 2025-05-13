from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from utils.s3_connect import generate_presigned_url_for_upload, generate_presigned_url_for_download

class S3APIView(APIView):
    permission_classes = [AllowAny]
    # S3 presignedUrl 생성하기 (업로드용)
    def post(self, request):
        file_name = request.data.get('file_name')
        content_type = request.data.get('content_type')
        
        if not file_name or not content_type:
            return Response(
                {"error": "file_name과 content_type은 필수입니다."}, 
                status=400
            )
            
        url = generate_presigned_url_for_upload(
            file_name=file_name,
            file_type=content_type
        )
        return Response({"presigned_url": url})
    
    # S3 presignedUrl 생성하기 (다운로드용)
    def get(self, request):
        file_name = request.query_params.get('file_name')
        
        if not file_name:
            return Response(
                {"error": "file_name은 필수입니다."}, 
                status=400
            )
            
        url = generate_presigned_url_for_download(file_name=file_name)
        return Response({"presigned_url": url})

    