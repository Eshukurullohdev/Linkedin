# Python bazasi
FROM python:3.11-slim

# .pyc fayllarni yozmaslik va loglarni buffer qilmaslik
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Loyihani ishlash joyiga o‘tkazish
WORKDIR /app

# Kerakli kutubxonalarni o‘rnatish
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Butun loyihani konteyner ichiga nusxalash
COPY . .

# Django dev serverni ishga tushurish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
