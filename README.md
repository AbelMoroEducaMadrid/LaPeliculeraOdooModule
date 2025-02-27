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

## Instalación

1. Descargar la última versión del módulo desde [aquí](https://github.com/AbelMoroEducaMadrid/LaPeliculeraOdooModule/releases/latest).

2. Copiar el módulo en la carpeta de addons de Odoo.

3. Reiniciar el servidor de Odoo y actualizar la lista de aplicaciones:

   ```sh
   sudo systemctl restart odoo
