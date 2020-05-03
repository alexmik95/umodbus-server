FROM alpine:latest

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3
RUN python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel
RUN ln -sf python3 /usr/bin/python && \
    ln -sf pip3 /usr/bin/pip
