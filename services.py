import uuid
import os
import re
import settings

from fastapi import UploadFile, HTTPException

from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

from models.session import async_session
from models.database import User, Audio

from sqlalchemy import select


async def convert_audio_and_add_in_db(user_id: int, token: str, wav_file: UploadFile) -> tuple:
    '''Получает загруженный файл, конвертирует, записывает в бд и '''
    async with async_session() as session:
        user = None
        if 32 <= len(token) <= 36:
            query = select(User).where((User.user_id == user_id) & (User.token == token))
            user = (await session.execute(query)).first()
        if user is None:
            raise HTTPException(status_code=404, detail='Пользователь или токен заданы некорректно')
        else:
            filename = f'{str(uuid.uuid4())}.mp3'
            while filename in os.listdir(settings.MEDIA_URL):
                filename = f'{str(uuid.uuid4())}.mp3'

            # Конвертируем файлы и записываем их в бд
            try:
                mp3_file = AudioSegment.from_file_using_temporary_files(wav_file.file, format='wav')
                mp3_file.export(os.path.join(settings.MEDIA_URL, filename), format='mp3')

                audio = Audio(
                    filename=filename,
                    user_id=user_id,
                )
                session.add(audio)
                await session.commit()

                audio_id = audio.audio_id
            except CouldntDecodeError:
                raise HTTPException(status_code=415, detail='Файл может быть только форматом wav')

    return audio_id


async def get_audio_from_db(user_id: int, audio_id: int) -> int:
    '''Получаем аудиозапись из бд'''
    query = select(Audio).where(Audio.audio_id == audio_id and Audio.user_id == user_id)
    async with async_session() as session:
        audio = (await session.execute(query)).first()

        if audio is None:
            raise HTTPException(status_code=404, detail="Файл не найден")
        else:
            # Получаем полный путь к файлу
            audio_url = os.path.join(settings.MEDIA_URL, audio[0].filename)

    return audio_url


async def create_user_in_db(username: str) -> tuple:
    '''Создает запись о пользователе'''
    # Валидация пользователя
    if not re.fullmatch(r'[a-zA-Z][a-zA-Z0-9_-]{2,63}', username):
        raise HTTPException(status_code=422, detail=
                       "Пользователь должен содержать только буквенные и цифровые символы.\n" \
                       "Размер имени пользователя должен находиться в диапазоне от 3 до 64"
                    )
    else:
        query = select(User).where(User.name == username)
        async with async_session() as session:
            # Проверка есть ли такой пользователь или нет
            if (await session.execute(query)).first() is not None:
                raise HTTPException(status_code=409, detail="Такой пользователь уже существует")
            else:
                # Создаем запись в бд
                new_user = User(name=username)
                session.add(new_user)
                await session.commit()

                user_id = new_user.user_id
                token = str(new_user.token)

    return user_id, token
