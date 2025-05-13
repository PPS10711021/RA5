FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

CMD ["python3", "-m", "unittest", "test_calculadora.py"]
