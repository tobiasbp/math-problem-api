FROM python:3.9

WORKDIR /fastapi

COPY ./src /fastapi/src

RUN pip install --no-cache-dir --upgrade -r /fastapi/src/requirements.txt


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]