import settings
import uvicorn
import os

from services import (
    convert_audio_and_add_in_db, create_user_in_db, get_audio_from_db
)
from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse


app = FastAPI()
templates = Jinja2Templates(settings.TEMPLATES_URL)
media = settings.MEDIA_URL

# Если папки нет, то мы её создаем
if not os.path.exists(media):
    os.mkdir(media)

@app.get('/record')
async def get_audio(user: str, id: int) -> FileResponse:
    '''Получение аудиозаписи'''
    file_path = await get_audio_from_db(user, id)
    return FileResponse(file_path, media_type="audio/mpeg", filename="audio.mp3")


@app.post('/create_user', status_code=201)
async def create_user(username: str) -> dict:
    '''Создание пользователя'''
    user_id, token = await create_user_in_db(username)
    return {'user_id': user_id, 'token': token}


@app.post('/add_audio', status_code=201)
async def add_audio(request: Request, user_id: int, token: str, file: UploadFile) -> dict:
    '''Загрузка аудиозаписи в wav формате и конвертация его в mp3'''
    audio_id = await convert_audio_and_add_in_db(user_id, token, file)
    return {'audio_url': f'{request.base_url}record?id={audio_id}&user={user_id}'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=settings.APP_PORT)
