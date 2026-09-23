FROM python:3.9

WORKDIR /app

COPY . /final

RUN pip install -r requirement.txt

EXPOSE 8000

CMD ["uvicorn","final.py","--host","0.0.0.0","--port","8000"]