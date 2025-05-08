# Базовый образ Python
FROM python:3.12

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY src /app/src

ENV PYTHONPATH=/app/src


#EXPOSE 8000
# CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
