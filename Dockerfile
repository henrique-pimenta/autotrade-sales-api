FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /autotrade-sales-api

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.interface_adapters.fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
