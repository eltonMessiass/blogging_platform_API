FROM python:3.12-slim
LABEL maintainer="eltonmessias10@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./blogging_platform_API /blogging_api
COPY ./scripts /scripts

WORKDIR /blogging_api

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /blogging_api/requirements.txt && \
    adduser --disabled-password --no-create-home eltonmessias && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R eltonmessias:eltonmessias /venv && \
    chown -R eltonmessias:eltonmessias /data/web/static && \
    chown -R eltonmessias:eltonmessias /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod -R +x /scripts

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    bash \
    netcat-openbsd

ENV PATH="/scripts:/venv/bin:$PATH"

USER eltonmessias

CMD [ "/scripts/commands.sh" ]
