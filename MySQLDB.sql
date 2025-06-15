CREATE DATABASE PassManDB;
USE PassManDB;
CREATE TABLE storage (
    -> id int auto_increment primary key,
    -> link varchar(256) not null,
    -> login varchar(32) not null,
    -> password varchar(32) not null );
