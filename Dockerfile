FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip mysql-server libmysqlclient-dev

RUN service mysql start

RUN pip3 install Django mysqlclient Pillow==6.2.0

ENV HOME_APP /app

RUN mkdir HOME_APP
WORKDIR  $HOME_APP

COPY requirements.txt $HOME_APP
COPY myapp/ $HOME_APP/myapp
COPY myresume/ $HOME_APP/myresume
COPY manage.py $HOME_APP
COPY database /usr/local/bin/entry-point
COPY query/ $HOME_APP/query
COPY media/ $HOME_APP/media

RUN chmod 777 /usr/local/bin/entry-point

EXPOSE 8087

ENTRYPOINT ["entry-point"]