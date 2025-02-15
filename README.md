# Assistant Coach

Приложение для тренеров и их клиентов, которое позволяет:
- Тренерам управлять тренировками клиентов через API.
- Клиентам просматривать свои тренировки и отправлять результаты выполнения.

## Технологии
- **Frontend**: ``React (TypeScript)``
- **Backend**: ``Django REST Framework (DRF)``
- **База данных**: `PostgreSQL`
- **Сервер**: `Nginx`
- **Контейнеризация**: `Docker`

---

## Содержание
1. [Установка и запуск](#установка-и-запуск)
   - [Для Linux](#для-linux)
   - [Для Windows](#для-windows)
2. [Работа с фикстурами](#работа-с-фикстурами)
   - [Загрузка фикстур](#загрузка-фикстур)
   - [Выгрузка фикстур](#выгрузка-фикстур)
3. [API](#api)
5. [Дополнительные настройки](#дополнительные-настройки)
6. [Лицензия](#лицензия)


---

## Установка и запуск

### Для Linux

1. **Установите Docker и Docker Compose**:
   - Убедитесь, что Docker и Docker Compose установлены. Если нет, выполните:
     ```bash
     sudo apt update
     sudo apt install docker.io docker-compose
     ```

2. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/Pankirbor/assistant_coach.git
   cd assistant_coach
   ```
3. **Запустите проект:**
 - Перейдите в ветку `development`, затем папку `infra` и запустите контейнеры:

    ```bash
    git checkout development
    cd infra
    sudo docker-compose up --build
    ```
4. **Выполните миграции:**
    - После первого запуска выполните миграции:

    ```bash
    sudo docker-compose exec web python manage.py makemigrations
    sudo docker-compose exec web python manage.py migrate
    ```
5. **[Загрузите данные из фикстур](#работа-с-фикстурами)**
6. **[Откройте приложение](#откройте-приложение-в-браузере)**

### Для Windows
**1. Установите Docker Desktop:**
    - Скачайте и установите [Docker Desktop](https://www.docker.com/products/docker-desktop).
    - Убедитесь, что Docker запущен.

2. **Клонируйте репозиторий:**
    - Откройте терминал (например, PowerShell) и выполните:

    ```bash
    git clone https://github.com/Pankirbor/assistant_coach.git
    cd assistant_coach
    ```
3. **Запустите проект:**
    - Перейдите в папку infra и запустите контейнеры:

    ```bash
    git checkout development
    cd infra
    sudo docker-compose up --build
    ```
4. **Выполните миграции:**
    - После первого запуска выполните миграции:

    ```bash
    sudo docker-compose exec web python manage.py makemigrations
    sudo docker-compose exec web python manage.py migrate
    ```
5. **[Загрузите данные из фикстур](#работа-с-фикстурами)**

#### Откройте приложение в браузере:
- Фронтенд: http://localhost:3000

- Админка Django: http://localhost:8000/admin
    - Username: Coach
    - Password: 1234
- Остановка контейнеров:
    ```bash
    cd infra/
    sudo docker-compose down -v
    ```

## Работа с фикстурами
- Загрузка фикстур (образцов данных в таблицы базы):
    - Убедитесь, что контейнер с бэкендом запущен.

    - Выполните команду для загрузки фикстур:

    ```bash

    sudo docker-compose exec web python manage.py loaddata backup_data.json
    ```

- Выгрузка фикстур если были добавлены данные в базу:
    - Выгрузка с запущенными контейнерами:
        1. **Запустите контейнер**:
            - Убедитесь, что ваш контейнер с приложением и базой данных запущен. Обычно это можно сделать с помощью команды:

            ```bash
            docker-compose up -d
            ```

        2. **Запустите команду dumpdata внутри контейнера:**
            - Используйте команду `exec` для выполнения команды `dumpdata` внутри вашего контейнера.

            ```bash
            # Эта команда создаст файл фиктуры my_fixture.json в директории fixtures вашего приложения внутри контейнера.
            docker exec -it web python manage.py dumpdata myapp --output=/app/fixtures/my_fixture.json
            ```



        3. Проверьте наличие файла фиктуры:
        - Убедитесь, что файл был создан успешно. Вы можете выполнить следующую команду, чтобы войти в контейнер и проверить наличие файла:
            ```bash
            docker exec -it web /bin/bash
            ls /app/fixtures/
            ```

            - Вы должны увидеть my_fixture.json в списке.

    - Теперь, когда файл фиктуры создан, вам нужно перенести его на локальный компьютер для сохранения в вашем репозитории. Для этого выполните следующие шаги:

        1. Скопируйте файл фиктуры на локальный компьютер:
            - Используйте команду:
            ```bash
            # Эта команда скопирует файл my_fixture.json в текущую директорию вашего локального компьютера.
            docker cp web:/app/fixtures/my_fixture.json assistant_coach/backend/backup_data_v1.json
            ```


        2. Проверьте файл на локальном компьютере:
            - Убедитесь, что файл был скопирован успешно, с помощью команды:
            ```bash
            ls -l ./my_fixture.json # Если файл отображается, значит, вы успешно переместили его на локальный компьютер.
            ```


        3. Добавьте файл в репозиторий:
            - Теперь, когда файл на локальном компьютере, вы можете добавить его в свой репозиторий:
            ```bash
            git add .
            git commit -m "Добавлены фиктуры"
            git push
            ```
    - Выгрузка при работе бэкэндом не в контейнере:
        - Убедитесь, что контейнеры приложения остановлены.
        ```bash
        cd infra/
        sudo docker-compose down -v
        ```
        - Выполните запуск по [инструкции](#бэкенд).

        - Выполните команду для выгрузки данных в фикстуру:

        ```bash
        python manage.py dumpdata --indent 2 > backup_data.json
        git add .
        git commit -m "Update backup_data.json"
        git push
    ```
## API
- Подробная документация API доступна после запуска проекта по адресу:
http://localhost/api/docs/swagger.

## Фронтенд
- Фронтенд написан на `React` с использованием `TypeScript`.
    - Основные функции:
        - Просмотр тренировок.
        - Отправка результатов выполнения упражнений.

- Запуск фронтенда отдельно:
    - Перейдите в папку `mini-app`:

    ```bash

    cd mini-app

    # Установите зависимости:
    npm install

    # Запустите сервер разработки:
    npm start
    ```
    - Фронтенд будет доступен по адресу: http://localhost:3000.

## Бэкенд
- Бэкенд написан на `Django REST Framework`. Основные функции:

    - Управление клиентами и тренировками.

    - Хранение данных в <del>PostgreSQL</del>.

- Запуск бэкенда отдельно
    - Перейдите в папку backend:

    ```bash

    cd backend

    # Создайте виртуальное окружение и установите зависимости:
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    pip install -r requirements.txt

    # Запустите сервер:
    python manage.py runserver
    ```
    - Бэкенд будет доступен по адресу: http://localhost:8000.

## Дополнительные настройки
- Переменные окружения
- Создайте файл `.env.dev` в папке `infra` с переменными окружения для `Django`, если он отсутствует:

```env
SECRET_KEY=ваш-секретный-ключ
DEBUG=True

# Пока не реализовано:
POSTGRES_DB=mydb
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```
