FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y pkg-config python3 python3-pip mysql-server mysql-client libmysqlclient-dev python3-venv

RUN service mysql start

ENV HOME_APP /app
ENV LISTEN_PORT=8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir $HOME_APP
WORKDIR  $HOME_APP

COPY requirements.txt $HOME_APP
COPY myapp/ $HOME_APP/myapp
COPY myresume/ $HOME_APP/myresume
COPY manage.py $HOME_APP
COPY database $HOME_APP
COPY script /usr/local/bin/entry-point
COPY query/ $HOME_APP/query
COPY media/ $HOME_APP/media

RUN pip3 install -r $HOME_APP/requirements.txt

RUN chmod +x $HOME_APP/database
RUN chmod 777 /usr/local/bin/entry-point

RUN $HOME_APP/database

EXPOSE 3306 8000

ENTRYPOINT ["entry-point"]