# Используем официальный образ Python
FROM python:3.10

# Создаем директорию для вашего приложения
RUN mkdir /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY req.txt .

# Устанавливаем зависимости
RUN pip install -r req.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Делаем скрипты исполняемыми
RUN chmod a+x /app/docker/*.sh

# Определяем команду, чтобы начать приложение
#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000