# Weather Data Scraper

Este proyecto es un scraper de datos meteorológicos que utiliza Selenium para obtener información del tiempo de diferentes ciudades desde el sitio web [Meteored](https://www.meteored.cl/). El script está diseñado para ser fácil de usar y permite al usuario especificar la ciudad deseada mediante una entrada de usuario al ejecutar el script.

## Características

- **Configuración personalizada del WebDriver**: Incluye opciones para maximizar la ventana y navegar en modo incógnito.
- **Búsqueda dinámica de ciudades**: Permite al usuario ingresar el nombre de cualquier ciudad soportada por el sitio de Meteored.
- **Extracción y visualización de datos**: Recupera y muestra los datos meteorológicos en formato de DataFrame.
- **Guardado de resultados**: Los datos se pueden guardar en archivos CSV y Excel, nombrados dinámicamente según la ciudad consultada.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python y las siguientes bibliotecas:
- `pandas`
- `selenium`

Además, es necesario contar con el WebDriver para Chrome, el cual debe estar ubicado en la ruta especificada en el script o ajustarse según la configuración del sistema del usuario.

## Instalación de dependencias

Puedes instalar las dependencias necesarias usando `pip`:

```bash
pip install pandas selenium
