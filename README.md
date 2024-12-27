# Ideas_Varias
# Proyecto de Wallet Financiera con Python

Este proyecto es una implementación de una *Wallet Financiera* utilizando Python, basado en el tutorial del canal **Zero2Hero**. El tutorial original se puede encontrar en el siguiente [video](https://www.youtube.com/watch?v=n3XS3Wrp1bc&list=PL3lna2aeKsUd5GALdbjTTpEIvCdU-bz9K&index=6&ab_channel=Zero2Hero).

## Descripción

Este proyecto descarga información financiera de acciones, visualiza su rendimiento y permite realizar comparaciones entre diferentes tickers. Se utilizan bibliotecas populares como `yfinance`, `matplotlib` y `pandas` para manejar los datos y generar gráficos.

### Mejoras y detalles adicionales

Basado en el código original del tutorial, he agregado algunas mejoras y detalles extras, como:

- **Validación de entradas**: Ahora el usuario puede ingresar los tickers y las fechas con instrucciones claras y el programa valida las entradas para evitar errores comunes.
- **Manejo de errores**: Se mejoró la gestión de errores al momento de ingresar fechas y tickers incorrectos.
- **Interfaz más amigable**: Ahora el usuario recibe mensajes claros sobre cómo debe ingresar las fechas y los tickers.
- **Flexibilidad en la entrada**: Los usuarios pueden ingresar cualquier ticker y periodo de tiempo que deseen analizar.

## Instalación

Para instalar y ejecutar este proyecto, necesitas tener Python y las siguientes bibliotecas instaladas:

- `pandas`
- `matplotlib`
- `yfinance`

Puedes instalarlas usando pip:

```bash
pip install pandas matplotlib yfinance
