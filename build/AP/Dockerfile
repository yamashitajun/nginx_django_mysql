FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN apk --no-cache --virtual build-dependencies add \
        linux-headers \
        build-base \
        libffi-dev \
    && apk --no-cache add \
        bash-completion \
    && pip install -r requirements.txt \
    && apk del --purge build-dependencies

RUN pip install django-import-export \
 && pip install python-dateutil \
 && pip install pings

COPY docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

COPY check_admin.py /

#docker-compose.yml内の環境変数djangoのプロジェクト名（DJANGO_PROJECT_NAME）と合わせる
WORKDIR /DJANGO_PROJECT
COPY project/ /DJANGO_PROJECT/

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
