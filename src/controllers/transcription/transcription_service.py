import configparser
import os

from boto3 import session
import whisper
from botocore.config import Config
from werkzeug.utils import secure_filename

from src.datasource.transcription_repository import create_transcribtion, set_file_to_transcribtion, \
    set_text_to_transcribtion

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

def create_transcription_service(file, name:str, owner_user_id:str, category_id:str):
    filename = secure_filename(file.filename)

    transcription_model = create_transcribtion(
        name = name,
        owner_user_id = owner_user_id,
        category_id = category_id,
        file_name = filename
    )

    transcription_id = str(transcription_model.inserted_id)

    path = os.path.join('audio_files', transcription_id)
    os.mkdir(path)

    filepath = os.path.join('audio_files', transcription_id, filename)
    file.save(filepath)

    session_local = session.Session()
    client = session_local.client(
        service_name='s3',
        region_name='ru',
        endpoint_url=config['LOCAL']['ENDPOINT_URL'],
        aws_access_key_id=config['LOCAL']['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=config['LOCAL']['AWS_SECRET_ACCESS_KEY'],
        use_ssl=True,
        config=Config(signature_version='s3'),
    )

    file_url = 'https://ru.serverspace.store/v1/AUTH_4249254c5c0e4303be8092531155cf55/speech-to-text/'

    set_file_to_transcribtion(transcription_id, f'{file_url}{filepath}')

    result = client.upload_file(filepath, 'speech-to-text', filepath)

    model = whisper.load_model("small")
    result = model.transcribe(filepath)

    set_text_to_transcribtion(transcription_id, result)
    return result