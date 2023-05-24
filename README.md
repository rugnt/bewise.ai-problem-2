# `bewise.ai` второе тестовое задание

## Установка

### Для начало работы необходимо

- Установить <a href="https://docs.docker.com/compose/install/" target="_blank">docker-compose</a> (если не установлен)
- Убедиться, что 8000 и 5432 порты открыты
- Убедиться, что нет контейнеров с названиями app, db и alembic_migrations

### 1. Клонировать репозиторий

    $ git clone https://github.com/rugnt/bewise.ai-problem-2.git

### 2. Перейти в директорию bewise.ai-problem-2

    $ cd bewise.ai-problem-2

### 3. Запустить docker-compose

    $ docker-compose up --build

### 4. Открыть приложение <a href="http://localhost:8000/docs" target="_blank"> http://localhost:8000/docs </a>


## Пример работы


### Создаем пользователя

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/981afef4-faf5-48c2-a1a1-2ae5ee6608d7)

### Однако при повторном отправки запроса выводится ошибка, что такой пользователь уже существует

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/bb36e987-226e-4b60-8ebe-1bf185f5cfaf)

## Загружаем аудиозапись пользователя в формате wav

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/851dc823-c699-4bfe-8301-6a31bc434a6c)

## Повторно вводим данные

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/32273d2e-39d7-4442-8aef-3316fee0464b)

## При отправке файла другого формата API выдает ошибку

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/34646015-81a8-4798-8d6d-277e8497c05a)

## При неверном токене или id пользователя выводится 404 ошибка

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/57b6ee4a-4ba8-4859-9952-687e58f1e8d2)

## Получаем аудиозапись по ссылке

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/43d99884-13e7-42fa-80a4-a25886f1024e)

## При вводе неверных данных получаем ошибку

![изображение](https://github.com/rugnt/bewise.ai-problem-2/assets/93862774/8b2a2914-5d45-4fa7-9d53-d6eeeaa7262e)




