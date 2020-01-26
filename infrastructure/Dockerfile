FROM python:alpine

RUN pip install --no-cache-dir awscli
COPY sync.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/sync.sh"]
