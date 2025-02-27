
# La Peliculera

Este es un proyecto para la asignatura de Gestión de Sistemas Empresariales del FP Superior de Desarrollo de Aplicaciones Multiplataforma (DAM) en el IES Ventura Rodríguez.

El objetivo de este proyecto es desarrollar un módulo para Odoo que gestione una tienda de películas, permitiendo la administración de inventario, ventas y clientes.

## Características

- Gestión de películas y su stock.
- Registro y administración de clientes.
- Procesamiento de ventas y alquileres.
- Integración con Odoo para un flujo de trabajo eficiente.

## Tecnologías utilizadas

- **Odoo** (Framework y ERP)
- **Python** (Para la lógica del módulo)
- **XML** (Para vistas y datos)
- **PostgreSQL** (Base de datos)

## Descarga

Descargar la última versión del módulo desde [aquí](https://github.com/AbelMoroEducaMadrid/LaPeliculeraOdooModule/releases/latest).
- **La_Peliculera_x.x.x** (Modulo portable odoo)
- **La_Peliculera_Docker_x.x.x** (Version con docker para despliegue rapido)
- **sample_data** (Datos de prueba para cargar en el módulo)

## Instalación

Para facilitar la configuración del entorno, puedes utilizar Docker. A continuación, se detallan los pasos para ejecutar el proyecto en un contenedor Docker. Si ya tienes un despliegue propio de Odoo, puedes ir al ultimo paso.

### 1. Instalar Docker

Si aún no tienes Docker y Docker Compose instalados en tu máquina, sigue los siguientes pasos según tu sistema operativo:

- **Windows y macOS**: Descarga Docker Desktop desde [aquí](https://www.docker.com/products/docker-desktop).
- **Linux**: Sigue las instrucciones de instalación de Docker en la [documentación oficial](https://docs.docker.com/engine/install/).

También necesitarás Docker Compose, que puedes instalar siguiendo las instrucciones [aquí](https://docs.docker.com/compose/install/).

### 2. Clonar el repositorio

Primero, clona el repositorio de GitHub en tu máquina local:

```bash
git clone https://github.com/AbelMoroEducaMadrid/LaPeliculeraOdooModule.git
cd LaPeliculeraOdooModule
```

### 3. Construir y levantar los contenedores Docker

Una vez que hayas clonado el repositorio, utiliza el siguiente comando para construir y levantar los contenedores de Docker en segundo plano:

```bash
docker-compose up -d --build
```

Este comando realizará lo siguiente:

- `--build`: Construirá las imágenes de Docker si es necesario.
- `-d`: Levantará los contenedores en segundo plano.

### 4. Verificar que los contenedores están en ejecución

Para asegurarte de que los contenedores se han levantado correctamente, puedes ejecutar:

```bash
docker-compose ps
```

Esto te mostrará una lista de los contenedores en ejecución.

### 5. Acceder a Odoo

Una vez que los contenedores estén en ejecución, podrás acceder a Odoo en tu navegador en la siguiente dirección:

[http://localhost:8069](http://localhost:8069)

### 6. Activar el módulo en Odoo

1. Inicia sesión en Odoo como administrador.
2. Dirígete a la sección de aplicaciones.
3. Actualiza la lista de aplicaciones para incluir "La Peliculera".
4. Instala el módulo de "La Peliculera" desde la lista de aplicaciones.
