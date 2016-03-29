# $  mysql -u root -p < mysql_create.sql 
# Aa123456

drop database if exists tornado_todo;

create database tornado_todo;

GRANT ALL ON tornado_todo.* TO 'tornado' IDENTIFIED BY '123';
