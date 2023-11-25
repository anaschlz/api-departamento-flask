create database rh;
use rh;

create table Departamento(
id_departamento INT NOT NULL AUTO_INCREMENT,
nome_departamento varchar(50) not null,
descricao text null,
primary key (id_departamento)
);