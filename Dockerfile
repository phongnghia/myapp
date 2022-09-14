FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip mysql-server libmysqlclient-dev python3-venv
#    apt-get install -y vim

RUN service mysql start

RUN pip3 install Django mysqlclient Pillow==6.2.0


RUN mkdir /myapp/
WORKDIR  /myapp/

COPY requirements.txt .
COPY myapp/ myapp/
COPY myresume/ myresume/
COPY manage.py .
COPY database.sh /usr/local/bin/entry-point
#COPY query/ query/
#COPY media/ media/

RUN chmod 777 /usr/local/bin/entry-point

EXPOSE 3306 8000

# ENTRYPOINT ["entry-point"]