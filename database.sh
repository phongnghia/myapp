#!/bin/sh

service mysql start

#mysql -uroot -ppassword --init-command='create database myresume_django;'
mysql -uroot -ppassword -e "create database myresume_django;"
cd /myapp
python3 manage.py migrate
python3 manage.py runserver