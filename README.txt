# Práctica obligatoria 2 - Sistema con Spring Boot, Frontend y API Flask

## Descripción

Este proyecto corresponde a la práctica obligatoria 2 de la asignatura de Sistemas Distribuidos.

El objetivo de la práctica es desarrollar una aplicación formada por:

- Un frontend web desarrollado con Spring Boot y Thymeleaf.
- Un backend Java desarrollado con Spring Boot.
- Un sistema de login sencillo con usuarios almacenados en base de datos.
- Una API desarrollada en Python con Flask.
- Acceso a bases de datos mediante contenedores Docker.
- Simulación y tratamiento de excepciones.
- Pruebas de los endpoints mediante Postman.

La aplicación permite probar llamadas correctas y llamadas con errores desde la interfaz web y desde Postman.

---

## Tecnologías utilizadas

- Java
- Spring Boot
- Spring Security
- Spring Data JPA
- Hibernate
- Thymeleaf
- Python
- Flask
- MySQL
- PostgreSQL
- Docker
- Docker Compose
- Postman
- Git

---

## Arquitectura general

La arquitectura de la práctica se divide en varios servicios:


Usuario
  |
  v
Frontend Thymeleaf / Spring Boot
  |
  v
Backend Spring Boot
  |
  v
API Python Flask
  |
  v
Base de datos PostgreSQL


Acceso rápido

Aplicación Spring Boot:

http://localhost:7001

API Flask:

http://localhost:5000

Credenciales de prueba:

Usuario: admin
Contraseña: admin