FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

copy . .

EXPOSE 8000

CMD ["uvicorn","final.py","--host","0.0.0.0","--port","8000"]