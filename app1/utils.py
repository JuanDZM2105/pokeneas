import os
import boto3
from dotenv import load_dotenv
import socket

load_dotenv()

def generar_url_firmada(key, bucket="pokeneas-images", expiracion=3600):
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
        region_name=os.getenv("AWS_DEFAULT_REGION")
    )
    s3 = session.client("s3")
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=expiracion
    )
    return url

def get_contenedor_id():
    return socket.gethostname()
