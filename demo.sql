create database sqldemo;
create database sqldemo1;

#use sqldemo;
use demo;

show tables;

create table employee(emp_id int,emp_name varchar(10),emp_address varchar(20));



insert into employee(emp_id,emp_name,emp_address) values (1,'mano','bangalore');
insert into employee(emp_id,emp_name,emp_address) values (1,'raj',null);

describe employee;


alter table employee add column emp_email varchar(20);

describe employee;

drop table employee;


rename table pet to petdata;

truncate table petdata;


CREATE TABLE `movie_table` (
  `movie_id` int NOT NULL auto_increment,
  `title` varchar(50) NOT NULL,
  `rating` varchar(5) NOT NULL,
  `category` varchar(10) NOT NULL,
  `purchased` date NOT NULL,
  PRIMARY KEY  (`movie_id`)
) ENGINE=MyISAM AUTO_INCREMENT=94 DEFAULT CHARSET=utf8;


INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('83','Big Advenure','G','family','2002-03-06');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('89','Shiny Things, The','PG','drama','2002-03-06');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('88','End of the Line','R','misc','2001-02-05');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('87','A Rat named Darcy','G','family','2003-04-19');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('86','Head First Rules','R','action','2003-04-19');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('85','Mad Clowns','R','horror','1999-11-20');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('84','Greg: The Untold Story','PG','action','2001-02-05');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('93','Potentially Habitable Planet','PG','scifi','2001-02-05');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('92','Weird Things from Space','PG','scifi','2003-04-19');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('91','Shark Bait','G','misc','1999-11-20');
INSERT INTO `movie_table` (`movie_id`,`title`,`rating`,`category`,`purchased`) VALUES ('90','Take it Back','R','comedy','2001-02-05');





