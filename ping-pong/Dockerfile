# Используем базовый образ Python
FROM python:3.10

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY app.py .

# Команда для запуска приложения
CMD ["python", "app.py"]