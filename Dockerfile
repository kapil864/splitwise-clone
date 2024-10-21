FROM python:3.12.7-alpine3.20
LABEL maintainer="kapil864"

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser -H -D backend-user

COPY ./app /app

EXPOSE 8000
WORKDIR /app

ENV PATH="/venv/bin:$PATH"
USER backend-user

    