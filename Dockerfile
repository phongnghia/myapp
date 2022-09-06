FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip mysql-server libmysqlclient-dev
#    apt-get install -y vim

RUN service mysql start

RUN pip3 install Django mysqlclient Pillow==6.2.0


RUN mkdir /myapp/
WORKDIR  /myapp/

COPY requirements.txt .
COPY myapp/ myapp/
COPY myresume/ myresume/
COPY manage.py .
#COPY query/ query/
#COPY media/ media/


EXPOSE 3306 8000
