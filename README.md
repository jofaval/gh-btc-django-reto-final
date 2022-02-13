# Reto Final - API LFG (Looking For Groups) #

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

## 3. Objectivos

En esta primera fase de proyecto el alumno ha de realizar una API REST completa, con Django, que cumpla con los requisitos anteriormente planteados.

Define los endpoints necesarios para que el backend pueda cumplir con lo establecido, nutriendo las diferentes vistas de frontend.

Además de esto el alumno ha de incluir la siguiente funcionalidad:

- Registro de usuarios.
- Login de usuarios, auth + token.
- CRUD de los diferentes modelos.
- Excelente Readme (IMPORTANTE).

Se valorará:

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

El proyecto se subirá a un repositorio público de GitHub y se valorará la existencia de ramas o la utilización de Git-Flow, así como diversos commits con la evolución del proyecto.

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