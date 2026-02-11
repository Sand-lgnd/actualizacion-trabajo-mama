use bd_mama;
select * from producto;

create database bd_mama;
use bd_mama;
create table producto (
id_prod varchar(7) primary key not null,
producto varchar(100),
peso decimal(7,3));

create table movimiento(
tipo_mov ENUM('S','E'),
fecha_mov date,
id_prod varchar(7) not null, 
cantidad int,
FOREIGN KEY (id_prod) REFERENCES producto(id_prod));


