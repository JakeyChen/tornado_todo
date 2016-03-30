# $  mysql -u root -p < mysql_create.sql 
# Aa123456

drop database if exists tornado_todo;

create database tornado_todo;

GRANT ALL ON tornado_todo.* TO 'tornado' IDENTIFIED BY '123';

use tornado_todo;

create table todo (
    `id` mediumint not null auto_increment,
    `todo_text` varchar(50) not null,
    `finished` bool not null default 0,
    `post_date` datetime not null default now(),
    primary key (`id`)
 ) engine=innodb default charset=utf8;
