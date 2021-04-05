FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirement.txt /app/requirement.txt
RUN pip install -r requirement.txt
COPY . /app


