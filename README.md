# Reto Final - API LFG (Looking For Groups) #

#### Tabla de contenido

- [1. Descripción](#1-descripción)
- [2. Requisitos Funcionales](#2-requisitos-funcionales)
- [3. Objetivos](#3-objetivos)
- [4. Stack Tecnológico](#4-stack-tecnológico)
- [5. Cómo usar la aplicación](#5-cómo-usar-la-aplicación)
- [6. Licencia](#6-licencia)
- [7. Registro de cambios](#7-registro-de-cambios)
- [8. Créditos](#8-créditos)

## 1. Descripción

Dada la situación sanitaria, una empresa tecnológica a estado trabajando en remoto desde marzo de 2020. Esto ha implicado que nuestros compañeros hayan perdido el contacto humano que siempre se ha tenido, y es algo que la empresa desea cambiar.

La empresa quiere dar un impulso a la manera que tienen los trabajadores de relacionarse, permitiendo que contacten entre ellos creando grupos de interés.

Una primera fase de este proyecto es crear una **aplicación web LFG**, que permita que los empleados puedan contactar con otros compañeros para formar grupos para jugar a un videojuego, con el objetivo de poder compartir un rato de ocio _afterwork_.

## 2. Requisitos Funcionales

Los requisitos funcionales de la aplicación son los siguientes:

1. **RF** - Los usuarios se tienen que poder registrar a la aplicación, estableciendo un usuario/contraseña.
1. **RF** - Los usuarios tienen que autenticarse a la aplicación haciendo login.
1. **RF** - Los usuarios tienen que poder crear Partías (grupos) por un determinado videojuego.
1. **RF** - Los usuarios tienen que poder buscar Partías seleccionando un videojuego.
1. **RF** - Los usuarios pueden entrar y salir de una Party.
1. **RF** - Los usuarios tienen que poder enviar mensajes a la Party. Estos mensajes tienen que poder ser editados y borrados por su usuario creador.
1. **RF** - Los mensajes que existan a una Party se tienen que visualizar como un chat común.
1. **RF** - Los usuarios pueden introducir y modificar sus datos de perfil, por ejemplo, su usuario de Steam.
1. **RF** - Los usuarios tienen que poder hacer logout de la aplicación web.

## 3. Objetivos

Realizar una API REST completa, con Django, que cumpla con los requisitos anteriormente planteados.

Que además proporcione y asegure:

- Registro de usuarios.
- Login de usuarios, auth + token.
- CRUD de los diferentes modelos.
- Excelente Readme (IMPORTANTE).

Y como preferidos:

- Buen naming en las variables.
- Aplicación de buenas prácticas.

## 4. Stack Tecnológico

Para el desarrollo de la API utilizaremos PostgreSQL con Django:

- PostgreSQL.
- Python (3.6 o superior).
- VirtualEnv propio.
- Django para la estructura de proyecto.
- Django Rest Framework encargado de la serialización de objetos JSON.
- JWT.

Como Sistema Control de Versiones se utilizará Git, hosteado en Github, haciendo uso de Git-Flow.

## 5. Cómo usar la aplicación

### Configurar el entorno

```shell
python -m pipenv install
python -m django lfg/manager.py makemigrations
python -m django lfg/manager.py migrate
```

### Ejecutar la aplicación

```shell
python -m django lfg/manager.py runserver
```

### Desde la web

El superusuario es:

- **user**: admin
- **pass**: 1234

_Testeado contra fuerza bruta para que no se pueda acceder_

### Desde la API

Una vez iniciada la aplicación con `... runserver`

`http://localhost:8000/{entidad}`

## 6. Licencia

El proyecto utiliza la licencia **MIT**, para más información, acceda al fichero [LICENSE](LICENSE)

## 7. Registro de cambios

Todos los cambios _relevantes_ realizados al proyecto/repositorio quedarán registrados en el fichero [CHANGELOG.md](CHANGELOG.md).

## 8. Créditos

- Proyecto ideado por [Jose Marín](https://es.linkedin.com/in/jos%C3%A9-mar%C3%ADn-20013460) como docente parte del equipo de [Geekshubs](https://www.geekshubsacademy.com)
- A Geekshubs por el [Bootcamp de Backend en Python](https://bootcamp.geekshubsacademy.com/online/backend-python/)
- A Valencia Digital Summit 2021, el evento que me hizo obtener una beca con la que poder acceder al evento

# [⬆ Volver arriba ⬆](#reto-final-api-lfg-looking-for-groups)